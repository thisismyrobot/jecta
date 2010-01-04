import gtk


class appwindow(object):
    """ This is a window in the application - basic application-wide settings
        are set here.
    """
    window = None

    def __init__(self):
        self.window = gtk.Window()


class tagger(appwindow):

    def __init__(self, text):
        super(tagger, self).__init__()
        w = self.window
        self.window.set_size_request(300, 50)
        self.window.set_title("Enter tag")
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_decorated(False)

        tag_label = gtk.Label()
        tag_label.set_text("Enter tag")
        tag_entry = gtk.Entry()
        tag_entry.connect("activate", self.enter_pressed, tag_entry)

        vbox = gtk.VBox(False, 0)
        vbox.add(tag_label)
        vbox.add(tag_entry)

        self.window.add(vbox)
        self.window.show_all()

    def enter_pressed(self, widget, entry):

        #handle the tag here
        print entry.get_text()

        self.window.destroy()


class dropper(appwindow):

    def __init__(self):
        super(dropper, self).__init__()
        self.window.set_size_request(150, 150)
        self.window.drag_dest_set(0, [], 0)
        self.window.set_opacity(0.75)
        self.window.set_keep_above(True)
        self.window.set_decorated(False)
        self.window.connect('drag_motion', self.motion_cb)
        self.window.connect('drag_drop', self.drop_cb)
        self.window.connect('drag_data_received', self.got_data_cb)
        self.window.show_all()
        gtk.main()
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
        tagger(text)

        context.finish(True, False, time)


dropper()

