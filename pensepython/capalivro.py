"""Problema
Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um
desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos
para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?
"""

preco_capa = 24.95

desconto = 0.6 * preco_capa

frete = 3 + 0.75*59

preco_atacado = desconto * 60 + frete

print(preco_atacado)