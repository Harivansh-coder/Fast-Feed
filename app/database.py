class database:

    def __init__(self): 
        self.db = dict()

    def get_all(self):
        return list(self.db.values())
    
    def add_data(self, data : dict, key : str):
        self.db[key] = data

    def get_one(self, user_name = str):
        for key, value in self.db.items():
            if value["user_name"] == user_name:
                return value

my_database = database()