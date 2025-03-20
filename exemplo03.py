import re 

texto = "O número do telefone do Raphael é (123) 456-7890"
padrao = r'\(\{3}\) \d{3}-\d{4}'
# Padrão para encontrar numeros de telefone no formato (XXX) XXX-XXXX

resultado = re.search(padrao, texto)

if resultado:
    numero_telefone = resultado.group()
    print("Numero de telefone encontrado: ", numero_telefone)
else:
    print("Numero de telefone não encontrado.")