from termcolor import colored, cprint #On importe la librairie termcolor pour la question n°6


#################
#PARTIE FONCTION#
#################

################################

# Question 1 

## Il permet de vérifier si l'indice est valide; L'indice étant l'entier n-1 vu qu'il commence à partir de 0. Il retournera True ou False.

def indice_valide(plateau,indice):
	if 0 <= indice <= (plateau["n"])-1:
		return True
	else:
		return False


################################

# Question 2

## Selon le booléen retourné par indice_valide, case_valide retournera un booléen True or False si une des valeurs i ou j ne correspond pas à l'intervalle entre 0 et n

def case_valide(plateau, i, j): #i est la ligne, j est la colonne
	if indice_valide(plateau, i) == False or indice_valide(plateau, j) == False: 
		return False
	return True

################################

# Question 3 

## get_case vérifie si la case est valide en réutilisant la fonction case_valide à travers un assert donnant une erreur spécifique et simple à comprendre.

def get_case(plateau, i, j):
	n=plateau["n"]
	assert case_valide(plateau, i, j), "La case est invalide"
	return plateau["cases"][n* i+ j] #n*i+j correspond à l'indice de la case correspondant aux coordonees (i,j)(i les lignes, j la colonne)

################################

# Question 4 

## Verifie si les coordonnees et la valeur sont valides, puis affecte la valeur à la case du tableau "cases" à l'indice correspondant

def set_case(plateau, i, j, val):
	n=plateau["n"]
	assert case_valide(plateau, i, j), "La case est invalide"
	assert val ==0 or val ==1 or val ==2, "La valeur est invalide!"
	plateau["cases"][n* i+ j]=val
	return plateau["cases"]

################################

# Question 5 

## Apres avoir verifie si le format de tableau choisi est correct, le tableau est crée

def creer_plateau(n):
	assert n ==4 or n ==6 or n ==8, "Tableau pas reglementaire"
	i=0
	plateau={"n":n, "cases":[]}
	while i < n*n:
		if i == (n/2*n+n/2)-n-1 or i== (n/2*n+n/2):   #affecte 2 à la case sur laquelle les coordonnees sont identiques (meme ligne et meme colonne), la formule donnant l'indice de cette position servira de repere pour les suivantes
			plateau["cases"].append(2)
		elif i==(n/2*n)+(n/2)-1 or i==(n/2*n)+(n/2)-n:
			plateau["cases"].append(1)
		else:
			plateau["cases"].append(0)
		i+=1
	return plateau

################################

# Question 6 

## Fonction 1 pour transformer le tableau du plateau en tableau de tableau de taille n pour séparer les lignes et permettre un changement de pattern au niveau des couleurs.

def tabtab(tab,n):
	i=0
	tabtab=[]
	j=0
	a=0
	while i<n:
		a+=n
		tabtab.append([])
		while j<a:
			tabtab[i].append(tab[j])
			j+=1
		i+=1
	return tabtab

## Fonction 2 pour que les cases aient plus d'espaces, selon la valeur de x, les lignes de cases vides (qui servent à donner de l'épaisseur aux cases) s'alterneront de manière différente (bleu-violet ou violet-bleu)

def remplir_case(n,x):
	tab=[]
	i=0
	while i<n:
		tab.append(0)
		i+=1
	i=0
	i=0
	print(' ',end='')
	if x==0:
		while i<len(tab):
			if i%2==0:
				tab[i]=colored('       ', 'magenta', 'on_magenta' ) #la case du tableau prend les couleurs venant de la libraire termcolor. Nous insérons des espaces vides pour la mise en page de l'affichage
				print(tab[i], end='')

			elif i%2!=0:
				tab[i]=colored('       ', 'blue', 'on_blue' )
				print(tab[i], end='')
			i+=1
		print()
	elif x==1:
		while i<len(tab):
			if i%2!=0:
				tab[i]=colored('       ', 'magenta', 'on_magenta' )
				print(tab[i], end='')

			elif i%2==0:
				tab[i]=colored('       ', 'blue', 'on_blue' )
				print(tab[i], end='')
			i+=1
		print()

