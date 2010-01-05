import gtk
import pickle
import widgets


def main():

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
    main()
