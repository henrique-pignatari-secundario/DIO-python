capacidade_atual, aumento_percentual = map(int, input().split())

aumento_decimal = 1 + aumento_percentual/100

nova_capacidade = int(capacidade_atual * aumento_decimal)

print(nova_capacidade)