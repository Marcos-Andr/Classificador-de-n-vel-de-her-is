# Classificador de nível de heróis

#Utilizei python por estar fazendo o curso em conjunto com a faculdade.
Nome = input("Digite o nome do herói: ")
XP = int(input("Digite o XP do herói:"))
Nivel = ""
if XP <= 1000: 
    Nivel = "Ferro"
elif XP <= 2000:
    Nivel = "Bronze"
elif XP <= 5000:
    Nivel = "Prata"
elif XP <= 7000:
    Nivel = "Ouro"
elif XP <= 8000:
    Nivel = "Platina"
elif XP <= 9000:
    Nivel = "Ascendente"
elif XP <= 10000:
    Nivel = "Imortal"  
else:
    Nivel = "Radiante"

print("\n===== Informações do Herói =====")
print(f"Nome: {Nome}")
print(f"Nível: {Nivel}")