#verificar e-mail conforme o que é pedido:
email = input().strip()

if email.startswith("@") or email.endswith("@"): #se e-mail começar ou terminar com "@" é falso
    print("E-mail inválido") #exibe ao usuário que é inválida a tentativa
elif " " in email: #se e-mail tiver algum espaço entre os carcateres da strinf é falso
    print("E-mail inválido") #exibe ao usuário que é invalida a tentaiva
elif "@" not in email: #se o "@" não estiver contido no e-mail como esperado, é falso
    print("E-mail inválido") #exibe ao usuário que é inválida a tentativa
elif email.endswith("@gmail.com") or email.endswith("@outlook.com"): # se o e-mail terminar com os dominios solicitador
    #é verdadeira a condição
    print("E-mail válido") #exibe ao usuário que a condição é valida
else: #se qualquer uma das condicionais anteriores não forem atendidas
    print("E-mail inválido") #exibe que a condição é invalida