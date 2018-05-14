# from vendeurs import *
# from clients import *
# from utilisateurs import *
from tables import *
from articles import * 


def main():

	# name=input("give the vendors name: ")
	# adress=input("the vendors address: ")
	# tel= int(input("The vendors numTel: "))
	# email = input("and the vendors email: ")
	# ajouter_vendeur(name, adress, tel, email)

	# ajouter_article("Fer", "electique", 300.0);
	# ajouter_article("Phone", "nokia", 3000);
	supprimer_article("Fer")
	afficher_table("Articles")

if __name__ == '__main__':
	main()