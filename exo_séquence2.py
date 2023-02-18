D = {'a' : False , 'b' : True , 'c' : None}
D['d'] = True
print(D)

pokemon = {'Bulbizarre' : [70, 7] , 'Herbizarre' : [100, 13] , 'Abo' : [200,7]}
L =[]
for i in pokemon.keys() :
   L.append(i)
   print(L)

p = {'Bulbizarre' : [70, 7] , 'Herbizarre' : [100, 13] , 'Abo' : [200,7]}
p['Herbizarre'][1]= 20
print(p)

def fonction():
	pokemon = {'Bulbizarre': [70, 8], 'Herbizarre': [100, 13], 'Abo': [200, 7]}
	a = 0
	for i in pokemon.values() :
		if i[1] > a :
			a = i[1]
	return a
print(fonction())