from experta import *

#software methodology list (sm = software methodology)
sm_list = []   
#Software_Methodology_characteristics  
sm_char = []
sm_map = {}
s_sm_map = {}

def preprocess():
	global sm_list,sm_char,sm_map,s_sm_map
	#ouvrire le fichier et lire les données
	sm = open("Software_Methodology.txt")
	sm_t = sm.read()
	dsm_list = sm_t.split("\n")
	sm.close()
	for m in sm_list:
		if(m==""):
			continue
		sm_s_file = open("Software_Methodology_Characteristics/" + m + ".txt")
		sm_s_data = sm_s_file.read()
		sm_list = sm_s_data.split("\n")
		sm_char.append(sm_list)
		sm_map[str(sm_list)] = m
		sm_s_file.close()


def identify_sm(*arguments):
    #liste des caractéres des methotologies 
	char_list = [] 
	for char in arguments:
		char_list.append(char)
	# Handle key error
	return sm_map[str(sm_list)]

def if_not_matched(m):
		print("")
		id_m = m
		print("")
		print("La méthodologie de développement logiciel que vous deviez choisir pour gerer votre projet de développement logiciel est : %s\n" %(id_m))

class Greetings(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print("")
		print("Bonjour ! je m'appelle Ben Ghozzi Chayma je suis là pour vous aider à choisir la meilleur méthodologie de développement logiciel pour votre projet .\n")
		print("Ce système expert permet de choisir la bonne la méthodologie de développement logiciel à utiliser pour un projet spécifique.\n")
		print("C'est pourquoi il est préférable d'analyser chaque scénario de projet par rapport à un ensemble de questions suivantes :")
		print("")
		yield Fact(action="find_sm")
	
#defifnition de base des regeles 
	@Rule(Fact(action='find_sm'), NOT(Fact(projetsimple=W())),salience = 1)
	def char_0(self):
		self.declare(Fact(projetsimple=input("Est-ce que le projet est simple? : ")))

	@Rule(Fact(action='find_sm'), NOT(Fact(projetcomplique=W())),salience = 1)
	def char_1(self):
		self.declare(Fact(projetcomplique=input("Est-ce que le projet est milieu de gamme ou compliqué? : ")))

	@Rule(Fact(action='find_sm'), NOT(Fact(projetcomplexe=W())),salience = 1)
	def char_2(self):
		self.declare(Fact(projetcomplexe=input("Est-ce que le projet est complexes? : ")))

	@Rule(Fact(action='find_sm'), NOT(Fact(projetchaotique=W())),salience = 1)
	def char_3(self):
		self.declare(Fact(projetchaotique=input("Est-ce que le projet est chaotique? : ")))

	@Rule(Fact(action='find_sm'), NOT(Fact(defintion=W())),salience = 1)
	def char_4(self):
		self.declare(Fact(definition=input("Le projet nécessite-t-il un périmètre clairement défini ? : ")))

	@Rule(Fact(action='find_sm'), NOT(Fact(clients=W())),salience = 1)
	def char_5(self):
		self.declare(Fact(clients=input("Le produit final nécessite-t-il une rétroaction constante des clients ? : ")))

	@Rule(Fact(action='find_sm'), NOT(Fact(produit=W())),salience = 1)
	def char_6(self):
		self.declare(Fact(produit=input("La livraison rapide du produit est-elle plus importante que la qualité du produit ? : ")))

	@Rule(Fact(action='find_sm'), NOT(Fact(equipe=W())),salience = 1)
	def char_7(self):
		self.declare(Fact(equipe=input("L'équipe de développement est-elle suffisamment compétente pour travailler dans des environnements en évolution et disposée à s'adapter ? : ")))

	@Rule(Fact(action='find_sm'),Fact(projetsimple="oui"),OR(Fact(projetcomplique="non"),Fact(projetcomplexe="non")),Fact(projetchaotique="non"),OR(Fact(defintion="oui"),Fact(clients="non"),
	Fact(produit="non")),OR(Fact(equipe="non"),NOT(Fact(clrShowed=W()))))
	def sm_0(self):
		self.declare(Fact(m="Waterfall(Cascade)"))
		self.declare(Fact(clrShowed="yes"))

	@Rule(Fact(action='find_sm'),Fact(projetsimple="non"),OR(Fact(projetcomplique="oui"),Fact(projetcomplexe="oui")),Fact(projetchaotique="non"),OR(Fact(defintion="non"),Fact(clients="oui"),
	Fact(produit="oui")),OR(Fact(equipe="oui"),NOT(Fact(clrShowed=W()))))
	def sm_1(self):
		self.declare(Fact(m="Scrum"))
		self.declare(Fact(clrShowed="yes"))

	@Rule(Fact(action='find_sm'),Fact(projetsimple="non"),OR(Fact(projetcomplique="oui"),Fact(projetcomplexe="non")),Fact(projetchaotique="non"),OR(Fact(defintion="non"),Fact(clients="oui"),
	Fact(produit="oui")),OR(Fact(equipe="oui"),NOT(Fact(clrShowed=W()))))
	def sm_2(self):
		self.declare(Fact(m="Kanban"))
		self.declare(Fact(clrShowed="yes"))

	@Rule(Fact(action='find_sm'),Fact(projetsimple="non"),OR(Fact(projetcomplique="non"),Fact(projetcomplexe="oui")),Fact(projetchaotique="oui"),OR(Fact(defintion="non"),Fact(clients="oui"),
	Fact(produit="oui")),OR(Fact(equipe="oui"),NOT(Fact(clrShowed=W()))))
	def sm_3(self):
		self.declare(Fact(m="Programmation extrême (XP)"))
		self.declare(Fact(clrShowed="yes"))

	@Rule(Fact(action='find_sm'),Fact(projetsimple="non"),OR(Fact(projetcomplique="non"),Fact(projetcomplexe="non")),Fact(projetchaotique="non"),OR(Fact(defintion="non"),Fact(clients="non"),
	Fact(produit="non")),OR(Fact(equipe="non"),NOT(Fact(clrShowed=W()))))
	def sm_4(self):
		self.declare(Fact(m="Méthodologie logicielle non détectée"))

	@Rule(Fact(action='find_sm'),Fact(m=MATCH.m),salience = -998)
	def m(self, m):
		print("")
		id_m = m 
		print("")
	
		print("La méthodologie de développement logiciel que vous deviez choisir est :\n %s\n" %(id_m))


	@Rule(Fact(action='find_sm'),
		  Fact(projetsimple=MATCH.projetsimple),
		  Fact(projetcomplique=MATCH.projetcomplique),
		  Fact(projetcomplexe=MATCH.projetcomplexe),
		  Fact(projetchaotique=MATCH.projetchaotique),
		  Fact(defintion=MATCH.defintion),
		  Fact(clients=MATCH.clients),
		  Fact(equipe=MATCH.equipe),NOT(Fact(m=MATCH.m)),salience = -999)


	def not_matched(self,projetsimple, projetcomplique, projetcomplexe, projetchaotique, defintion, clients, equipe):
		print("\n Je n'ai pas trouvé de méthodologie de développement logiciel correspondant aux caractéristiques exacts donnés.")
		lis = [projetsimple, projetcomplique, projetcomplexe, projetchaotique, defintion, clients, equipe]
		
		max_count = 0
		max_sm = ""
		for key,val in sm_map.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "oui"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_sm = val
		if_not_matched(max_sm)

if __name__ == "__main__":
	preprocess()
	engine = Greetings()
	while(1):
		engine.reset()  # Prepare the engine for the execution.
		engine.run()  # Run it!
		print("Voulez-vous choisir d'autres méthodologie ??")
		if input() == "non":
			exit()
		#print(engine.facts)
