"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 67
local_carro = 99

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

# range correto (antes e depois do radar)
dentro_do_range = (LOCAL_1 - RADAR_RANGE) <= local_carro <= (LOCAL_1 + RADAR_RANGE)

# acima de 10% da velocidade
acima_limite = velocidade > (RADAR_1 * 1.1)

if dentro_do_range and acima_limite:
    print("Veículo multado")
elif acima_limite:
    print("Acima do limite")