# Dicionário com os valores de desconto
#lembrando que não são reais de desconto são % de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# Aplique o desconto se o cupom for válido:

valor_desconto10 = 100 * (10/100) #calcula a porcentagem
valor_desconto20 = (20/100) * 200 #calcula porcentagem
#forma de ser feita é:
# valor_descontado20 = 100 * (20/100) da mesma forma como no desconto em 10

if cupom == "DESCONTO10": #se for esse o cupom
  descontado_10 = preco - valor_desconto10 #calculo o preço do produto menos o desconto
  print(f'{descontado_10:.2f}') #exibe ao usuário o valor que deve pagar com desconto
elif cupom == "DESCONTO20": #se for esse o cupom
  descontado2 = preco - valor_desconto20 #calcula o valor a ser descontado
  #descontado2 = preco - valor_descontado20 * 2 (são *2 dois por ser 20% de desconto que é = 40)
  print(f'{descontado2:.2f}') #exibe ao usuário o valor
elif cupom == "SEM_DESCONTO": #se for esse o cupom
  print(f'{preco:.2f}') #exibe o valor sem nenhum desconto previsto na compra
else:
  print('Esse cupom não existe na nossa loja, tente novamente') #se o usuário errar algo, como por exemplo, colocar um cupom que não existe na loja