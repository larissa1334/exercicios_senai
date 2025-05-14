# Cálculo de Desconto em um Produto.
# • Se o usuário informar que o preço original é 100 e o desconto é
# de 20%, o programa deverá calcular que o valor do desconto é 20
# e, consequentemente, o preço final será 80.
# • Exemplo de fórmula:
# valor_desconto = preco_original * (porcentagem_desconto / 100)
# preco_final = preco_original - valor_descont

nome =(input('nome do produto'))  
preço = float (input('preço do produto'))
porcentagem = float(input('porcentagem de desconto'))
desconto =preço * (porcentagem / 100)
valor_novo = preço - desconto

print (valor_novo)

print (f'n { preço} com {porcentagem}% de desconto custara : R$ {valor_novo} ')