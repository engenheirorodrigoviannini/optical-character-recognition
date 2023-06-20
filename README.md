# Optical Character Recognition (OCR) Functions

This repository contains three OCR (Optical Character Recognition) functions implemented in Python. Each function takes an image file as input and extracts text from the image using different OCR libraries or APIs.

## Functions

1. `extract_azure_ocr(filepath)`: This function utilizes the Azure Computer Vision API to perform OCR on the given image file. It converts text in image format to human-        readable character format. The function returns the extracted text as a string.

2. `extract_google_ocr(filepath)`: This function uses the Google Cloud Vision API for OCR. It converts text in image format to human-readable character format. The function     returns the extracted text as a string.

3. `extract_paddle_ocr(filepath)`: This function leverages the PaddleOCR library for OCR. It converts text in image format to human-readable character format. The function      returns the extracted text as a string along with a message indicating the result status.

## Usage

To use any of the OCR functions, follow these steps:

1. Install the required libraries:
   - For Azure OCR: Install the Azure Cognitive Services Python SDK.
   - For Google OCR: Install the Google Cloud Vision Python SDK.
   - For Paddle OCR: Install the PaddleOCR library.

2. Import the required libraries and functions into your Python script:
   ```python
   # For Azure OCR
   from azure.cognitiveservices.vision.computervision import ComputerVisionClient
   from msrest.authentication import CognitiveServicesCredentials
   from YOUR_MODULE import extract_azure_ocr

   # For Google OCR
   from google.cloud import vision
   from YOUR_MODULE import extract_google_ocr

   # For Paddle OCR
   import cv2
   from paddleocr import PaddleOCR
   from YOUR_MODULE import extract_paddle_ocr

3. Provide the path to the image file you want to extract text from.

4. Call the respective OCR function with the image file path as an argument:
  # For Azure OCR
  result = extract_azure_ocr(filepath)

  # For Google OCR
  result = extract_google_ocr(filepath)

  # For Paddle OCR
  result, status = extract_paddle_ocr(filepath)

5. Process the result variable returned by the OCR function as needed.
  Ensure that you have valid credentials or API keys for the respective OCR services (Azure, Google Cloud Vision) and configure them appropriately in your code.
  Make sure you have an internet connection to access the cloud-based OCR services (Azure, Google Cloud Vision).

