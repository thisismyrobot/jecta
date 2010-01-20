import gobject


class Sender(gobject.GObject):
    def __init__(self):
        self.__gobject_init__()


class Receiver(gobject.GObject):
    """ Generic receiver of signals - provides specialisers with 'self.sender'.
    """
    def __init__(self, sender):
        self.__gobject_init__()
        self.sender = sender


class Controller(Receiver):
    """ This maps/translates signals between views and model - acting as the
        'controller'.
    """
    def __init__(self, *args, **kw):
        super(Controller, self).__init__(*args, **kw)
        self.sender.connect('jecta_data_received', self.data_received)
        self.sender.connect('jecta_tag_and_data_received', self.tag_and_data_received)
        self.sender.connect('jecta_dropper_clicked', self.dropper_clicked)
        self.sender.connect('jecta_search_string_updated', self.search_string_updated)
        self.sender.connect('jecta_search_results_ready', self.search_results_ready)

    def data_received(self, sender, data):
        self.sender.emit('jecta_get_tag_for_data', data)

    def tag_and_data_received(self, sender, tag, data):
        self.sender.emit('jecta_add_to_db', tag, data)

    def dropper_clicked(self, sender):
        self.sender.emit('jecta_get_search_tag')

    def search_string_updated(self, sender, search_string):
        self.sender.emit('jecta_search_db', search_string)

    def search_results_ready(self, sender, results):
        self.sender.emit('jecta_display_search_results', results)
