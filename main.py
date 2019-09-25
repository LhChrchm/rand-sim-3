from csv_manager import CSV_Manager
from manipulator import Manipulator
import json

def run(filter_field, value):
    reader = CSV_Manager("./articles.csv")
    articles = reader.get_csv_as_dicts()
    manipulator = Manipulator(articles)

    filtered = manipulator.filter_by(filter_field, value)
    print(json.dumps(filtered, indent=2))
    

#run("author", "a2")

CSV_Man = CSV_Manager("articles.csv")

CSV_Man.read()
