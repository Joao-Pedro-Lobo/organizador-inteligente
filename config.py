import os
from pathlib import Path

# Configurações do projeto
BASE_DIR = Path(__file__).parent

# Pastas a serem organizadas
PASTAS_ORIGEM = [
    Path.home() / "Desktop",
]

# Destino para arquivos organizados
PASTA_DESTINO = Path.home() / "Arquivos_Organizados"

# Extensões por categoria
CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"],
    "Audios": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programas": [".exe", ".msi", ".deb", ".dmg"],
    "Codigos": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".php"]
}