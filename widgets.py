import gtk
import pickle


class Widget(object):
    """ This is a window(widget) in the application - basic application-wide 
        settings are set here.
    """
    window = None

    def __init__(self):
        self.window = gtk.Window()
        #self.window.set_decorated(False)

    def show(self):
        self.window.show_all()

    def hide(self):
        self.window.hide()


class Tagger(Widget):

    tag_prompt = 'Type in a tag'
    text = ''

    def __init__(self):
        super(Tagger, self).__init__()
        self.window.set_size_request(300, 30)
        self.window.set_title(self.tag_prompt)
        self.window.set_position(gtk.WIN_POS_CENTER)

        self.tag_entry = gtk.Entry()
        self.tag_entry.set_text(self.tag_prompt)
        self.tag_entry.connect("activate", self.parse_tag, self.tag_entry)

        self.window.add(self.tag_entry)

    def parse_tag(self, widget, entry):

        #handle the tag here
        tag = entry.get_text()

        print tag

#        if tag != self.tag_prompt and tag != '':
#            self.db[tag] = self.text
#            print self.db

#            db_file = open("database.pickle", 'w')
#            pickle.dump(self.db, db_file, -1)
#            db_file.close()

        self.window.destroy()


class Dropper(Widget):

    def __init__(self):
        super(Dropper, self).__init__()
        self.window.set_size_request(150, 150)
        self.window.drag_dest_set(0, [], 0)
        self.window.set_opacity(0.75)
        self.window.set_keep_above(True)
