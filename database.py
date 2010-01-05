import pickle


class Database(object):

    mapping = {}

    def __init__(self):
        self.load()

    def add(self, tag, data):
        if tag in self.mapping:
            self.mapping[tag].append(data)
        else:
            self.mapping[tag] = [data]
        print self.mapping
        db_file = open("database.pickle", 'w')
        pickle.dump(self.mapping, db_file, -1)
        db_file.close()

    def load(self):
        try:
            db_file = open("database.pickle", 'r')
            self.mapping = pickle.load(db_file)
            db_file.close()
        except:
            self.mapping = {}
