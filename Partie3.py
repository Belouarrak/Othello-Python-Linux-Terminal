from Partie1 import *
from Partie2 import *
from os import system
import os
import json
from json import dumps, loads


#################
#PARTIE FONCTION#
#################

################################

# Question 15

## Cela permet de créer une variable contenant un dictionnaire avec le joueur et le plateau. 

def creer_partie(n):

	# On appelle la fonction creer_plateau pour la création du plateau, et cette fonction vérifie si la taille est réglementaire.
	partie={"joueur":1,"plateau":creer_plateau(n)} 
	return partie

################################

# Question 16

def saisie_valide(partie, s):
	if s=="m":
		s=s.upper()
	# La fonction vérifie que la saisie est "M"(qui redirige au menu principal), ou bien un mouvement valide sur le plateau
	# Les indices i et j sont ici obtenus grace à la fonction ord()-codeASCIIpremierelettre/chiffre, (ainsi a4 devient 0,3 par exemple)
	if s=="M" or mouvement_valide(partie["plateau"],ord(s[0])-97,ord(s[1])-49,partie["joueur"]):
		return True
	else:
		return False

################################

# Question 17

###FONCTION EFFACER TERMINAL###
def effacer_terminal():
    system('clear')
###FONCTION EFFACER TERMINAL###

def tour_jeu(partie):

	effacer_terminal() # Afin de dégager toute l'information du terminal vers le haut
	afficher_plateau(partie["plateau"]) # Nous affichons le plateau sur le terminal
	print("C'est au joueur ", partie["joueur"]," de jouer.\nSi vous voulez aller dans le menu principal, tapez M." )
	s=str(input("Veuillez entrer une commande.: "))
	if s=="m":
		s=s.upper()

	if saisie_valide(partie,s): 
		if s=="M":
			return False  # False est retourné pour retourner au menu (dans une fonction suivante)
		else:
			i=ord(s[0])-97 # On les affecte à des variables pour une question de visibilité
			j=ord(s[1])-49
			mouvement(partie["plateau"],i,j,partie["joueur"]) # Le mouvement du joueur est effectué sur le plateau
			return True

	else:
		return tour_jeu(partie) # La fonction se répète si aucune des options sont valides

#################################

# Question 18

def saisir_action(partie):

	action=42 # Un nombre sans conséquence
	# Tant que le nombre inséré sort de l'intervalle 0 à 4, on redemande à l'utilisateur de réinsérer sa saisie
	while action!=0 and action!=1 and action!=2 and action!=3 and action!=4: 
		action=int(input("Vous êtes dans le menu principal.\nVeuillez entrer une action.: "))
	return action

#################################

# Question 19

def jouer(partie):

	if fin_de_partie(partie["plateau"]): # Si la partie est terminée, on retourne True, sinon False
		return True
	else:
		return False

#################################

# Question 20

def saisir_taille_plateau(): 

	nombre=0 # Il s'agit d'un nombre sans conséquence
	# Tant que le nombre inséré n'est pas un format réglementaire de plateau, on redemande à l'utilisateur de réinsérer sa saisie
	while nombre!=4 and nombre!=6 and nombre!=8:
		nombre=int(input("Veuillez saisir une taille de plateau réglementaire : "))
	return nombre

#################################

# Question 21

## On se sert des fonctions JSON pour sauvegarder une partie dans un fichier stocké dans le répertoire

def sauvegarder_partie(partie):

	partiecours= dumps(partie) # On stocke la partie dans la variable partiecours
	fichier= open("sauvegarde_partie.json", "w") # On met en place une variable qui ouvre/crée un fichier JSON en écriture
	fichier.write(partiecours) # On stocke la partie dans le fichier
	fichier.close # On ferme le fichier pour empêcher des conflits

#################################

# Question 22

def charger_partie():

	if os.path.exists("sauvegarde_partie.json"): # On regarde si le fichier existe
		fichier = open("sauvegarde_partie.json") # On ouvre le fichier sous la variable "fichier"
		data = fichier.read() # On stocke la partie présente dans le fichier dans la variable data
		fichier.close() # On ferme la variable qui contient le fichier puisque nous avons le contenu dans "data"
		partie=json.loads(data) # On récupère le contenu sous format de dictionnaire et non STR avec la fonction loads 

	else:
		partie=creer_partie(4) # Si le fichier n'existe pas, nous créeons une nouvelle partie sous format 4*4

	return partie

