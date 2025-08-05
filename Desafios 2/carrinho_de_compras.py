#Crie um sistema de carrinho de compras que permita adicionar produtos e calcular o valor total da compra.

lista_produtos = []
total = 0.0
itens = int(input().strip())

for item in range(itens):
    item = input().strip()
    espaço = item.rfind(" ")

    nome_produto = item[:espaço]
    preco_produto = float(item[espaço + 1:])
    lista_produtos.append((nome_produto, preco_produto))
    total += preco_produto
    
for nome_produto, preco_produto in lista_produtos:
    print(f"{nome_produto}: R${preco_produto:.2f}")
print(f"Total: R${total:.2f}")

