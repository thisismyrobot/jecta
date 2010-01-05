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


class Tagger(Widget):

    tag_prompt = 'Type in a tag'
    text = ''

    def __init__(self, text, db):
        super(Tagger, self).__init__()
        self.window.set_size_request(300, 30)
        self.window.set_title(self.tag_prompt)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.text = text
        self.db = db

        self.tag_entry = gtk.Entry()
        self.tag_entry.set_text(self.tag_prompt)
        self.tag_entry.connect("activate", self.parse_tag, self.tag_entry)

        self.window.add(self.tag_entry)
        self.window.show_all()

    def parse_tag(self, widget, entry):

        #handle the tag here
        tag = entry.get_text()
        if tag != self.tag_prompt and tag != '':
            self.db[tag] = self.text
            print self.db

            db_file = open("database.pickle", 'w')
            pickle.dump(self.db, db_file, -1)
            db_file.close()

        self.window.destroy()


class Dropper(Widget):

    def __init__(self, db):
        super(Dropper, self).__init__()
        self.window.set_size_request(150, 150)
        self.window.drag_dest_set(0, [], 0)
        self.window.set_opacity(0.75)
        self.window.set_keep_above(True)
        self.window.connect('drag_motion', self.motion_cb)
        self.window.connect('drag_drop', self.drop_cb)
        self.window.connect('drag_data_received', self.got_data_cb)
        self.window.show_all()
        self.db = db

    def motion_cb(self, wid, context, x, y, time):
        #self.l.set_text('\n'.join([str(t) for t in context.targets]))
        context.drag_status(gtk.gdk.ACTION_COPY, time)
        return True

    def drop_cb(self, wid, context, x, y, time):
        wid.drag_get_data(context, context.targets[-1], time)
        return True

    def got_data_cb(self, wid, context, x, y, data, info, time):
        # Got data
        text = data.get_text() #gnome files
        if text is None: # fall-back on windows
            text = data.data[0:-3]

        #launch labeler
        Tagger(text, self.db)

        context.finish(True, False, time)