##################################

# Question 23

def game(partie):

# Cette fonction correspond à la partie "ingame" du jeu, elle permet d'insérer les joueurs dans une partie dans laquelle le plateau s'affiche et où ils jouent pour de vrai
# Elle a été séparée de Othello() pour soucis de lisibilté et d'ergonomie 

	ingame=True 
	# La variable "ingame" utilisée tout au long de cette question permet d'indiquer si les joueurs sont face au plateau ou pas, ainsi tant ingame est vraie, la partie continue
	while ingame==True:			
		# Cette boucle constitue le jeu en lui-même
		if joueur_peut_jouer(partie["plateau"],partie["joueur"])==False or tour_jeu(partie)==True: 
		# Si le joueur saisi un mouvement, celui si est effectué et le joueur adverse a la main, et ainsi de suite 
		# Ou bien si le joueur ne peut pas jouer, la main passe à l'autre joueur sans que tour-jeu soit appelé 
			if joueur_peut_jouer(partie["plateau"],partie["joueur"])==False:  
				print("La main passe au joueur adverse.")
			partie["joueur"]=pion_adverse(partie["joueur"])
		# Dans n'importe quel autre cas (fin de partie, ou bien menu principal), on sort du jeu
		else:
			ingame=False

		if jouer(partie):
			afficher_plateau(partie["plateau"])
			print("La partie est terminée !!")
			if gagnant(partie["plateau"])==1:
				print ("Le joueur 1 a gagné la partie !")
			elif gagnant(partie["plateau"])==2:
				print("Le joueur 2 a gagné la partie !")
			elif gagnant(partie["plateau"])==0:
				print("Egalité.")	
			ingame=False

	return ingame

##### Fonction principale

def othello():

	print ("########################################\n############### OTHELLO ################\n########################################")
	partie={}
	action=42

	#################### Menu principal (0) #####################
	while action!=0:
		action=saisir_action(None) 

    #################### Nouvelle partie (1) #####################
		if action==1:
			ingame=True
			partie=creer_partie(saisir_taille_plateau())
			ingame=game(partie)

    #################### Charger une partie (2) ####################
		elif action==2:
			partie=charger_partie()
			if partie==creer_partie(4):
				print("Il n'existe pas de partie sauvegardé.\nUne nouvelle partie en 4*4 a été crée ")
			ingame=True
			print("Une partie a été chargée")
			ingame=game(partie)

	################## Sauvegarder une partie (3) ##################
		elif action==3:
			if partie=={}:
				print("Vous n'avez pas commencé de nouvelle partie! ")
			else:
				sauvegarder_partie(partie)
				print("La partie a été sauvegardé sous le fichier sauvegarde_partie.json! ")

    ################### Reprendre la partie (4) ####################
		elif action==4:
			ingame=True
			if partie=={}:
				print ("Vous n'avez pas commencé de nouvelle partie")
				ingame=0
			ingame=game(partie)


################################

#############
#PARTIE TEST#
#############

# Fonctions principales de test 

# Nous nous servons de séries de test pour chaque format de plateau (4, 6 et 8) qui vérifient
# le fonctionnement de la fonction avec "assert"

#*****************************

### Test Question 15

def test_creer_partie():
	assert creer_partie(4)=={"joueur":1,"plateau":creer_plateau(4)}, "Nous avons dierctement mis le dictionnaire avec la fonction creer_plateau au format 4"
	assert creer_partie(6)=={"joueur":1,"plateau":creer_plateau(6)}, "Nous avons dierctement mis le dictionnaire avec la fonction creer_plateau au format 6"
	assert creer_partie(8)=={"joueur":1,"plateau":creer_plateau(8)}, "Nous avons dierctement mis le dictionnaire avec la fonction creer_plateau au format 8"
	assert not creer_partie(4)=={"joueur":1,"plateau":creer_plateau(6)}, "Nous avons dierctement mis le dictionnaire avec la fonction creer_plateau au format 6, on voit que les n ne correspondent pas"

	assert creer_partie(4)=={"joueur":1,"plateau":{'n': 4, 'cases': [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0]}}, "Nous avons dierctement mis le dictionnaire au format 4"
	assert creer_partie(6)=={"joueur":1,"plateau":{'n': 6, 'cases': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}}, "Nous avons dierctement mis le dictionnaire au format 6"
	assert creer_partie(8)=={"joueur":1,"plateau":{'n': 8, 'cases': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}}, "Nous avons dierctement mis le dictionnaire au format 8"
	
	assert not creer_partie(4)=={"joueur":1,"plateau":{'n': 4, 'cases': [0, 0, 0, 1, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0]}}, "Ici les pions ne correspondent pas"
	assert not creer_partie(4)=={"joueur":2,"plateau":{'n': 4, 'cases': [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0]}}, "Ici les valeurs des joueurs ne correspondent pas"

