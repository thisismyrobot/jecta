import gtk
import gobject
import widgets
import database


class Sender(gobject.GObject):
    def __init__(self):
        self.__gobject_init__()


class Handler(gobject.GObject):
    """ This handles all custom application signals, acting as the "controller"
        for this application. It stores a instance of the database and the data
        for the last tag.
    """
    def __init__(self, sender):
        self.__gobject_init__()
        sender.connect('jecta_data_received', self.data_received)
        sender.connect('jecta_tag_received', self.tag_received)
        sender.connect('jecta_load_db', self.load_db)
        sender.connect('jecta_add_to_db', self.add_to_db)
        sender.connect('jecta_search_request_received', self.search_request_received)
        sender.connect('jecta_search_string_received', self.search_string_recieved)

    def data_received(self, sender, data):
        self.data = data
        tagger = widgets.Tagger(sender)
        tagger.show()

    def tag_received(self, sender, tag):
        sender.emit('jecta_add_to_db', tag, self.data)
        self.data = None

    def add_to_db(self, sender, tag, data):
        self.db.add(tag, data)

    def load_db(self, sender):
        self.db = database.Database()

    def search_request_received(self, sender):
        searcher = widgets.Searcher(sender)
        searcher.show()

    def search_string_recieved(self, sender, search_string, entry):
        print self.db.search(search_string)
