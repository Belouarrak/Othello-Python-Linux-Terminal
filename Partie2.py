from Partie1 import creer_plateau, afficher_plateau, case_valide, get_case, set_case


#################
#PARTIE FONCTION#
#################

################################

# Question 7

## Retourne Joueur 1 si il s'agit du Joueur 2 et vice-versa

def pion_adverse(joueur):
	assert joueur == 1 or joueur == 2, "Ce n'est ni le joueur 1 et ni le joueur 2" # Lève une erreur avec description si la variable sort de 1 ou de 2
	if joueur == 1: 
		return 2 # On retourne 2 si 1
	else:
		return 1 # On retourne 1 si 2

################################

# Question 8

## Vérifie toutes les prises possibles de direction et continue à chercher si la case est le pion opposé 

def prise_possible_direction(p, i, j, vertical, horizontal, joueur):
	if case_valide(p,i+vertical,j+horizontal)==False: # Si la case n'existe pas dans le plateau, on retourne False
		return False
	if get_case(p,i+vertical,j+horizontal)==0 or get_case(p,i+vertical,j+horizontal)==joueur: # Si la case est 0 ou la case est celle du joueur en paramètre, on retourne False 
		return False
	vert=vertical # On rajoute une variable qui permettera une addition de la direction verticale
	horiz=horizontal # On rajoute une variable qui permettera une addition horizontale
	while case_valide(p,i+vertical+vert,j+horizontal+horiz): # Tant qu'on ne sort pas du plateau, on continue de vérifier
		if get_case(p,i+vertical+vert,j+horizontal+horiz)==joueur: # On additionne les directions pour aller dans une nouvelle ligne et/ou nouvelle colonne. Si on retombe sur nos pas avec un pion du même type, on retourne True
			return True # On retourne True si on retombe sur nos pas avec un pion de même couleur
		elif get_case(p,i+vertical+vert,j+horizontal+horiz)==0: # On utilise la même stratégie mais avec le besoin de vérifier si la case entre les deux pions de la même couleur ne soit pas vide (0)
			return False # On retourne False si le pion est vide
		else:
			vertical+=vert #On ré-additionne pour aller dans une nouvelle ligne et/ou colonne 
			horizontal+=horiz 
	return False

################################

# Question 9

## On valide si le mouvement est réglementaire. C'est à dire qu'on appelle la fonction prise_possible_direction pour chaque direction afin de savoir si le pion peut être posé.

def mouvement_valide(plateau, i, j, joueur):
	if get_case(plateau,i,j)==0: # On regarde immédiatement si la case est vide
		vertical=-1 # On initialise à -1 pour tout balayer
		while vertical<=1:  
			horizontal=-1 # Même chose pour cette variable
			while horizontal<=1: 
				if prise_possible_direction(plateau,i,j,vertical,horizontal,joueur)==True: # Nous regardons la prise possible de direction dans toutes les directions possibles
					return True # On retourne True si le mouvement est valide
				horizontal+=1 
			vertical+=1
	return False # On retourne False si le mouvement n'est pas valide

################################

# Question 10

## On confirme la prise de direction et on change les cases jusqu'à atteindre le deuxième pion de même couleur à l'autre bout

def mouvement_direction(plateau, i, j, vertical, horizontal, joueur):
	if prise_possible_direction(plateau, i, j, vertical, horizontal, joueur)==True: # On confirme que la prise de direction est possible
		vert=vertical+i # Vertical s'additionne avec la valeur i (de colonne)
		horiz=horizontal+j # Horizontal s'additionne avec la valeur j (de ligne)
		while get_case(plateau, vert, horiz)==pion_adverse(joueur): # Tant que la case est celle de l'adversaire...
			set_case(plateau, vert, horiz, joueur) # ...On change la valeur pour celle du joueur
			vert+=vertical
			horiz+=horizontal # On additionne pour arriver à la prochaine ligne et/ou colonne

################################

# Question 11

## On insère le pion et on appelle les fonctions pour retourner les pions entre le pion inséré et l'autre pion de même couleur
	
