import re
import unicodedata

def cleaning_text(texto):
    # Remove caracteres especiais e acentos
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
    # Converte para minúsculas
    texto = texto.lower()
    # Remove espaços sobressalentes e quebras de linha
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto