def grand(dico,taille) :
    resultat = []
    for i in dico.keys() :
        if dico[i][0] > taille :
            resultat.append(i)
    resultat.sort()
    return resultat