def mouvement(plateau,i,j,joueur):
	if mouvement_valide(plateau,i,j,joueur)==True: # On appelle la fonction pour savoir si le mouvement est possible
		set_case(plateau,i,j,joueur) # On insère le pion si le mouvement est possible
		vertical=-1  
		while vertical<=1:
			horizontal=-1
			while horizontal<=1:
				mouvement_direction(plateau,i,j,vertical,horizontal,joueur) # On recherche dans toutes les directions possibles si on peut manger des pions
				horizontal+=1
			vertical+=1

################################

# Question 12

## On regarde dans chaque case si un mouvement est possible

def joueur_peut_jouer(plateau, joueur):
	n=plateau["n"] # Pour la visibilité on affecte le format du plateau à la variable n
	i=0 # on se sert de i et j pour pouvoir se servir de la fonction mouvement valide
	while i<n:
		j=0
		while j<n:
			if mouvement_valide(plateau,i,j,joueur)==True: # On regarde si le mouvement est réglementaire dans chaque case possible
				return True # On retourne True s'il reste une possibilité de jouer
			j+=1
		i+=1
	return False # On retourne False s'il n'y a plus de moyen de jouer

################################

# Question 13

## Si aucun des joueurs ne peut jouer, il s'agit d'une fin de partie

def fin_de_partie(plateau):
	return joueur_peut_jouer(plateau,1)==False and joueur_peut_jouer(plateau,2)==False #Si aucun des deux ne peut jouer, la partie est terminée

################################

# Question 14

## On affecte les points aux deux joueurs compte tenu du plateau

def gagnant(plateau):
	i=0
	joueur1=0
	joueur2=0
	tab=plateau["cases"] #On affecte le tableau à la variable tab pour la visibilité
	while i < len(tab): # 
		if tab[i]==1: # Si l'intérieur de la case possède un 2
			joueur1+=1 # On ajoute un 1 au Joueur 1
		elif tab[i]==2: # Si l'intérieur de la case possède un 2
			joueur2+=1 # On ajoute un 2 au Joueur 2
		i+=1
	if joueur2>joueur1:
		return 2
	elif joueur1>joueur2:
		return 1
	else : 
		return 0


################################

#############
#PARTIE TEST#
#############

# Fonctions principales de test 

# Nous nous servons de séries de test pour chaque format de plateau (4, 6 et 8) qui vérifient
# le fonctionnement de la fonction avec "assert"

#*****************************

### Test Question 7

def test_pion_adverse():
	assert pion_adverse(1)==2 #Doit retourner True car le joueur est le joueur 1 et l'adversaire est le joueur 2#
	assert pion_adverse(2)==1 #Doit retourner True car le joueur est le joueur 2 et l'adversaire est le joueur 1#
	assert not pion_adverse(2)==2 #Doit retourner False car le joueur est le joueur 2 et l'adversaire est le joueur 1#
	assert not pion_adverse(1)==0 #Doit retourner False car le joueur est le joueur 1 et l'adversaire est le joueur 2#
	
test_pion_adverse()

#*****************************

### Test Question 8

def test_prise_possible_direction():
	
	p = creer_plateau(4)
	print("PLATEAU 4 POUR FONCTION PRISE_POSSIBLE_DIRECTION")
	afficher_plateau(p)
	assert prise_possible_direction(p,2,3,0,-1,1)==True # True car le pion noir (2,3) peut manger un pion blanc (2,2)
	assert prise_possible_direction(p,1,3,0,-1,1)==False # False car le pion noir (1,3) fera face à un autre pion noir (1,2)
	
	p = creer_plateau(6)
	print("PLATEAU 6 POUR FONCTION PRISE_POSSIBLE_DIRECTION")
	afficher_plateau(p)
	assert prise_possible_direction(p,2,1,1,0,1)==False # False car la direction du pion (2,1) mène vers une case vide
	assert prise_possible_direction(p,1,2,1,0,1)==True # True car le pion noir (1,2) peut manger un pion blanc (2,2)
	
	p = creer_plateau(8)
	print("PLATEAU 8 POUR FONCTION PRISE_POSSIBLE_DIRECTION")
	afficher_plateau(p)
	assert prise_possible_direction(p,3,2,0,1,1)==True # True car le pion noir (3,2) peut manger un pion blanc (3,3)
	assert prise_possible_direction(p,2,4,1,0,2)==True # True car le pion blanc (2,4) peut manger un pion blanc (3,4)

