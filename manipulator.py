import json

class Manipulator:
    def __init__(self, data):
        self.data = data

    def filter_by(self, key, value):
        return list(
            filter(lambda d: d[key] == value, self.data)
        )

    def relevant(self,key):
        print(json.dumps(self.data[key], indent=2))

