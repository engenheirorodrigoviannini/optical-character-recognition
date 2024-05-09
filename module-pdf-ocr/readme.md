<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documentação do Projeto</title>
</head>
<body>
    <h1>Documentação do Projeto</h1>
    
    <h2>Projeto: module-pdf-ocr</h2>

    <h3>main.py</h3>
    <p>Este arquivo contém a classe DocumentProcessor, que é responsável por processar documentos PDF.</p>
    <p>A funcionalidade principal é:</p>
    <ul>
        <li>Processar um documento PDF e extrair texto usando OCR (Reconhecimento Óptico de Caracteres).</li>
    </ul>
    <pre><code class="python">from utils.ocr_extraction import OCRProcessor

class DocumentProcessor:
    def __init__(self):
        self.ocr_processor = OCRProcessor()

    def process_document(self, pdf_path):
        """
        Processa um documento PDF e extrai texto usando OCR.

        Args:
            pdf_path (str): O caminho para o arquivo PDF a ser processado.

        Returns:
            str: O texto extraído do documento PDF.
        """
        ocr = self.ocr_processor.extract_text_from_pdf_paddle(pdf_path)
        return ocr

if __name__ == "__main__":
    document_processor = DocumentProcessor()

    file_path = "files/teste_.pdf"
    ocr = document_processor.process_document(file_path)
    print(ocr)
    </code></pre>

    <h3>requirements.txt</h3>
    <p>Este arquivo lista todas as bibliotecas necessárias para o projeto, com suas versões específicas.</p>
    <pre><code class="plaintext">numpy==1.26.4
</code></pre>

    <h2>Subpasta: files</h2>

    <h3>Arquivo: files/config</h3>
    <p>Este arquivo contém as credenciais de acesso AWS necessárias para autenticação em serviços da AWS.</p>
    <pre><code class="json">{
  "aws_access_key_id": "SUA_ACCESS_KEY_ID",
  "aws_secret_access_key": "SUA_SECRET_ACCESS_KEY",
  "aws_region": "us-east-1"
}
</code></pre>

    <h3>Arquivo: files/teste_.pdf</h3>
    <p>Contém um texto em PDF: Testando a extração do OCR</p>

    <h2>Subpasta: utils</h2>

    <h3>Arquivo: utils/ocr_extraction.py</h3>
    <p>Este arquivo contém a classe OCRProcessor, que fornece métodos para extrair texto de documentos PDF usando OCR e AWS Rekognition.</p>
    <p>As funcionalidades principais são:</p>
    <ul>
        <li>Extrair texto de um documento PDF usando PaddleOCR.</li>
        <li>Extrair texto de uma imagem usando AWS Rekognition.</li>
    </ul>
    <pre><code class="python">from paddleocr import PaddleOCR
import boto3
import json

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def load_aws_credentials(file_path):
    """
    Carrega as credenciais AWS do arquivo de configuração.

    Args:
        file_path (str): O caminho para o arquivo de configuração.

    Returns:
        dict: Um dicionário contendo as credenciais AWS.
    """
    with open(file_path, 'r') as config_file:
        config_data = json.load(config_file)
    return config_data

class OCRProcessor:
    def __init__(self):
        pass

    def extract_text_from_pdf_paddle(self, pdf_path):
        """
        Extrai texto de um documento PDF usando PaddleOCR.

        Args:
            pdf_path (str): O caminho para o arquivo PDF.

        Returns:
            str: O texto extraído do documento PDF.
        """
        result = ocr.ocr(pdf_path, cls=True)

        text = ''
        for line in result:
            for word in line:
                text += word[1][0] + ' '
            text += '\n'
        return text

    def extract_text_from_image_aws(self, image_path):
        """
        Extrai texto de uma imagem usando AWS Rekognition.

        Args:
            image_path (str): O caminho para a imagem.

        Returns:
            str: O texto extraído da imagem.
        """
        aws_config = load_aws_credentials('aws_config.json')
        aws_access_key_id = aws_config['aws_access_key_id']
        aws_secret_access_key = aws_config['aws_secret_access_key']
        aws_region = aws_config['aws_region']

        client = boto3.client('rekognition', region_name=aws_region, aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key)

        with open(image_path, 'rb') as image_file:
            image_bytes = image_file.read()

        response = client.detect_text(Image={'Bytes': image_bytes})

        detected_text = ''
        for text_detection in response['TextDetections']:
            detected_text += text_detection['DetectedText'] + ' '
        return detected_text.strip()
</code></pre>
</body>
</html>
