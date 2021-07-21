import pandas as pd


# J'importe les données  
territories = pd.read_csv('data/territories.csv')
relations = pd.read_csv('data/territory_parents.csv')


# Je garde que les colonnes qui m'interessent 
colonnes_territories = ['id','code','name', 'kind']
colonnes_relations = ['child_id', 'parent_id']

territories = territories[colonnes_territories]
relations = relations[colonnes_relations]


# JEe crée un filtre pour recuperer que les territoires departement
filtre_depa = territories["kind"] == "FRDEPA"
departements = territories[filtre_depa]


# Je renomme l'id en parent_id et je modifie les autres entete pour pas d'ambiguite
mapping = {departements.columns[0]:'parent_id',departements.columns[1]:'code_depa',departements.columns[2]:'name_depa',departements.columns[3]:'kind'}
departements = departements.rename(columns=mapping)

############################################################################

#Je récupère le département choisit par l'user avec l'ID
code_depa_user_choice = input('Veuillez reinsegner le numero du departement: ') 


# Je recupère la ligne avec les infos du departement
departement_choice = departements.loc[departements['code_depa'] == code_depa_user_choice] 
departement_parent_id = departement_choice['parent_id']

departement_name = departement_choice['name_depa']

# Je récupère la liste des ID enfants pour cet ID parent
departements_enfants = relations.loc[relations['parent_id'].isin(departement_parent_id)] 

# Je récupère les sous territoires en filtrant par ID les territoires
child_id_to_check = departements_enfants['child_id']
child_check_territories = territories.loc[territories['id'].isin(child_id_to_check)]

print('') # Pour un retour à la ligne
print('Voici les territoires enfants du departement ' + departement_name + ':')

# boucle pour parcourir le df et afficher les premiers 10 resultats
for i in range(len(child_check_territories.index)): 
	print("-"+child_check_territories.iloc[i]['name'])


############################################################################ 












