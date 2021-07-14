from threading import Thread
import time

def carro(velocidade, piloto):
    print('teste')
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print('Piloto: {} Km: {} \n'.format(piloto,  trajeto))
        
 

t_carro1 = Thread(target=carro, args=[1, 'Jean'])
t_carro2 = Thread(target=carro, args=[2, 'Marcelo'])

t_carro1.start()
t_carro2.start()
