import cv2
import PIL.ImageGrab as screen
import numpy as np
import tesseract

image = screen.grab()
#image.save("asdfqwerty.png")
#api = tesseract.TessBaseAPI()
#api.Init(".","eng",tesseract.OEM_DEFAULT)
#api.SetPageSegMode(tesseract.PSM_SINGLE_WORD)
#api.SetPageSegMode(tesseract.PSM_AUTO)
#tesseract.SetCvImage(image,api)
#text=api.GetUTF8Text()
#conf=api.MeanTextConf()
#print text
