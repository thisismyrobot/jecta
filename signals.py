import gtk
import gobject


class Sender(gobject.GObject):
    def __init__(self):
        self.__gobject_init__()


class DropHandler(object):

    def motion_cb(self, wid, context, x, y, time):
        #self.l.set_text('\n'.join([str(t) for t in context.targets]))
        context.drag_status(gtk.gdk.ACTION_COPY, time)
        return True

    def drop_cb(self, wid, context, x, y, time):
        wid.drag_get_data(context, context.targets[-1], time)
        return True

    def got_data_cb(self, wid, context, x, y, data, info, time, sender):
        # Got data
        text = data.get_text() #gnome files
        if text is None: # fall-back on windows
            text = data.data

        if text != '':
            sender.emit("taggable_data_recieved", text)

        context.finish(True, False, time)


class DataReceived(gobject.GObject):
    """ This reciever triggers the tagging window for the data.
    """
    def __init__(self, sender):
        self.__gobject_init__()
        sender.connect('taggable_data_recieved', self.taggable_data_received)

    def taggable_data_received(self, sender, data):
        print "got taggable data: %s" % data


class TagHandler(object):
    """ This recieves a tag and saves it to the DB.
    """