test_prise_possible_direction()

#*****************************

### Test Question 9

def test_mouvement_valide():
	
	p=creer_plateau(4)
	print("PLATEAU 4 POUR FONCTION MOUVEMENT_VALIDE")
	afficher_plateau(p)
	assert mouvement_valide(p,0,1,1)==True # True car un pion noir peut être placé en (0,1) pour retourner un pion blanc
	assert mouvement_valide(p,0,0,1)==False # False car un pion noir ne peut pas être placé en (0,0) pour retourner un pion blanc
	
	p=creer_plateau(6)
	print("PLATEAU 6 POUR FONCTION MOUVEMENT_VALIDE")
	afficher_plateau(p)
	assert mouvement_valide(p,1,3,1)==False # False car un pion noir ne peut pas être placé en (0,0) pour retourner un pion blanc
	assert mouvement_valide(p,3,1,2)==True # True car un pion blanc peut être placé en (0,1) pour retourner un pion noir
	
	p=creer_plateau(8)
	print("PLATEAU 8 POUR FONCTION MOUVEMENT_VALIDE")
	afficher_plateau(p)
	assert mouvement_valide(p,5,4,2)==False # False car un pion blanc ne peut pas être placé en (5,4) pour retourner un pion noir
	assert mouvement_valide(p,5,4,1)==True # True car un pion noir peut être placé en (5,4) pour retourner un pion blanc

test_mouvement_valide()

#*****************************

### Test Question 10

def test_mouvement_direction():
	
	p=creer_plateau(4)
	mouvement_direction(p,0,2,1,0,2) # On mange le pion blanc placé en (1,2)
	print("PLATEAU 4 POUR FONCTION MOUVEMENT_DIRECTION")
	afficher_plateau(p)
	assert get_case(p,2,1)==1 # La valeur de la case (2,1) est 1
	assert not get_case(p,0,0)==2 # La valeur de la case (2,2) est 0
	
	p=creer_plateau(6)
	mouvement_direction(p,4,2,-1,0,2) # On mange le pion noir placé en (3,2)
	print("PLATEAU 6 POUR FONCTION MOUVEMENT_DIRECTION")
	afficher_plateau(p)
	assert get_case(p,3,2)==2 # La valeur de la case (3,2) est 2
	assert not get_case(p,3,2)==1 # La valeur de la case (3,2) est 2
	
	p=creer_plateau(8)
	mouvement_direction(p,4,2,0,1,2) # On mange le pion blanc placé en (4,3)
	print("PLATEAU 8 POUR FONCTION MOUVEMENT_DIRECTION")
	afficher_plateau(p)
	assert get_case(p,4,3)==2 # La valeur de la case (4,3) est 2
	assert not get_case(p,4,3)==1 # La valeur de la case (4,3) est 2

test_mouvement_direction()

#*****************************

### Test Question 11

def test_mouvement():
	
	p=creer_plateau(4)
	print("PLATEAU 4 POUR FONCTION MOUVEMENT")
	mouvement(p,3,2,1) # On mange le pion en (2,2) et on place un pion (3,2)
	afficher_plateau(p)
	assert get_case(p,2,2)==1 # Le pion mangé est bien noir
	assert not get_case(p,2,2)==2 # Le pion mangé est noir donc cela est faux
	
	p=creer_plateau(6)
	print("PLATEAU 6 POUR FONCTION MOUVEMENT") 
	mouvement(p,4,2,2) # On mange le pion en (3,2) et on place un pion (4,2)
	afficher_plateau(p)
	assert get_case(p,3,2)==2 # Le pion mangé est bien blanc
	assert not get_case(p,4,2)==1 # Le pion mangé est blanc donc cela est faux
	
	p=creer_plateau(8)
	print("PLATEAU 8 POUR FONCTION MOUVEMENT")
	mouvement(p,2,3,1) # On mange le pion en (3,3) et on place un pion (2,3)
	afficher_plateau(p)
	assert get_case(p,2,3)==1 # Le pion qu'on a inséré est bien noir
	assert not get_case(p,3,3)==2 # Le pion qu'on a retourné n'est plus noir mais blanc

