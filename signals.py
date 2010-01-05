import gtk
import gobject
import pickle
import widgets


class Sender(gobject.GObject):
    def __init__(self):
        self.__gobject_init__()


class Handler(gobject.GObject):
    """ This handles all custom application signals, acting as the "controller"
        for this application.
    """
    db = None
    data = None

    def __init__(self, sender):
        self.__gobject_init__()
        sender.connect('jecta_data_received', self.data_received)
        sender.connect('jecta_tag_received', self.tag_received)
        sender.connect('jecta_load_db', self.load_db)
        sender.connect('jecta_add_to_db', self.add_to_db)

    def data_received(self, sender, data):
        self.data = data
        tagger = widgets.Tagger(sender)
        tagger.show()

    def tag_received(self, sender, tag):
        sender.emit('jecta_add_to_db', tag)

    def add_to_db(self, sender, tag):
        self.db[tag] = self.data
        print self.db
        db_file = open("database.pickle", 'w')
        pickle.dump(self.db, db_file, -1)
        db_file.close()

    def load_db(self, sender):
        try:
            db_file = open("database.pickle", 'r')
            self.db = pickle.load(db_file)
            db_file.close()
        except:
            self.db = {}

