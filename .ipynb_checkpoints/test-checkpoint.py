import pandas as pd
from glob import glob

stock_files = sorted(glob('data/territor*.csv'))
pd.concat((pd.read_csv(file).assign(filename = file)
	for file in stock_files), ignore_index = True)


# Je recupere,via le URL, le ID du kind = FRDEPA dans "territories.csv"

# Je recupere les terriroires enfants dans "territory_parents.csv", cad les child_id qui ont parent_id = id_FRDEPA 

# J'obtiens les Cantons(FRCANT) + EPCI (FREPCI) + Communes (FRCOMM) => Je ne veux pas visualiser les communes ici

# Pour chaque FREPCI, je recupere les terrioites enfants, cad les child_id ont parent_id = iD_FREPCI

# J'obtiens  les Communes (FRCOMM)

