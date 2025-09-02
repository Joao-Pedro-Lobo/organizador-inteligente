# 🗂️ Organizador de Arquivos Inteligente

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Concluído-success)

Um sistema inteligente de automação em Python que organiza automaticamente arquivos em seu computador por tipo, data ou categoria, com interface gráfica amigável e funcionalidades avançadas.

## ✨ Funcionalidades

- **📂 Organização Automática**: Classifica arquivos por tipo (imagens, documentos, vídeos, etc.)
- **🖼️ Interface Gráfica Intuitiva**: Interface amigável desenvolvida com Tkinter
- **⚡ Execução em Background**: Processamento em thread separada para não travar a interface
- **🔍 Prévia de Organização**: Visualização do resultado antes de executar
- **🔄 Controle de Duplicatas**: Opção para sobrescrever ou renomear arquivos duplicados
- **⏰ Agendamento Automático**: Organização programada com a biblioteca `schedule`
- **📊 Log de Execução**: Registro detalhado de todas as operações realizadas

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+** - Linguagem principal
- **Tkinter** - Interface gráfica
- **Pathlib** - Manipulação de caminhos de forma orientada a objetos
- **Schedule** - Agendamento de tarefas
- **Shutil** - Operações de arquivos e diretórios

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/organizador-inteligente.git
```

## 🎯 Próximas Melhorias
- Backup automático antes da organização
- Suporte a plugins e extensões
- Modo nuvem (Google Drive, Dropbox)
- Reconhecimento inteligente de conteúdo de arquivos
- Relatórios estatísticos em PDF
