import os
import json

def scale(val, old_min, old_max, new_min, new_max):
    return new_min + (((val - old_min) * (new_max - new_min)) / (old_max - old_min))

def collect_files(path, accepted = []):
    final_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            ext = os.path.splitext(file)[1][1:].lower()
            if ext in accepted or len(accepted) == 0:
                final_list.append(os.path.join(root, file))
    return final_list

def write_json(path : str, content : dict, indent : int = 4) -> None:
    """
    Donner un chemin de destination et du contenu et enregistrer au format json.
    
    Si le dossier n'existe pas, cette fonction créera le dossier de manière récursive.
    """
    if os.path.splitext(path)[1] == ".json":
        check_dir_exists(path)

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii = False, indent = indent)
    else:
        print("Erreur ! Il faut donner un fichier avec une extension \"json\" !")

def check_dir_exists(filepath):
    """Check if folder exists, if not, create it."""
    if os.path.isdir(os.path.dirname(filepath)) == False:
        os.makedirs(os.path.dirname(filepath))

def read_json(path : str) -> dict:
    """Donner le chemin vers un fichier json et retourner un dict."""
    if os.path.isfile(path):
        if os.path.splitext(path)[1].lower() == ".json":
            with open(path, 'r') as f:
                return json.load(f)
        else:
            print("Erreur ! Il ne s'agit pas d'un fichier json !")
    else:
        print("Erreur ! Le fichier n'existe pas !")