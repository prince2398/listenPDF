from PIL import Image
from wand.image import Image as wi
import io
import pytesseract
import sys


#get pages as image blobs from pdf
def pdf2image(pdfName,resolution= 300,imgFormat= 'jpeg'):

    pdf = wi(filename= pdfName,resolution = resolution)
    pdfImage = pdf.convert(imgFormat)

    imgBlobs = []

    for img in pdfImage.sequence:
        imgPage = wi(image= img)
        imgBlobs.append(imgPage.make_blob(imgFormat))

    return imgBlobs

#convert imageBlobs given by pdf2image to strings list
def img2text(imgBlobs,lang = 'eng'):
    pageText = []

    for imgBlob in imgBlobs:
        img = Image.open(io.BytesIO(imgBlob))
        text = pytesseract.image_to_string(img,lang=lang)
        pageText.append(text)

    return pageText


#convert pdf to text
def pdf2text(pdfName,lang='eng'):
    imgBlobs = pdf2image(pdfName= pdfName)
    Text = img2text(imgBlobs= imgBlobs)
    return Text

#main
if __name__ == '__main__':
    if(len(sys.argv)>1):
        pdfFile = sys.argv[1]
    else:
        print("Argument Missing: Name of PDF File")
        exit()
    Strings =  pdf2text(pdfName = pdfFile)
    # with open('Strings.txt','wb') as file:

    x = 0
    for string in Strings:
        x=x+1
        print("Page ",x)
        print(string)

#end
