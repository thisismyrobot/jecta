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

        #create windows
        drop_target = widgets.Dropper()
        tagger = widgets.Tagger()

        #create signals
        gobject.type_register(signals.Sender)
        gobject.signal_new("taggable_data_recieved", signals.Sender, gobject.SIGNAL_RUN_FIRST,
                           gobject.TYPE_NONE, (gobject.TYPE_STRING,))
        sender = signals.Sender()
        data_reciever = signals.DataReceived(sender)

        #create action handlers
        drop_handler = signals.DropHandler()

        #connect signals up
        drop_target.window.connect('drag_motion', drop_handler.motion_cb)
        drop_target.window.connect('drag_drop', drop_handler.drop_cb)
        drop_target.window.connect('drag_data_received', drop_handler.got_data_cb, sender)

        #show drop target
        drop_target.show()

        gtk.main()


if __name__ == "__main__":
    Jecta()
