import gtk
import signals
import widgets
import gobject
import database


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
        gobject.signal_new("jecta_tag_and_data_received",
                           signals.Sender,
                           gobject.SIGNAL_RUN_FIRST,
                           gobject.TYPE_NONE,
                           (gobject.TYPE_STRING, gobject.TYPE_STRING))
        gobject.signal_new("jecta_get_tag_for_data",
                           signals.Sender,
                           gobject.SIGNAL_RUN_FIRST,
                           gobject.TYPE_NONE,
                           (gobject.TYPE_STRING,))
        gobject.signal_new("jecta_add_to_db",
                           signals.Sender,
                           gobject.SIGNAL_RUN_FIRST,
                           gobject.TYPE_NONE,
                           (gobject.TYPE_STRING, gobject.TYPE_STRING))
        gobject.signal_new("jecta_dropper_clicked",
                           signals.Sender,
                           gobject.SIGNAL_RUN_FIRST,
                           gobject.TYPE_NONE,
                           ())
        gobject.signal_new("jecta_get_search_tag",
                           signals.Sender,
                           gobject.SIGNAL_RUN_FIRST,
                           gobject.TYPE_NONE,
                           ())
        gobject.signal_new("jecta_search_string_updated",
                           signals.Sender,
                           gobject.SIGNAL_RUN_FIRST,
                           gobject.TYPE_NONE,
                           (gobject.TYPE_STRING,))
        gobject.signal_new("jecta_search_db",
                           signals.Sender,
                           gobject.SIGNAL_RUN_FIRST,
                           gobject.TYPE_NONE,
                           (gobject.TYPE_STRING,))
        gobject.signal_new("jecta_search_results_received",
                           signals.Sender,
                           gobject.SIGNAL_RUN_FIRST,
                           gobject.TYPE_NONE,
                           (gobject.TYPE_STRING,))

        #create the signal sender
        sender = signals.Sender()

        #create the controller
        signals.Controller(sender)

        #create windows, provide signal sender
        drop_target = widgets.Dropper(sender)
        widgets.Tagger(sender)
        widgets.Searcher(sender)
        database.Database(sender)

        #show drop target
        drop_target.show()

        gtk.main()


if __name__ == "__main__":
    Jecta()
