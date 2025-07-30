import matplotlib.pyplot as plt

tiempo_total = 50
dt = 1
retardo = 5
entrada_base = 10
entrada_cambio = 20
cambio_dia = 25

tiempo = []
stock = []
salida = []
entrada = []

s = 0

for t in range(tiempo_total + 1):
    e = entrada_base if t < cambio_dia else entrada_cambio
    out = s / retardo
    s = s + dt * (e - out)

    tiempo.append(t)
    entrada.append(e)
    salida.append(out)
    stock.append(s)

equilibrio_1 = entrada_base * retardo
equilibrio_2 = entrada_cambio * retardo

plt.figure(figsize=(10, 6))
plt.plot(tiempo, stock, label='Stock (nivel acumulado)')
plt.plot(tiempo, salida, label='Salida (flujo)')
plt.plot(tiempo, entrada, label='Entrada (flujo)', linestyle='--')

plt.axhline(equilibrio_1, color='gray', linestyle='--', linewidth=1, label='Equilibrio 1 (10*5)')
plt.axhline(equilibrio_2, color='gray', linestyle='--', linewidth=1, label='Equilibrio 2 (20*5)')
plt.axvline(cambio_dia, color='red', linestyle=':', label='Cambio en entrada (día 25)')

plt.xlabel('Días')
plt.ylabel('Unidades')

plt.title('Simulación de Retardo de Primer Orden')

plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
