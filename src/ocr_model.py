
from paddleocr import PaddleOCR

def recognize_handwriting(image_path):
 
    ocr_model = PaddleOCR(use_angle_cls=True, lang='en')  
    
    result = ocr_model.ocr(image_path)
   
    recognized_text = [line[1][0] for line in result[0]]
    
    return recognized_text
