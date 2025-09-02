import schedule
import time
from datetime import datetime
from organizador import OrganizadorArquivos
from config import PASTAS_ORIGEM

def tarefa_organizacao():
    """Tarefa que será executada periodicamente"""
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Executando organização automática...")
    
    organizador = OrganizadorArquivos()
    
    for pasta in PASTAS_ORIGEM:
        if pasta.exists():
            print(f"Organizando: {pasta}")
            organizador.organizar_pasta(pasta)
        else:
            print(f"Pasta não encontrada: {pasta}")
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Organização concluída!")

def agendar_tarefas():
    """Configura o agendamento das tarefas"""
    
    schedule.clear()
    
    schedule.every().month.at("08:00").do(tarefa_organizacao)
    
    print("Agendador iniciado. Pressione Ctrl+C para parar.")
    print("Agendamentos configurados:")
    for job in schedule.jobs:
        print(f"→ {job}")
    
    # Manter o agendador rodando
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    try:
        agendar_tarefas()
    except KeyboardInterrupt:
        print("\nAgendador interrompido pelo usuário.")