#*****************************

### Test Question 16

def test_saisie_valide():
	p = creer_partie(4)
	assert saisie_valide(p, "M")==True, "M est conforme"
	assert not saisie_valide(p, "M")==False
	assert saisie_valide(p, "m")==True, "m est convertit en M et est donc conforme"
	assert not saisie_valide(p, "a1")==True, "a1 est un mouvement invalide"

	p = creer_partie(6)
	assert saisie_valide(p, "M")==True, "M est conforme"
	assert not saisie_valide(p, "M")==False
	assert saisie_valide(p, "m")==True, "m est convertit en M et est donc conforme"
	assert not saisie_valide(p, "a1")==True, "a1 est un mouvement invalide"

	p = creer_partie(8)
	assert saisie_valide(p, "M")==True, "M est conforme"
	assert not saisie_valide(p, "M")==False
	assert saisie_valide(p, "m")==True, "m est convertit en M et est donc conforme"
	assert not saisie_valide(p, "a1")==True, "a1 est un mouvement invalide"




#*****************************

### Test Question 17

##############################################################################
def tour_jeu_ver_test(partie, s): # On a crée une version de tour_jeu qui est testable (car on ne voulait rentrer dans le jeu en plein test)

	if s=="m":
		s=s.upper()

	if saisie_valide(partie,s): 
		if s=="M":
			return False  
		else:
			i=ord(s[0])-97 
			j=ord(s[1])-49
			mouvement(partie["plateau"],i,j,partie["joueur"])
			return True

	else:
		return 2 #Pour dire que la fonction se répète
##############################################################################


def test_tour_jeu():
	p = creer_partie(4)
	assert tour_jeu_ver_test(p,"M")==False, "M n'est pas un mouvement(False = menu principal)"
	assert tour_jeu_ver_test(p,"m")==False, "m devient M et n'est pas un mouvement"
	assert tour_jeu_ver_test(p,"a1")==2, "return 2= saisie invalide et la fonction se répete"
	assert tour_jeu_ver_test(p,"a2")==True, "Cette commande correspond à un mouvement valide"

	p = creer_partie(6)
	assert tour_jeu_ver_test(p,"M")==False, "M n'est pas un mouvement(False = menu principal)"
	assert tour_jeu_ver_test(p,"m")==False, "m devient M et n'est pas un mouvement"
	assert tour_jeu_ver_test(p,"a1")==2, "return 2= saisie invalide et la fonction se répete"
	assert tour_jeu_ver_test(p,"b3")==True, "Cette commande correspond à un mouvement valide"

	p = creer_partie(8)
	assert tour_jeu_ver_test(p,"M")==False, "M n'est pas un mouvement(False = menu principal)"
	assert tour_jeu_ver_test(p,"m")==False, "m devient M et n'est pas un mouvement"
	assert tour_jeu_ver_test(p,"a1")==2, "return 2= saisie invalide et la fonction se répete"
	assert tour_jeu_ver_test(p,"c4")==True, "Cette commande correspond à un mouvement valide"



#*****************************

### Test Question 18

##############################################################################
def saisir_action_ver_test(action):											 #
	if action!=0 and action!=1 and action!=2 and action!=3 and action!=4: 	 #
		return False														 #
	else:																	 #
		return True	   #On a crée une version test qui retourne des booléens #
##############################################################################

def test_saisir_action():
	assert saisir_action_ver_test(0)==True, "0 est une action possible"
	assert saisir_action_ver_test(1)==True, "1 est une action possible"
	assert saisir_action_ver_test(2)==True, "2 est une action possible"
	assert saisir_action_ver_test(3)==True, "3 est une action possible"
	assert saisir_action_ver_test(4)==True, "4 est une action possible"

	assert not saisir_action_ver_test(5)==True, "5 est une action impossible"
	assert not saisir_action_ver_test(6)==True, "6 est une action impossible"
	assert not saisir_action_ver_test(7)==True, "7 est une action impossible"
	assert not saisir_action_ver_test(69)==True, "69 est une action impossible"
	assert not saisir_action_ver_test(420)==True, "420 est une action impossible"


