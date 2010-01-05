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

    def __init__(self, sender):
        super(Tagger, self).__init__()

        self.window.set_size_request(300, 30)
        self.window.set_title(self.tag_prompt)
        self.window.set_position(gtk.WIN_POS_CENTER)

        tag_entry = gtk.Entry()
        tag_entry.set_text(self.tag_prompt)
        tag_entry.connect("activate", self.tag_submitted, sender)

        self.window.add(tag_entry)

    def tag_submitted(self, entry, sender):
        tag = entry.get_text()
        if tag != '' and tag is not None:
            sender.emit("jecta_tag_received", tag)
        self.window.destroy()


class Dropper(Widget):

    def __init__(self, sender):
        super(Dropper, self).__init__()
        self.window.set_size_request(150, 150)
        self.window.drag_dest_set(0, [], 0)
        self.window.set_opacity(0.75)
        self.window.set_keep_above(True)
        self.window.connect('drag_motion', self.motion_cb)
        self.window.connect('drag_drop', self.drop_cb)
        self.window.connect('drag_data_received', self.got_data_cb, sender)

    def motion_cb(self, wid, context, x, y, time):
        context.drag_status(gtk.gdk.ACTION_COPY, time)
        return True

    def drop_cb(self, wid, context, x, y, time):
        wid.drag_get_data(context, context.targets[-1], time)
        return True

    def got_data_cb(self, wid, context, x, y, data, info, time, sender):
        text = data.get_text() #gnome files

        #fall-back on windows
        if text is None:
            text = data.data

        if text != '' and text is not None:
            sender.emit("jecta_data_received", text)

        context.finish(True, False, time)
