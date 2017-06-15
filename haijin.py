from random import randint

lista1 = ["Ramas", "Hojas", "Ligustrinas", "Plantas","Arboledas"]
lista2 = ["ocres", "amarillas","doradas","marchitas", "secas", "muertas"]

lista3 = ["gracioso", "pantagruelico", "abatido", "sublime", "penoso", "sobrecogedor"]
lista5 = ["verdadero", "oscuro", "ominoso"]
lista4 = ["paisaje", "colorido", "luminoso", "Otoño"]

lista6 = ["invaluable", "irrevocable", "irremplazable"]
lista7 = ["imaginacion", "inspiracion", "sabiduria"]

listaIndice1 = randint(0, len(lista1) - 1)
listaIndice2 = randint(0, len(lista2) - 1)
listaIndice3 = randint(0, len(lista3) - 1)
listaIndice4 = randint(0, len(lista4) - 1)
listaIndice5 = randint(0, len(lista5) - 1)
listaIndice6 = randint(0, len(lista6) - 1)
listaIndice7 = randint(0, len(lista7) - 1)

haiku = lista1[listaIndice1] + " " + lista2[listaIndice2] + ",\n"
haiku = haiku + lista3[listaIndice3] + " " + lista4[listaIndice4] + " " + lista5[listaIndice5] + ",\n"
haiku = haiku + lista6[listaIndice6] + " " + lista7[listaIndice7] + "."

print(haiku)