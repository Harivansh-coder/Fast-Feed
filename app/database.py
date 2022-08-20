class database:

    def __init__(self): 
        self.db = dict()

    def get_all(self):
        return list(self.db.values())
    
    def add_data(self, data = dict, key = str):
        self.db[key] = data

my_database = database()