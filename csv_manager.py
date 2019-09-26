import csv


class CSV_Manager:
    def __init__(self, filename):
        self.filename = filename
        self.mapped_dict={}

    def get_csv_as_dicts(self):
        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            rows = [row for row in csv_reader]
            return self.to_dict(rows)

    def to_dict(self, rows):
        keys = rows[0]
        all_data = []

        for row in rows:
            data_dict = {}
            for i in range(0, len(row)):
                data_dict[keys[i]] = row[i]
            all_data.append(data_dict)

        return all_data
        
    def read(self):
        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            rows = [row for row in csv_reader]
            # print(rows)

            a1_array = []
            a2_array = []
            a3_array = []
            c1_array = []
            c2_array = []
            c3_array = []
            
            for row in rows:
                if row[3]=='a1':
                    a1_array.append(row)
                elif row[3]=='a2':
                    a2_array.append(row)
                elif row[3]=='a3':
                    a3_array.append(row)

            for row in rows:
                if row[2]=='c1':
                    c1_array.append(row)
                elif row[2]=='c2':
                    c2_array.append(row)
                elif row[2]=='c3':
                    c3_array.append(row)

            self.mapped_dict = {
                "author1" : a1_array,
                "author2" : a2_array,
                "author3" : a3_array,
                "category1" : c1_array,
                "category2" : c2_array,
                "category3" : c3_array
            }

            # print(self.mapped_dict)
            

            




        
