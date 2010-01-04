import gtk

class widget:

    def __init__(self):
        self.setup()
        
    def setup(self):
        self.window = gtk.Window()
        w = self.window
        w.set_size_request(800, 100)
        w.drag_dest_set(0, [], 0)
        w.connect('drag_motion', self.motion_cb)
        w.connect('drag_drop', self.drop_cb)
        w.connect('drag_data_received', self.got_data_cb)
        w.connect('destroy', lambda w: gtk.main_quit())
        self.l = gtk.Label()
        w.add(self.l)
        w.show_all()
        gtk.main()
    def motion_cb(self, wid, context, x, y, time):
        self.l.set_text('\n'.join([str(t) for t in context.targets]))
        context.drag_status(gtk.gdk.ACTION_COPY, time)
        # Returning True which means "I accept this data".
        return True

    def drop_cb(self, wid, context, x, y, time):
        # Some data was dropped, get the data
        wid.drag_get_data(context, context.targets[-1], time)
        return True

    def got_data_cb(self, wid, context, x, y, data, info, time):
        # Got data
        text = data.get_text() #gnome files
        if text is None: # fall-back on win
            text = data.data[0:-3]
        self.l.set_text(text)
        context.finish(True, False, time)


widget()
