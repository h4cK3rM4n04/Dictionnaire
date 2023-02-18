mon_dico = {"nom": "Durand", "prenom": "Christophe", "date de naissance": "29/02/1981"}
#print(mon_dico["nom"])

lolo = {"nom": "Durand", "prenom": "Christophe", "date de naissance": "29/02/1981"}
lolo['lieu naissance'] = "Bonneville"
#print(lolo)

mlml = {"poire": 3, "pomme": 4, "orange": 2}
del mlml["pomme"]
#print(mlml)

mes_fruits = {"poire": 3, "pomme": 4, "orange": 2}
mes_fruits.pop("pomme")
#print(mes_fruits)

#sdsd = {"poire": 3, "pomme": 4, "orange": 2}
#sdsd["pomme"] = mesFruits["pomme"] - 1
#print(sdsd)

g = {"poire": 3, "pomme": 4, "orange": 2}
a= g.pop("pomme")
g["mangue"] = a
#print(g)

i = {"poire": 3, "pomme": 4, "orange": 2}
#.keys parcourt les clées de la variable i
#for fruit in i.keys():
	#print(fruit)

o = {"poire": 3, "pomme": 4, "orange": 2}
#normalement ça affiche que les valeurs....
#for qte in o.values():
	#print(o)

gh = {"poire": 3, "pomme": 0, "orange": 2, "kiwi" : 1, "mangue" : 12}
a = 0
for i in gh.keys():
	#print(gh[i])
	if gh[i] > 2 :
            a = a + gh[i]
            # somme des valeurs des clefs - valeur de la première clef
            #print(a)

dictionnaire = {'liste': 56, 'Bibo': 45,'Nombre': 32}
#print(dictionnaire["liste"])

nombre_de_roues = {"voiture": 2,\
					 "vélo": 5,\
					  "tricycle": 45}

for i in nombre_de_roues.items():
    print(i)