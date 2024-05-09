from utils.ocr_extraction import OCRProcessor
from utils.functions import cleaning_text
class DocumentProcessor:
    def __init__(self):
        self.ocr_processor = OCRProcessor()

    def process_document(self, pdf_path):  # Corrigido para receber o caminho do arquivo PDF
        ocr = self.ocr_processor.extract_text_from_pdf_paddle(pdf_path)  # Passa o caminho do arquivo PDF
        return ocr

if __name__ == "__main__":
    document_processor = DocumentProcessor()

    file_path = "files/teste_.pdf"
    ocr = document_processor.process_document(file_path)
    clean_ocr = cleaning_text(ocr)
    print(clean_ocr)
