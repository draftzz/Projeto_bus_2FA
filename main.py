import time
import os
import shutil

def mover_pastas():
    origem = r"\\spct-prod-saopaulo.scania.com\spctdatalog$\ES_Log\Reports"  # Caminho da pasta no servidor
    destino = os.path.join(os.path.expanduser("~"), "Desktop", "destino")  # Pasta na Área de Trabalho

    # Verificar se a pasta de origem existe
    if not os.path.exists(origem):
        print("A pasta no servidor não pode ser acessada.")
        return

    # Listar apenas pastas dentro do servidor
    pastas = [os.path.join(origem, f) for f in os.listdir(origem) if os.path.isdir(os.path.join(origem, f))]

    # Verificar se há pastas disponíveis
    if not pastas:
        print("Nenhuma pasta encontrada no servidor.")
        return

    # Ordenar as pastas pela data de criação (mais recente primeiro)
    pastas_ordenadas = sorted(pastas, key=os.path.getctime, reverse=True)

    # quantidade de pastas movidas
    quantidade = 10
    pastas_para_mover = pastas_ordenadas[:quantidade]

    # Criar a pasta de destino se não existir
    if not os.path.exists(destino):
        os.makedirs(destino)

    # Copiar as pastas mais recentes para o destino
    for pasta in pastas_para_mover:
        nome_pasta = os.path.basename(pasta)
        destino_pasta = os.path.join(destino, nome_pasta)

        # Verificar se a pasta já existe no destino
        if os.path.exists(destino_pasta):
            print(f"❌ Não foi possível mover '{nome_pasta}' porque já existe em '{destino}'.")
        else:
            print(f"📦 Copiando '{nome_pasta}' para '{destino_pasta}'...")
            shutil.copytree(pasta, destino_pasta)
            print(f"✅ Pasta '{nome_pasta}' copiada com sucesso!")

    print("🚀 Transferência concluída!\n")

# Loop para rodar o script a cada 30 minutos
while True:
    mover_pastas()
    print("⏳ Aguardando 4 horas para a próxima execução...\n")
    time.sleep(14400)  
