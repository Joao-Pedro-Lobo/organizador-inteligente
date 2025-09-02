import os
import shutil
from pathlib import Path
from datetime import datetime
from config import CATEGORIAS, PASTA_DESTINO

class OrganizadorArquivos:
    def __init__(self, sobreescrever=False):
        self.contador = 0
        self.arquivos_duplicados = 0
        self.sobreescrever = sobreescrever  # Controla se arquivos duplicados devem ser sobrescritos
        
    def organizar_pasta(self, pasta_origem):
        """Organiza todos os arquivos de uma pasta"""
        if not pasta_origem.exists():
            print(f"Pasta {pasta_origem} não existe!")
            return
            
        for item in pasta_origem.iterdir():
            if item.is_file():
                self._processar_arquivo(item)
            elif item.is_dir() and item != PASTA_DESTINO:
                # Organizar subpastas também
                self.organizar_pasta(item)
                
        print(f"Organização completa! {self.contador} arquivos processados, "
              f"{self.arquivos_duplicados} duplicados ignorados.")
    
    def _processar_arquivo(self, arquivo):
        """Processa um arquivo individual"""
        # Determinar categoria
        categoria = self._determinar_categoria(arquivo)
        
        if not categoria:
            # Manter arquivos não categorizados na pasta "Outros"
            categoria = "Outros"
        
        # Criar pasta de destino se não existir
        pasta_destino = PASTA_DESTINO / categoria
        pasta_destino.mkdir(parents=True, exist_ok=True)
        
        # Gerar novo nome para evitar duplicatas
        novo_nome = self._gerar_nome_unico(arquivo, pasta_destino)
        
        if novo_nome:
            # Mover arquivo
            shutil.move(str(arquivo), str(pasta_destino / novo_nome))
            self.contador += 1
            print(f"Organizado: {arquivo.name} -> {categoria}/{novo_nome}")
        else:
            self.arquivos_duplicados += 1
            print(f"Duplicado ignorado: {arquivo.name}")
    
    def _determinar_categoria(self, arquivo):
        """Determina a categoria do arquivo baseado na extensão"""
        extensao = arquivo.suffix.lower()
        
        for categoria, extensoes in CATEGORIAS.items():
            if extensao in extensoes:
                return categoria
                
        return None
            
    def _gerar_nome_unico(self, arquivo, pasta_destino):
        """Gera um nome único para o arquivo para evitar sobreescrever"""
        destino = pasta_destino / arquivo.name
        
        if not destino.exists() or self.sobreescrever:
            return arquivo.name
        
        # Se já existe e não queremos sobreescrever, adicionar timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_sem_ext = arquivo.stem
        novo_nome = f"{nome_sem_ext}_{timestamp}{arquivo.suffix}"
        
        if not (pasta_destino / novo_nome).exists():
            return novo_nome
        
        # Se ainda existe, não mover (arquivo duplicado)
        return None