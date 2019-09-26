from csv_manager import CSV_Manager
from manipulator import Manipulator
import json

def run(filter_field, value=False):
    reader = CSV_Manager("./articles.csv")
    if value:
        articles = reader.get_csv_as_dicts()
        manipulator = Manipulator(articles)
        filtered = manipulator.filter_by(filter_field, value)
    
        print(json.dumps(filtered, indent=2))
    else:
        reader.read()
        manipulator = Manipulator(reader.mapped_dict)
        manipulator.relevant(filter_field)

run("author", "a1")
run("author1")



