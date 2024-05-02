from pathlib import Path
from tinydb import TinyDB, Query
from tinydb import where



def save_db(db_name, json_data):
    Path("data/").mkdir(exist_ok=True)
    try:
        db = TinyDB(f"data/{db_name}.json")
    except FileNotFoundError:
        with open(f"data/{db_name}.json", "w"):
            pass
        db = TinyDB("data/" + db_name + ".json")

    db.insert(json_data)  #nom de la var des données json_data -> json
    print("sauvegardé avec succès.")

def load_db(db_name):
    db=TinyDB(f'data/{db_name}.json')
    return db.all()

def update_db(db_name, serialized_data):
    db = TinyDB(f"data/{db_name}.json")
    db.update(
        serialized_data,
        where('id') == serialized_data['id']
    )
    print(f"{serialized_data['id']} updaté avec succès.")