from  PIL  import  Image 
import  pytesseract as tess
img=Image.open('practice2.jpg')
text=tess.image_to_string(img,lang='kor')
# text=text.split('\n')
img.show()
print(text)
