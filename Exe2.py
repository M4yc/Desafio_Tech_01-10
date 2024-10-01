
frase = str(input("Informe a frase: "))

num = frase.lower().count('a')

if num == 0:
    print("A letra 'a' não está na string")
else:
    print(f"A letra 'a' está na string {num} vezes.")