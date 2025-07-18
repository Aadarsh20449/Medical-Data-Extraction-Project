from pdf2image import convert_from_path
import cv2
import pytesseract
import numpy as np
from PIL import Image

from backend.src.parser_prescription import PrescriptionParser
from backend.src.parser_patient_details import PatientDetailsParser

POPPLER_PATH = 'C:/poppler-24.08.0/Library/bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(img):
    #use ADAPTIVE THRESHOLDING 
    #convert colorful image to gray backgoround image
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(gray,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_LINEAR)
    processed_image = cv2.adaptiveThreshold(
        resized_image,255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        61#trail and error value BLOCK SIZE
        ,
        11#trail and error value C value constant
    )
    return processed_image

def extract(filepath,filetype):
    #extract text from the file 
    pages = convert_from_path(filepath,poppler_path=POPPLER_PATH)

    document_text = ''
    for page in pages:
        #preprocess image 
        processed_image = preprocess_image(page)
        #extract data 
        text = pytesseract.image_to_string(processed_image,lang='eng')
        #add to whole text
        document_text += '\n'+text

    if filetype == 'prescription':
        extracted_data = PrescriptionParser(document_text).parse()
    elif filetype == 'patient_details':
        extracted_data = PatientDetailsParser(document_text).parse()

    return extracted_data


if __name__ == '__main__':
    print("Extract function called...")
    data = extract(
        r'C:\Users\manik\OneDrive\Documents\S\Ps\Medical_Data_Extraction_Project\backend\resources\prescription\pre_2.pdf',
        'prescription')
    print("Text Extracted:")
    print(data)

    
    
