import gtk
import pickle
import widgets


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

        widgets.Dropper(db)
        gtk.main()


if __name__ == "__main__":
    Jecta()
