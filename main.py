
print("=============================")
print("GERADOR DE LINK PARA WHATSAPP")
print("=============================")

numero = int(input("Digite seu numero de celular com DD: "))
mensagem = str(input("Digite uma mensagem: "))

mensagemFinal = mensagem.replace(" ", "%20") #subtitui os caracteres do primeiro parametro para o do segundo parametro

linkFinal = print(f"O link para o seu número é: \nhttps://api.whatsapp.com/send?phone=55{numero}&text={mensagemFinal}" )

print(linkFinal)