import gtk
import pickle
import signals
import widgets
import gobject


class Jecta(object):
    """ The Jecta application.
    """
    def __init__(self):

        #load db
        db = {}
        try:
            db_file = open("database.pickle", 'r')
            db = pickle.load(db_file)
            db_file.close()
        except:
            pass

        #create signals
        gobject.type_register(signals.Sender)
        gobject.signal_new("jecta_data_received", 
                           signals.Sender, 
                           gobject.SIGNAL_RUN_FIRST,
                           gobject.TYPE_NONE, 
                           (gobject.TYPE_STRING,))
        gobject.signal_new("jecta_tag_received", 
                           signals.Sender, 
                           gobject.SIGNAL_RUN_FIRST,
                           gobject.TYPE_NONE, 
                           (gobject.TYPE_STRING,))

        #connect signals to handler
        sender = signals.Sender()
        signals.Handler(sender)

        #create windows, provide signal sender in case needed
        drop_target = widgets.Dropper(sender)
        tagger = widgets.Tagger(sender)

        #show drop target
        drop_target.show()

        gtk.main()


if __name__ == "__main__":
    Jecta()
