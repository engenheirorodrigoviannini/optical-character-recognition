from paddleocr import PaddleOCR
import boto3
import json

# Inicializa o objeto PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Carrega as credenciais AWS do arquivo de configuração
def load_aws_credentials(file_path):
    with open(file_path, 'r') as config_file:
        config_data = json.load(config_file)
    return config_data

class OCRProcessor:
    def __init__(self):
        pass

    # Função para extrair texto OCR de um PDF
    def extract_text_from_pdf_paddle(self, pdf_path):
        # Use o método `ocr.ocr()` para extrair texto de uma imagem
        result = ocr.ocr(pdf_path, cls=True)  # Corrigido para usar `pdf_path` diretamente

        # Concatene todas as palavras detectadas em uma única string
        text = ''
        for line in result:
            for word in line:
                text += word[1][0] + ' '  # O índice 0 representa o texto da palavra
            text += '\n'  # Adicione uma nova linha após cada linha de texto
        return text


    # Função para extrair texto de uma imagem usando AWS Rekognition
    def extract_text_from_image_aws(self, image_path):  # Renomeado de `extract_text_from_pdf_aws` para `extract_text_from_image_aws`
        # Carrega as credenciais AWS do arquivo de configuração
        aws_config = load_aws_credentials('aws_config.json')
        aws_access_key_id = aws_config['aws_access_key_id']
        aws_secret_access_key = aws_config['aws_secret_access_key']
        aws_region = aws_config['aws_region']

        # Inicializa o cliente Rekognition
        client = boto3.client('rekognition', region_name=aws_region, aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key)

        # Lê a imagem como bytes
        with open(image_path, 'rb') as image_file:
            image_bytes = image_file.read()

        # Faz a chamada para detectar texto na imagem
        response = client.detect_text(Image={'Bytes': image_bytes})

        # Extrai o texto detectado
        detected_text = ''
        for text_detection in response['TextDetections']:
            detected_text += text_detection['DetectedText'] + ' '
        return detected_text.strip()
