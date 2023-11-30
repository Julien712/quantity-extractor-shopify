import yaml

# Chemin vers votre fichier YAML
chemin_fichier = "quantity.yml"

with open(chemin_fichier, 'r') as fichier:
    # Lire chaque document YAML un par un
    for document_yaml in fichier:
        # Charger le document YAML
        contenu_yaml = yaml.safe_load(document_yaml)

        # Extraire la valeur de "initialQuantity"
        initial_quantity = contenu_yaml["initialQuantity"]

        # Imprimer la valeur extraite
        print(f"{initial_quantity}")

