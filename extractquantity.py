import yaml

# Chemin vers votre fichier YAML d'entrée
chemin_fichier_entree = "quantity.yml"

# Chemin vers votre fichier de sortie
chemin_fichier_sortie = "quantity_sortie.txt"

# Ouvrir le fichier de sortie en mode écriture
with open(chemin_fichier_sortie, 'w') as fichier_sortie:
    # Lire le contenu du fichier YAML d'entrée
    with open(chemin_fichier_entree, 'r') as fichier_entree:
        # Lire chaque document YAML un par un
        for document_yaml in fichier_entree:
            # Charger le document YAML
            contenu_yaml = yaml.safe_load(document_yaml)

            # Extraire la valeur de "initialQuantity"
            initial_quantity = contenu_yaml["initialQuantity"]

            # Écrire la valeur extraite dans le fichier de sortie
            fichier_sortie.write(f"{initial_quantity}\n")
