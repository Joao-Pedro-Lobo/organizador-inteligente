from pathlib import Path
from config import PASTAS_ORIGEM
from organizador import OrganizadorArquivos

def main():
    print("=== ORGANIZADOR DE ARQUIVOS ===")
    print("Iniciando organização...\n")
    
    organizador = OrganizadorArquivos()
    
    for pasta in PASTAS_ORIGEM:
        if pasta.exists():
            print(f"Organizando: {pasta}")
            organizador.organizar_pasta(pasta)
        else:
            print(f"Pasta não encontrada: {pasta}")
    
    print("\nOrganização concluída!")

if __name__ == "__main__":
    main()