# interface_grafica.py
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
from organizador import OrganizadorArquivos
from config import PASTAS_ORIGEM, PASTA_DESTINO, CATEGORIAS
import threading

class InterfaceOrganizador:
    def __init__(self, root):
        self.root = root
        self.root.title("Organizador de Arquivos Automático")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Variáveis de controle
        self.pastas_origem = list(PASTAS_ORIGEM)
        self.pasta_destino = PASTA_DESTINO
        self.executando = False
        
        self.criar_interface()
        
    def criar_interface(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar expansão
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Título
        titulo = ttk.Label(main_frame, text="Organizador de Arquivos", 
                          font=("Arial", 16, "bold"))
        titulo.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Seção de pastas de origem
        ttk.Label(main_frame, text="Pastas para Organizar:").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        self.lista_origem = tk.Listbox(main_frame, height=4)
        self.lista_origem.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        # Adicionar scrollbar para a lista
        scrollbar_origem = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.lista_origem.yview)
        scrollbar_origem.grid(row=2, column=2, sticky=(tk.N, tk.S), pady=5)
        self.lista_origem.configure(yscrollcommand=scrollbar_origem.set)
        
        # Frame para botões de origem
        frame_botoes_origem = ttk.Frame(main_frame)
        frame_botoes_origem.grid(row=3, column=0, columnspan=2, pady=5)
        
        ttk.Button(frame_botoes_origem, text="Adicionar Pasta", 
                  command=self.adicionar_pasta).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botoes_origem, text="Remover Selecionada", 
                  command=self.remover_pasta).pack(side=tk.LEFT, padx=5)
        
        # Pasta de destino
        ttk.Label(main_frame, text="Pasta de Destino:").grid(row=4, column=0, sticky=tk.W, pady=5)
        
        self.var_destino = tk.StringVar(value=str(self.pasta_destino))
        entry_destino = ttk.Entry(main_frame, textvariable=self.var_destino, state='readonly')
        entry_destino.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(main_frame, text="Alterar Destino", 
                  command=self.alterar_destino).grid(row=5, column=1, padx=5)
        
        # Opções de organização
        ttk.Label(main_frame, text="Opções:", font=("Arial", 10, "bold")).grid(row=6, column=0, sticky=tk.W, pady=10)
        
        self.var_sobreescrever = tk.BooleanVar(value=False)
        ttk.Checkbutton(main_frame, text="Sobreescrever arquivos duplicados", 
                       variable=self.var_sobreescrever).grid(row=7, column=0, sticky=tk.W, pady=2)
        
        self.var_backup = tk.BooleanVar(value=True)
        ttk.Checkbutton(main_frame, text="Fazer backup antes de organizar", 
                       variable=self.var_backup).grid(row=8, column=0, sticky=tk.W, pady=2)
        
        # Barra de progresso
        ttk.Label(main_frame, text="Progresso:").grid(row=9, column=0, sticky=tk.W, pady=10)
        
        self.progresso = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progresso.grid(row=10, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Botões de ação
        frame_botoes_acao = ttk.Frame(main_frame)
        frame_botoes_acao.grid(row=11, column=0, columnspan=2, pady=20)
        
        ttk.Button(frame_botoes_acao, text="Organizar Agora", 
                  command=self.iniciar_organizacao).pack(side=tk.LEFT, padx=10)
        ttk.Button(frame_botoes_acao, text="Visualizar Prévia", 
                  command=self.visualizar_previa).pack(side=tk.LEFT, padx=10)
        ttk.Button(frame_botoes_acao, text="Sair", 
                  command=self.root.quit).pack(side=tk.LEFT, padx=10)
        
        # Área de log
        ttk.Label(main_frame, text="Log de Execução:").grid(row=12, column=0, sticky=tk.W, pady=10)
        
        self.log_text = tk.Text(main_frame, height=8, width=60)
        self.log_text.grid(row=13, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        scrollbar_log = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.log_text.yview)
        scrollbar_log.grid(row=13, column=2, sticky=(tk.N, tk.S), pady=5)
        self.log_text.configure(yscrollcommand=scrollbar_log.set)
        
        # Configurar expansão dos elementos
        main_frame.rowconfigure(2, weight=1)
        main_frame.rowconfigure(13, weight=1)
        
        # Carregar pastas iniciais
        self.atualizar_lista_origem()
        
    def adicionar_pasta(self):
        pasta = filedialog.askdirectory(title="Selecionar Pasta para Organizar")
        if pasta:
            path_pasta = Path(pasta)
            if path_pasta not in self.pastas_origem:
                self.pastas_origem.append(path_pasta)
                self.atualizar_lista_origem()
    
    def remover_pasta(self):
        selecionados = self.lista_origem.curselection()
        if selecionados:
            indice = selecionados[0]
            self.pastas_origem.pop(indice)
            self.atualizar_lista_origem()
    
    def alterar_destino(self):
        pasta = filedialog.askdirectory(title="Selecionar Pasta de Destino")
        if pasta:
            self.pasta_destino = Path(pasta)
            self.var_destino.set(str(self.pasta_destino))
    
    def atualizar_lista_origem(self):
        self.lista_origem.delete(0, tk.END)
        for pasta in self.pastas_origem:
            self.lista_origem.insert(tk.END, str(pasta))
    
    def log(self, mensagem):
        self.log_text.insert(tk.END, mensagem + "\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def visualizar_previa(self):
        self.log("=== PRÉVIA DA ORGANIZAÇÃO ===")
        for pasta in self.pastas_origem:
            if pasta.exists():
                self.log(f"\nAnalisando: {pasta}")
                for item in pasta.iterdir():
                    if item.is_file():
                        # Simular a organização
                        extensao = item.suffix.lower()
                        categoria = "Outros"
                        for cat, exts in CATEGORIAS.items():
                            if extensao in exts:
                                categoria = cat
                                break
                        self.log(f"  {item.name} → {categoria}/")
            else:
                self.log(f"Pasta não encontrada: {pasta}")
        self.log("\nPrévia concluída. Esta é apenas uma simulação.")
    
    def iniciar_organizacao(self):
        if self.executando:
            return
            
        self.executando = True
        self.progresso.start()
        self.log("=== INICIANDO ORGANIZAÇÃO ===")
        
        # Executar em uma thread separada para não travar a interface
        thread = threading.Thread(target=self.executar_organizacao)
        thread.daemon = True
        thread.start()
    
    def executar_organizacao(self):
        try:
            organizador = OrganizadorArquivos()
            organizador.sobreescrever = self.var_sobreescrever.get()
            
            for pasta in self.pastas_origem:
                if pasta.exists():
                    self.log(f"Organizando: {pasta}")
                    organizador.organizar_pasta(pasta)
                else:
                    self.log(f"Pasta não encontrada: {pasta}")
            
            self.log("Organização concluída com sucesso!")
            messagebox.showinfo("Sucesso", "Organização concluída com sucesso!")
            
        except Exception as e:
            self.log(f"Erro durante a organização: {e}")
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
        
        finally:
            self.executando = False
            self.progresso.stop()
            self.root.after(100, lambda: self.root.update_idletasks())

def main():
    root = tk.Tk()
    app = InterfaceOrganizador(root)
    root.mainloop()

if __name__ == "__main__":
    main()