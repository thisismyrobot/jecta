import gtk
import signals


class Widget(signals.Receiver):
    """ This is a window(widget) in the application - basic application-wide 
        settings are set here.
    """
    def __init__(self, *args, **kw):
        super(Widget, self).__init__(*args, **kw)
        self.window = gtk.Window()
        self.window.connect("destroy", self.close)
        self.window.set_keep_above(True)

    def show(self):
        self.create_window()
        self.window.show_all()

    def create_window(self):
        """ Specialisations should overwrite to generate window from self.window.
        """

    def close(self, window):
        self.window.destroy()


class Tagger(Widget):

    tag_prompt = 'Type in a tag'

    def __init__(self, *args, **kw):
        super(Tagger, self).__init__(*args, **kw)
        self.sender.connect('jecta_get_tag_for_data', self.get_tag_for_data)

    def get_tag_for_data(self, sender, data):
        self.data = data
        self.show()

    def create_window(self):
        self.window.set_size_request(300, 30)
        self.window.set_title(self.tag_prompt)
        self.window.set_position(gtk.WIN_POS_CENTER)
        tag_entry = gtk.Entry()
        tag_entry.set_text(self.tag_prompt)
        tag_entry.connect("activate", self.tag_submitted)
        self.window.add(tag_entry)

    def tag_submitted(self, entry):
        tag = entry.get_text()
        if tag != self.tag_prompt and tag != '' and tag is not None:
            self.sender.emit("jecta_tag_and_data_received", tag, self.data)
        self.window.destroy()


class Searcher(Widget):

    search_prompt = 'Find by tag'

    def __init__(self, *args, **kw):
        super(Searcher, self).__init__(*args, **kw)
        self.sender.connect('jecta_get_search_tag', self.get_search_tag)

    def get_search_tag(self, sender):
        self.show()

    def create_model(self):
        store = gtk.ListStore(str)
        for row in ['a','b','c','d']:
            store.append([row])
        return store

    def create_columns(self, treeView):
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Results", rendererText, text=0)
        column.set_sort_column_id(0)
        treeView.append_column(column)


    def create_window(self):
        self.window.set_size_request(300, 300)
        self.window.set_title(self.search_prompt)
        self.window.set_position(gtk.WIN_POS_CENTER)

        search_entry = gtk.Entry()
        search_entry.set_text(self.search_prompt)
        search_entry.connect("changed", self.search)

        store = self.create_model()
        results_listing = gtk.TreeView(store)
        self.create_columns(results_listing)

        results_scroller = gtk.ScrolledWindow()
        results_scroller.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        results_scroller.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        results_scroller.add(results_listing)

        layout = gtk.Table(2, 1, False)
        layout.attach(search_entry, 0, 1, 0, 1, xoptions=gtk.FILL, yoptions=gtk.FILL)
        layout.attach(results_scroller, 0, 1, 1, 2)

        self.window.add(layout)

    def search(self, entry):
        search_string = entry.get_text()
        if search_string != self.search_prompt and search_string != '' and search_string is not None:
            self.sender.emit("jecta_search_string_updated", search_string)


class Dropper(Widget):

    def create_window(self):
        self.window.set_size_request(150, 150)
        self.window.drag_dest_set(0, [], 0)
        self.window.set_opacity(0.75)
        self.window.connect('drag_motion', self.motion_cb)
        self.window.connect('drag_drop', self.drop_cb)
        self.window.connect('drag_data_received', self.got_data_cb)
        self.window.connect('delete-event', gtk.main_quit)
        self.window.connect('button-press-event', self.clicked)
        self.window.set_events(gtk.gdk.BUTTON_PRESS_MASK)

    def motion_cb(self, wid, context, x, y, time):
        context.drag_status(gtk.gdk.ACTION_COPY, time)
        return True

    def drop_cb(self, wid, context, x, y, time):
        wid.drag_get_data(context, context.targets[-1], time)
        return True

    def got_data_cb(self, wid, context, x, y, data, info, time):
        text = data.get_text() #gnome files

        #fall-back on windows
        if text is None:
            text = data.data

        if text != '' and text is not None:
            self.sender.emit("jecta_data_received", text)

        context.finish(True, False, time)

    def clicked(self, window, event):
        if event.button == 1:
            self.sender.emit("jecta_dropper_clicked")
