import pickle
import signals


class Database(signals.Receiver):

    mapping = {}

    def __init__(self, *args, **kw):
        super(Database, self).__init__(*args, **kw)
        self.sender.connect('jecta_add_to_db', self.add_to_db)
        self.sender.connect('jecta_search_db', self.search_db)
        self.load()

    def add_to_db(self, sender, tag, data):
        self.add(tag, data)

    def search_db(self, sender, query):
        results = self.search(query)
        sender.emit('jecta_search_results_ready', results)

    def add(self, tag, data):
        if tag in self.mapping:
            self.mapping[tag].append(data)
        else:
            self.mapping[tag] = [data]
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

    def search(self, query):
        results = []
        for tag,data in self.mapping.items():
            if tag.startswith(query):
                for item in data:
                    results.append((tag, item))
        return results