test_mouvement()

#*****************************

### Test Question 12

def test_joueur_peut_jouer():
	
	p=creer_plateau(4)	
	p["cases"]=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
	print("PLATEAU 4 POUR FONCTION JOUEUR_PEUT_JOUER")
	afficher_plateau(p)
	assert joueur_peut_jouer(p,1)==False # Le joueur ne peut pas jouer car toutes les cases sont remplies
	assert joueur_peut_jouer(p,2)==False # Le joueur ne peut pas jouer car toutes les cases sont remplies
	
	p=creer_plateau(6)
	print("PLATEAU 6 POUR FONCTION JOUEUR_PEUT_JOUER")
	afficher_plateau(p)
	assert joueur_peut_jouer(p,1) # Le joueur 1 peut encore jouer
	assert joueur_peut_jouer(p,2) # Le joueur 2 peut encore jouer
	
	p=creer_plateau(8)
	set_case(p,3,3,1) # On transforme les pions blancs en pions noirs
	set_case(p,4,4,1) 
	print("PLATEAU 8 POUR FONCTION JOUEUR_PEUT_JOUER")
	afficher_plateau(p)
	assert joueur_peut_jouer(p,2)==False # Le joueur ne peut pas jouer car les pions sont tous d'une seule et même couleur
	assert joueur_peut_jouer(p,1)==False # Le joueur ne peut pas jouer car les pions sont tous d'une seule et même couleur

test_joueur_peut_jouer()

#*****************************

### Test Question 13

def test_fin_de_partie():
	
	p=creer_plateau(4)
	print("PLATEAU 4 POUR FONCTION FIN_DE_PARTIE")
	p["cases"]=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
	afficher_plateau(p)
	assert fin_de_partie(p)==True # Prouve que la partie se termine car plus d'actions possible
	
	p=creer_plateau(6)
	print("PLATEAU 6 POUR FONCTION FIN_DE_PARTIE")
	afficher_plateau(p)
	assert fin_de_partie(p)==False # Prouve que l'un des joueurs peut toujours jouer

	p=creer_plateau(8)
	print("PLATEAU 8 POUR FONCTION FIN_DE_PARTIE")
	set_case(p,4,4,1)
	set_case(p,3,3,1) # On transforme les pions blancs en pions noirs
	afficher_plateau(p)
	assert fin_de_partie(p)==True # Les joueurs ne peuvent pas jouer, donc la partie se termine

test_fin_de_partie()

#*****************************

### Test Question 14

def test_gagnant():
	
	p=creer_plateau(4)
	p["cases"]=[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
	print("PLATEAU 4 POUR FONCTION GAGNANT")
	afficher_plateau(p)
	assert gagnant(p)==2 # Retourne True car le joueur 2 a plus de points que le joueur 1
	assert (gagnant(p)==1)==False # Retourne False car le joueur 2 a plus de points que le joueur 1

	p=creer_plateau(6)
	print("PLATEAU 6 POUR FONCTION GAGNANT")
	afficher_plateau(p)	
	assert (gagnant(p)==0)==True # Retourne True car il s'agit d'une égalité
	assert (gagnant(p)==2)==False # Retourne False car il s'agit d'une égalité

	p=creer_plateau(8)
	print("PLATEAU 8 POUR FONCTION GAGNANT")
	set_case(p,4,4,1)
	set_case(p,3,3,1) # On remplace les pions blancs par des pions noirs
	afficher_plateau(p)
	assert gagnant(p)==1 # Retourne True car le joueur 1 a plus de points que le joueur 2
	assert (gagnant(p)==2)==False # Retourne False car le joueur 1 a plus de points que le joueur 2

test_gagnant()

#*****************************