texto = "Nossa aula Manipulando String."

print(texto[0:20:2])
print(texto)
print(len(texto))
print(texto.count("a"))
print(texto.count("a", 5, 30))
print(texto.find("aula"))
print(texto.find("Python"))
print('String' in texto)
print("Vanderson" in texto)

novo_txt = texto.replace("manipulando", "trabalhando com")
print(novo_txt)

print(texto.startswith("Nossa"))
print(texto.startswith("aula"))
print(texto.endswith("aula"))
print(texto.endswith("."))

print(texto.lower())
print(texto.upper())
print(texto.capitalize())
print(texto.title())
print(texto.swapcase())

nome = str(input('Digite o seu nome: '))
print(f'Ola, {nome}!')
print(f'Ola, {nome.strip()}!')
print(nome.rstrip())
print(nome.lstrip())

palavras = texto.split()
for palavra in palavras:
    print(palavras)