#*****************************

### Test Question 19

def test_jouer():
	p = creer_partie(4)
	assert jouer(p) == False, "La partie n'est pas finie"
	p = creer_partie(6)
	assert jouer(p) == False, "La partie n'est pas finie"
	p = creer_partie(8)
	assert jouer(p) == False, "La partie n'est pas finie"

	p = {"joueur":1,"plateau":{'n': 4, 'cases': [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0]}}
	assert jouer(p) == False, "La partie n'est pas finie"

	p = {"joueur":1,"plateau":{'n': 4, 'cases': [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]}}
	assert jouer(p) == True, "La partie est pas finie, toutes les cases sont remplies et aucun des joueurs ne peut jouer"

	p = {"joueur":1,"plateau":{'n': 4, 'cases': [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]}}
	assert jouer(p) == True, "La partie est pas finie, toutes les cases sont remplies et aucun des joueurs ne peut jouer"



#*****************************

### Test Question 20

##############################################################################
def saisir_taille_plateau_ver_test(nombre): 								 #
	 if nombre!=4 and nombre!=6 and nombre!=8:								 #
	 	return False														 #
	 else:																	 #
	 	return True   # On a crée une version test qui retourne des booléens #
##############################################################################

def test_saisir_taille_plateau():
	assert saisir_taille_plateau_ver_test(4)==True, "Taille réglementaire"
	assert saisir_taille_plateau_ver_test(6)==True, "Taille réglementaire"
	assert saisir_taille_plateau_ver_test(8)==True, "Taille réglementaire"

	assert not saisir_taille_plateau_ver_test(0)==True, "0 n'est pas une taille réglementaire"
	assert not saisir_taille_plateau_ver_test(-1)==True, "-1 n'est pas une taille réglementaire"
	assert not saisir_taille_plateau_ver_test(420)==True, "420 n'est pas une taille réglementaire"
	assert not saisir_taille_plateau_ver_test(69)==True, "69 n'est pas une taille réglementaire"
	assert not saisir_taille_plateau_ver_test(1001010101)==True, "1001010101 n'est pas une taille réglementaire"


#*****************************

### Test Question 21

def test_sauvegarder_partie():
	p = creer_partie(4)
	sauvegarder_partie(p)
	fichier= open("sauvegarde_partie.json")
	data = fichier.read()
	assert {"joueur":1,"plateau":{'n': 4, 'cases': [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0]}}==json.loads(data), "La partie sauvegardée correspond à ce dictionnaire"
	assert {"joueur":1,"plateau":{'n': 4, 'cases': [0, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 1, 1]}}!=json.loads(data), "La partie sauvegardée ne correspond pas à ce dictionnaire"

	p = creer_partie(6)
	sauvegarder_partie(p)
	fichier= open("sauvegarde_partie.json")
	data = fichier.read()
	assert json.loads(data)=={"joueur":1,"plateau":{'n': 6, 'cases': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}}, "La partie sauvegardé correspond à ce dictionnaire"
	assert json.loads(data)!={"joueur":1,"plateau":{'n': 6, 'cases': [0, 1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}}, "La partie sauvegardé ne correspond pas à ce dictionnaire"



#*****************************

### Test Question 22

def test_charger_partie():
	p = creer_partie(4)
	sauvegarder_partie(p)
	p2 = charger_partie()
	assert p==p2, "La partie sauvegardée (p) est p2"
	set_case(p["plateau"],0,1,2)
	assert not p==p2, "p a été modifié et ne correspond plus à la partie chargée (p2)"


	p = creer_partie(6)
	sauvegarder_partie(p)
	p2 = charger_partie()
	assert p==p2, "La partie sauvegardée (p) est p2"
	set_case(p["plateau"],0,1,2)
	assert not p==p2, "p a été modifié et ne correspond plus à la partie chargée (p2)"


#*****************************

### Test Question 23

othello()
# Il suffit d'enlever le dièse en commentaire pour pouvoir le tester soi-même




				
if __name__ == "__main__":
	test_creer_partie()
	test_saisie_valide()
	test_tour_jeu()
	test_saisir_action()
	test_jouer()
	test_saisir_taille_plateau()
	test_sauvegarder_partie()
	test_charger_partie()