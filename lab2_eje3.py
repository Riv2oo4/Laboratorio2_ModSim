
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

S0 = 990   
I0 = 10    
R0 = 0     
N = S0 + I0 + R0

beta = 0.3  
mu = 0.1    
R_0 = beta / mu

def modelo_sir(t, y):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - mu * I
    dRdt = mu * I
    return [dSdt, dIdt, dRdt]

t_eval = np.linspace(0, 100, 101)
sol_sin_vacuna = solve_ivp(modelo_sir, [0, 100], [S0, I0, R0], t_eval=t_eval)

sol_con_vacuna = solve_ivp(modelo_sir, [0, 30], [S0, I0, R0], t_eval=np.linspace(0, 30, 31))
S_vac = sol_con_vacuna.y[0, -1] * 0.5
I_vac = sol_con_vacuna.y[1, -1]
R_vac = sol_con_vacuna.y[2, -1] + sol_con_vacuna.y[0, -1] * 0.5
sol_post_vac = solve_ivp(modelo_sir, [30, 100], [S_vac, I_vac, R_vac], t_eval=np.linspace(30, 100, 71))

t_total = np.concatenate([sol_con_vacuna.t, sol_post_vac.t])
S_total = np.concatenate([sol_con_vacuna.y[0], sol_post_vac.y[0]])
I_total = np.concatenate([sol_con_vacuna.y[1], sol_post_vac.y[1]])
R_total = np.concatenate([sol_con_vacuna.y[2], sol_post_vac.y[2]])

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(sol_sin_vacuna.t, sol_sin_vacuna.y[0], label='Susceptibles (sin vacunación)', linestyle='--')
ax.plot(sol_sin_vacuna.t, sol_sin_vacuna.y[1], label='Infectados (sin vacunación)', linestyle='--')
ax.plot(sol_sin_vacuna.t, sol_sin_vacuna.y[2], label='Recuperados (sin vacunación)', linestyle='--')

ax.plot(t_total, S_total, label='Susceptibles (con vacunación)')
ax.plot(t_total, I_total, label='Infectados (con vacunación)')
ax.plot(t_total, R_total, label='Recuperados (con vacunación)')

ax.axvline(30, color='red', linestyle=':', label='Vacunación (día 30)')
ax.set_title('Modelo SIR con y sin vacunación')
ax.set_xlabel('Días')
ax.set_ylabel('Población')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.show()
