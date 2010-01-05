import gtk


class Drop(object):

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
            sender.emit("taggable_data_recieved", text)

        context.finish(True, False, time)
