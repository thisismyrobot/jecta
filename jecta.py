import gtk


class appwindow(object):
    """ This is a window in the application - basic application-wide settings
        are set here.
    """
    window = None

    def __init__(self):
        self.window = gtk.Window()


class labeler(appwindow):
    pass


class dropwidget(appwindow):

    def __init__(self):
        super(dropwidget, self).__init__()
        w = self.window
        w.set_size_request(150, 150)
        w.drag_dest_set(0, [], 0)
        w.set_opacity(0.75)
        w.set_keep_above(True)
        w.set_decorated(False)
        #w.set_has_frame(True)
        w.connect('drag_motion', self.motion_cb)
        w.connect('drag_drop', self.drop_cb)
        w.connect('drag_data_received', self.got_data_cb)
        w.connect('destroy', lambda w: gtk.main_quit())
        w.show_all()
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
        diag = gtk.MessageDialog(message_format=text)
        diag.show()
        context.finish(True, False, time)


dropwidget()