## Fonction 3 (Principale) pour afficher le plateau (On y trouve les chiffres et lettres pour représenter les lignes et colonnes respectivement)
	
def afficher_plateau(plateau):
	tab=plateau["cases"]
	n=plateau["n"]
	tab=tabtab(tab,n)   #le tableau case est divisé en tableaux correspondants aux lignes
	undeuxtrois=1    #cette valeur correspond au chiffre s'affichant horizontalement
	while undeuxtrois<n+1:
		print('   ',undeuxtrois,' ',end='')
		undeuxtrois+=1
	print()
	abc="abcdefghi"  #les lettres qui s'affichent verticalement sont stockées dans ce string
	j=0
	while j<len(tab):
		i=0
		if j%2!=0: #en fonction de la parité de l'indice de la ligne, x prend 1 ou 0, et le jeu de couleurs sera alterné sur les cases de remplissages
			a=i+1
			x=1
		else:
			a=i              #les couleurs d'une case dépend de sa valeur et de son indice mais pour les lignes d'indices impaires (deuxième, quatrième ligne,etc) cette logique est inversées
			x=0              #la valeur a permet d'effectuer ce changement sans repercussion sur le déroulement de la boucle à la ligne 150
		remplir_case(n,x)
		print(abc[j], end='')	
		while i<len(tab[j]):
			if a%2==0 and tab[j][i]==0:
				tab[j][i]=colored('       ', 'magenta', 'on_magenta' )
				print(tab[j][i], end='')

			elif a%2!=0 and tab[j][i]==0:
				tab[j][i]=colored('       ', 'blue', 'on_blue' )
				print(tab[j][i], end='')

			elif a%2==0 and tab[j][i]==1:
				tab[j][i]=colored('  ###  ', 'grey', 'on_magenta')
				print(tab[j][i], end='')

			elif a%2!=0 and tab[j][i]==1:
				tab[j][i]=colored('  ###  ', 'grey', 'on_blue')
				print(tab[j][i], end='')

			elif a%2==0 and tab[j][i]==2:
				tab[j][i]=colored('  ###  ', 'white', 'on_magenta')
				print(tab[j][i], end='')

			elif a%2!=0 and tab[j][i]==2:
				tab[j][i]=colored('  ###  ', 'white', 'on_blue')
				print(tab[j][i], end='')

			a+=1
			i+=1
		print()
		remplir_case(n,x) #On remet une ligne de cases vides pour qu'il y ait de l'épaisseur des deux côtés
		j+=1


################################

#############
#PARTIE TEST#
#############

# Fonctions principales de test 

# Nous nous servons de séries de test pour chaque format de plateau (4, 6 et 8) qui vérifient
# le fonctionnement de la fonction avec "assert"

#*****************************

### Test Question 1

def test_indice_valide():
    p = creer_plateau(4) #Plateau format 4
    assert indice_valide(p,0)==True #Doit retourner True
    assert indice_valide(p,3)==True #Doit retourner True
    assert indice_valide(p,-1)==False #Doit retourner False car valeur négative
    assert indice_valide(p,4)==False  #Doit retourner False car valeur au-delà des indices
    p = creer_plateau(6) #Plateau format 6
    assert indice_valide(p,4)==True #Doit retourner True
    assert indice_valide(p,5)==True #Doit retourner True
    assert indice_valide(p,6)==False #Doit retourner False car au-delà des indices
    p = creer_plateau(8) #Plateau format 8
    assert indice_valide(p,7)==True #Doit retourner True
    assert indice_valide(p,8)==False #Doit retourner False car plateau format 8 va de 0 à 7

test_indice_valide()

#*****************************

### Test Question 2

