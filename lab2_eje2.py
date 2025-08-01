import numpy as np
import matplotlib.pyplot as plt

objetivo = 50
retardo_percepcion = 15  
retardo_ajuste = 10      
tiempo_total = 200       
dt = 1                   
tiempo = np.arange(0, tiempo_total + dt, dt)

kernel_size = retardo_percepcion
erlang_kernel = np.exp(-np.linspace(0, 5, kernel_size))
erlang_kernel /= erlang_kernel.sum()

stock_real = [0]
stock_percibido = [0]
flujo = []

for t in range(1, len(tiempo)):
    percibido = np.convolve(stock_real, erlang_kernel, mode='full')[:len(stock_real)]
    stock_percibido.append(percibido[-1])

    flujo_ajuste = (objetivo - stock_percibido[-1]) / retardo_ajuste
    nuevo_stock = stock_real[-1] + flujo_ajuste * dt

    stock_real.append(nuevo_stock)
    flujo.append(flujo_ajuste)

plt.figure(figsize=(10, 6))
plt.plot(tiempo, stock_real, label='Stock Real')
plt.plot(tiempo, stock_percibido, label='Stock Percibido', linestyle='--')
plt.axhline(objetivo, color='gray', linestyle=':', label='Objetivo')

plt.title('Ejercicio 2 - Retroalimentación con Retardo de Percepción')
plt.xlabel('Días')
plt.ylabel('Unidades')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
