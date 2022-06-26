import time
from threading import Thread

# eu importo a classe Thread da biblioteca threading e com isso a gente pode fazer o multithreading
def carro(velocidade, piloto):
    # onde o carro vai iniciar
    trajeto = 0 # km 0

    # defini até onde o carrinho vai percorrer
    while trajeto <= 100:

        # o trajeto cresce com a velocidade
        trajeto += velocidade
        time.sleep(0.5)
        print(f'Piloto : {piloto} Km: {trajeto} \n')

# Criacao de Threads

# Digamos que o carro1 seja um objeto da classe Thread
thread_carro1 = Thread(target=carro, args=[1, 'Max Verstappen'])
thread_carro2 = Thread(target=carro, args=[2, 'Daniel Ricciardo'])

thread_carro1.start() # inicia o processo do carro1
thread_carro2.start() # inicia o processo do carro2
