import gtk
import signals
import widgets
import gobject


class Jecta(object):
    """ The Jecta application.
    """
    def __init__(self):

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
        gobject.signal_new("jecta_load_db", 
                           signals.Sender, 
                           gobject.SIGNAL_RUN_FIRST,
                           gobject.TYPE_NONE, 
                           ())
        gobject.signal_new("jecta_add_to_db", 
                           signals.Sender, 
                           gobject.SIGNAL_RUN_FIRST,
                           gobject.TYPE_NONE, 
                           (gobject.TYPE_STRING,))

        #connect signals to handler
        sender = signals.Sender()
        signals.Handler(sender)

        #load the db
        sender.emit("jecta_load_db")

        #create windows, provide signal sender in case needed
        drop_target = widgets.Dropper(sender)
        tagger = widgets.Tagger(sender)

        #show drop target
        drop_target.show()

        gtk.main()


if __name__ == "__main__":
    Jecta()