def test_case_valide():
	p = creer_plateau(4) # Plateau format 4
	assert case_valide(p,0,1)==True #Doit retourner True car la case est valide
	assert case_valide(p,1,2)==True #Doit retourner True car la case est valide
	assert case_valide(p,-1,2)==False #Doit retourner False car -1 est une valeur négative
	p = creer_plateau(6) # Plateau format 6
	assert case_valide(p,4,1)==True #Doit retourner True car la case est valide
	assert case_valide(p,5,5)==True #Doit retourner True car la case est valide
	assert case_valide(p,6,8)==False #Doit retourner False car les indices sortent du plateau
	p = creer_plateau(8) # Plateau format 8
	assert case_valide(p,7,3)==True #Doit retourner True car la case est valide
	assert case_valide(p,7,7)==True #Doit retourner True car la case est valide
	assert case_valide(p,6,8)==False #Doit retourner False car 8 est en dehors des indices du plateau

test_case_valide()

#*****************************

### Test Question 3

#Les mauvaises utilisations sont mis en assert à travers un commentaire, il suffit d'enlever le commentaire (#) pour vérifier

def test_get_case(): 
	p= creer_plateau(4) # Plateau format 4
	assert get_case(p,0,1)==0 #Fonctionne, la valeur de la case est de 0
	assert get_case(p,1,2)==1 #La valeur de la case est de 1
	#assert get_case(p,-1,2) #Ne marche pas car -1 est en dehors des indices
	p = creer_plateau(6) # Plateau format 6
	assert get_case(p,4,1)==0 #La valeur de la case est de 0
	assert get_case(p,3,2)==1 #La valeur de la case est de 1
	#assert get_case(p,6,8)  #Ne marche pas car 8 est en dehors des indices
	p = creer_plateau(8) # Plateau format 8
	assert get_case(p,7,7)==0 #La valeur est 0
	#assert not get_case(p,6,10)==0 #Cela ne marche pas car
	assert get_case(p,4,4)==2 #Le résultat est bon

test_get_case()

#*****************************

### Test Question 4

# Enlever commentaire pour tester les valeurs fausses

def test_set_case():
	p = creer_plateau(4) # Plateau format 4
	assert set_case(p,0,1,2)==[0, 2, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0] #Les valeurs sont bonnes
	#assert set_case(p,-1,2,1) #Faux car valeur négative (-1)
	p = creer_plateau(6) # Plateau format 6
	#assert set_case(p,4,1,8) #Faux car valeur en dehors de l'indice du plateau
	assert set_case(p,5,5,1)==[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1] #Les valeurs sont bonnes
	#assert set_case(p,6,8,2) #Faux car valeur en dehors de l'indice du plateau
	p = creer_plateau(8) # Plateau format 8
	#assert set_case(p,7,3,3) #Faux car 3 n'est pas une valeur possible, elle est gérée par une erreur d'assertion
	#assert set_case(p,7,7,-1) #Faux car -1 n'est pas une valeur possible, elle est gérée par l'erreur d'assertion
	assert set_case(p,6,7,0)==[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #Les valeurs sont bonnes

test_set_case()

#*****************************

### Test Question 5

# Enlever commentaire pour tester les valeurs fausses

def test_creer_plateau():
	#assert creer_plateau(1) #ce plateau ne peut pas être créé car 1 n'est pas réglementaire
	assert creer_plateau(4)=={'n': 4, 'cases': [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0]}
	assert creer_plateau(6)=={'n': 6, 'cases': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
	assert creer_plateau(8)=={'n': 8, 'cases': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

test_creer_plateau()


#*****************************

### Test Question 6

# Enlever commentaire pour tester les valeurs fausses

def test_afficher_plateau():
	p=creer_plateau(4)
	afficher_plateau(p) # Affiche plateau format 4
	p=creer_plateau(6)
	afficher_plateau(p) # Affiche plateau format 6
	p=creer_plateau(8)
	afficher_plateau(p) # Affiche plateau format 8
	#p=creer_plateau(1) # Le tableau sera considere comme non reglementaire, donc il ne pourra pas afficher un plateau d'un autre format à moins de le faire soi-même



test_afficher_plateau()


#****************************

# Print d'essai

#print(indice_valide(plateau,3))
#print(case_valide(plateau, 3, 3))
#print(get_case(plateau,6,2))
#print(set_case(plateau, 1, 0, 2)) #Le dictionnaire est un objet unique donc le résultat se repercute sur les autres programmes
#print(plateau["cases"])
#afficher_plateau(plateau)