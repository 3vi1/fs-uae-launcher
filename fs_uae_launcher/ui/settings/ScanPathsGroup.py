from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import fsui as fsui
from fsgs.FSGSDirectories import FSGSDirectories
from ...I18N import _
from ...Settings import Settings
from ..IconButton import IconButton


class ScanPathsGroup(fsui.Group):

    def __init__(self, parent):
        fsui.Group.__init__(self, parent)
        self.layout = fsui.HorizontalLayout()
        # self.layout.padding_left = 10
        # self.layout.padding_top = 10
        # self.layout.padding_right = 10
        # self.layout.padding_bottom = 10

        #image = fsui.Image("fs_uae_launcher:res/search_group.png")
        #self.image_view = fsui.ImageView(self, image)
        #self.layout.add_spacer(20)
        #self.layout.add(self.image_view, valign=0.0)
        #self.layout.add_spacer(20)

        self.layout2 = fsui.VerticalLayout()
        self.layout.add(self.layout2, fill=True, expand=True)

        hlayout = fsui.HorizontalLayout()
        self.layout2.add(hlayout, fill=True, expand=True)

        self.list_view = fsui.ListView(self)
        self.list_view.set_min_height(130)
        self.default_icon = fsui.Image("fs_uae_launcher:res/folder_16.png")
        hlayout.add(self.list_view, expand=True, fill=True)
        hlayout.add_spacer(10)

        vlayout = fsui.VerticalLayout()
        hlayout.add(vlayout, fill=True)

        add_button = IconButton(self, "add_button.png")
        add_button.set_tooltip(_("Add Directory to Search Path"))
        #add_button.disable()
        add_button.activated.connect(self.on_add_button)
        vlayout.add(add_button)
        vlayout.add_spacer(10)

        self.remove_button = IconButton(self, "remove_button.png")
        self.remove_button.set_tooltip(_("Remove Directory from Search Path"))
        self.remove_button.disable()
        self.remove_button.activated.connect(self.on_remove_button)
        vlayout.add(self.remove_button)

        # self.list_view.set_items(self.get_search_path())
        self.repopulate_list()
        self.list_view.on_select_item = self.on_select_item
        Settings.add_listener(self)

    def on_destroy(self):
        Settings.remove_listener(self)

    def on_setting(self, key, value):
        if key == "search_path":
            self.repopulate_list()

    def on_select_item(self, index):
        self.remove_button.enable()

    def repopulate_list(self):
        self.list_view.clear()
        for item in self.get_search_path():
            self.list_view.add_item(item, self.default_icon)

    @classmethod
    def get_search_path(cls):
        paths = FSGSDirectories.get_default_search_path()
        search_path = Settings.get("search_path")
        for p in search_path.split(";"):
            p = p.strip()
            if not p:
                continue
            elif p[0] == "-":
                p = p[1:]
                if p in paths:
                    paths.remove(p)
            else:
                if not p in paths:
                    paths.append(p)
        # the Configurations dir is always scanned on startup (whenever
        # modification time has changed). If we don't include it here too
        # always, the result will be that the configs sometimes appear (on
        # startup) and disappear (on scan)
        if not FSGSDirectories.get_configurations_dir() in paths:
            paths.append(FSGSDirectories.get_configurations_dir())
        return paths

    def on_add_button(self):
        paths = self.get_search_path()
        #search_path = Settings.get("search_path")

        search_path = Settings.get("search_path")
        search_path = [x.strip() for x in search_path.split(";") if x.strip()]

        path = fsui.pick_directory(parent=self.get_window())
        if path:
            for i in range(len(search_path)):
                if search_path[i].startswith("-"):
                    if path == search_path[i][1:]:
                        search_path.remove(search_path[i])
                        break
                else:
                    if search_path[i] == path:
                        # already added
                        break
            else:
                default_paths = FSGSDirectories.get_default_search_path()
                if path not in default_paths:
                    search_path.append(path)
            Settings.set("search_path", ";".join(search_path))

    def on_remove_button(self):
        path = self.list_view.get_item(self.list_view.get_index())
        #search_path = self.get_search_path()

        search_path = Settings.get("search_path")
        search_path = [x.strip() for x in search_path.split(";") if x.strip()]

        for i in range(len(search_path)):
            if search_path[i].startswith("-"):
                if path == search_path[i][1:]:
                    # already removed
                    break
            else:
                if search_path[i] == path:
                    search_path.remove(search_path[i])
                    break
        default_paths = FSGSDirectories.get_default_search_path()
        if path in default_paths:
            search_path.append("-" + path)
        Settings.set("search_path", ";".join(search_path))
