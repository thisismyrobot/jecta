import gtk
import gobject
import widgets


class Sender(gobject.GObject):
    def __init__(self):
        self.__gobject_init__()


class Handler(gobject.GObject):
    """ This handles all custom application signals, acting as the "controller"
        for this application.
    """
    data = None
    tag = None

    def __init__(self, sender):
        self.__gobject_init__()
        sender.connect('jecta_data_received', self.data_received)
        sender.connect('jecta_tag_received', self.tag_received)

    def data_received(self, sender, data):

        #store the data
        self.data = data

        #create and show the tagging widget
        tagger = widgets.Tagger(sender)
        tagger.show()

    def tag_received(self, sender, tag):

        print "got tag:" + tag

#        if tag != self.tag_prompt and tag != '':
#            self.db[tag] = self.text
#            print self.db

#            db_file = open("database.pickle", 'w')
#            pickle.dump(self.db, db_file, -1)
#            db_file.close()

        #import pdb; pdb.set_trace()
#        widget.get_window().destroy()
