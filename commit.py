import os

def arborescense_structure(arborescense_analyse_donee):
    # Définir la structure du projet
    arborescense_structure = {
        "data": ["raw", "cleaned"],
        "notebooks": ["main_notebook.ipynb"],
        "makefile":[],
        "model":[],
        "scripts": [],
        "reports": ["figures", "summary"],
        "config": [],
    }

    try:
        # Créer le répertoire principal du projet
        os.makedirs(arborescense_analyse_donee)

        # Parcourir les dossiers et sous-dossiers pour créer la structure
        for folder, subfolders in arborescense_structure.items():
            folder_path = os.path.join(arborescense_analyse_donee, folder)
            os.makedirs(folder_path)
            for subfolder in subfolders:
                os.makedirs(os.path.join(folder_path, subfolder))

        print("Arborescence du projet créée avec succès.")
    except Exception as e:
        print(f"Une erreur est survenue lors de la création du projet : {e}")

if __name__ == "__main__":
    project_name = "Projet_Analyse_De_Donnees"
    arborescense_structure(arborescense_analyse_donee)