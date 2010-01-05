import gtk
import gobject


class Sender(gobject.GObject):
    def __init__(self):
        self.__gobject_init__()


class Handler(gobject.GObject):
    """ This handles all custom application signals, acting as the "controller"
        of the application.
    """
    def __init__(self, sender):
        self.__gobject_init__()
        sender.connect('taggable_data_recieved', self.taggable_data_received)

    def taggable_data_received(self, sender, data):
        print "got taggable data: %s" % data
        #display tagging window
        
