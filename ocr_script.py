import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext('images/img1.png')

with open("ocr_output.txt", "w", encoding="utf-8") as file:
    for bbox, text, confidence in result:
        file.write(f"Detected Text: {text}\n")
        file.write(f"Confidence: {confidence:.2f}\n")
        file.write(f"Bounding Box: {bbox}\n")
        file.write("-" * 40 + "\n")

print("OCR result has been saved to 'ocr_output.txt'")
