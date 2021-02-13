import os
import shutil
import traceback
import zlib

import fsui
from fsbc.resources import Resources
from fsgamesys.FSGSDirectories import FSGSDirectories
from fsui.extra.iconheader import IconHeader

# from workspace.shell import SimpleApplication
from launcher.res import gettext
from workspace.ui.theme import WorkspaceTheme


class ADFCreatorWindow(fsui.Window):
    @classmethod
    def open(cls, parent=None):
        return fsui.open_window_instance(cls, parent)

    def __init__(self, parent=None):
        title = gettext("ADF Disk Image Creator")
        super().__init__(parent, title=title, maximizable=False)
        self.theme = WorkspaceTheme.instance()
        buttons, layout = fsui.DialogButtons.create_with_layout(self)
        if self.window().theme.has_close_buttons:
            buttons.create_close_button()

        self.dialog = None
        self.path = ""

        self.set_icon(fsui.Icon("floppy", "pkg:workspace"))

        layout.min_width = 500

        self.icon_header = IconHeader(
            self,
            fsui.Icon("floppy", "pkg:workspace"),
            gettext("ADF Disk Image Creator"),
            gettext("Create a blank or formatted ADF floppy disk image"),
        )
        layout.add(self.icon_header, fill=True, margin_bottom=20)

        label = fsui.Label(self, gettext("Create disk image of type:"))
        layout.add(label)
        layout.add_spacer(6)
        self.list_view = fsui.ListView(self)
        self.list_view.set_min_width(560)
        self.list_view.set_min_height(60)
        icon = fsui.Image("workspace:res/16x16/floppy.png")
        self.list_view.add_item(
            gettext("ADF - Standard Floppy Disk Image"), icon
        )
        self.list_view.add_item(
            gettext("ADF - Extended Floppy Disk Image (MFM Encoded)"), icon
        )
        layout.add(self.list_view, expand=True, fill=True)
        # self.list_view.on_select_item = self.on_select_item
        self.list_view.item_selected.connect(self.on_item_selected)

        layout.add_spacer(20)
        label = fsui.Label(self, gettext("Filename for the new disk image:"))
        layout.add(label)
        layout.add_spacer(6)
        hori_layout = fsui.HorizontalLayout()
        layout.add(hori_layout, fill=True)
        self.name_field = fsui.TextField(self, "", read_only=False)
        hori_layout.add(self.name_field, expand=True)
        text = gettext("Size:")
        label = fsui.Label(self, text)
        hori_layout.add(label, margin_left=20)
        self.size_field = fsui.TextField(self, "")
        self.size_field.set_min_width(60)
        hori_layout.add(self.size_field, expand=False, margin_left=10)
        text = gettext("MB")
        label = fsui.Label(self, text)
        hori_layout.add(label, margin_left=10)

        layout.add_spacer(20)
        label = fsui.Label(self, gettext("Save to directory:"))
        layout.add(label)
        layout.add_spacer(6)
        hori_layout = fsui.HorizontalLayout()
        layout.add(hori_layout, fill=True)
        self.dir_field = fsui.TextField(self, "", read_only=True)
        hori_layout.add(self.dir_field, expand=True)
        self.browse_button = fsui.Button(self, gettext("Browse"))
        self.browse_button.actived.connect(self.on_browse_clicked)
        hori_layout.add(self.browse_button, margin_left=10)

        self.created_label = fsui.Label(self, "")
        layout.add(self.created_label, fill=True)

        # layout.add_spacer(20)
        # layout.add_spacer(20)
        # hori_layout = fsui.HorizontalLayout()
        # layout.add(hori_layout, fill=True)
        # self.created_label = fsui.Label(self, "")
        # hori_layout.add(self.created_label, expand=True)
        # hori_layout.add_spacer(20)
        self.create_button = fsui.Button(buttons, gettext("Create"))
        # self.create_button.activated.connect(self.on_create_clicked)
        self.create_button.activated.connect(self.on_create_clicked)
        # hori_layout.add(self.create_button)
        buttons.add_button(self.create_button)

        self.list_view.select_item(0)
        self.update_name_suggestion()

        # self.set_size_from_layout()
        # self.center_on_parent()

    def __del__(self):
        print("ADFCreator.__del__")

    def update_name_suggestion(self):
        k = 1
        while True:
            if k > 1:
                name = "New Disk {0}.adf".format(k)
            else:
                name = "New Disk.adf"
            if not os.path.exists(os.path.join(self.path, name)):
                self.name_field.set_text(name)
                return
            k += 1

    def on_item_selected(self, index):
        self.set_path(FSGSDirectories.get_floppies_dir())
        if index == 0:
            size = "0.86"
        elif index == 1:
            size = "2.00"
        else:
            raise Exception("Unexpected index " + repr(index))
        self.size_field.set_text(size)
        self.size_field.set_enabled(False)

    def set_path(self, path):
        self.path = path
        self.dir_field.set_text(path)

    def on_browse_clicked(self):
        # if hasattr(self, "dialog"):
        #    return
        self.dialog = fsui.DirDialog(
            None, gettext("Select Destination Directory")
        )
        self.dialog.accepted.connect(self.on_dialog_accepted)
        # self.dialog.destroyed.connect(self.on_dialog_destroyed)
        # self.dialog.finished.connect(self.on_dialog_finished)
        self.dialog.show()
        # if dialog.show_modal():
        #     self.set_path(dialog.get_path())
        # dialog.destroy()

    def on_dialog_accepted(self):
        print("accepted")
        print(self.dialog)
        self.set_path(self.dialog.get_path())
        self.dialog = None

    # def on_dialog_destroyed(self):
    #     self.dialog = None

    # def on_dialog_finished(self, result):
    #     # del self.dialog
    #     # self.dialog = None
    #     # return
    #     print("finished")
    #     if self.dialog.result():
    #         print("result")
    #         self.set_path(self.dialog.get_path())
    #     # self.dialog.destroy()
    #     # print("...")
    #     del self.dialog

    def on_create_clicked(self):
        try:
            self.create_disk_file()
        except Exception as e:
            traceback.print_exc()
            self.show_error(repr(e))

    def show_error(self, message):
        self.created_label.set_text(message)
        fsui.show_error(message)

    def show_success(self, message):
        self.created_label.set_text(message)

    def create_disk_file(self):
        self.created_label.set_text("")
        disk_type = self.list_view.index()
        path = self.dir_field.get_text().strip()
        if not os.path.isdir(path):
            return self.show_error(
                gettext("Specified directory does not exist")
            )
        name = self.name_field.get_text().strip()
        ext = ".adf"
        if not name.lower().endswith(ext):
            name += ext
        path = os.path.join(path, name)

        # if disk_type == 0:
        #     size = 901120
        # elif disk_type == 1:
        #     size = 2104892

        if os.path.exists(path):
            return self.show_error(gettext("File already exists"))

        path_partial = path + ".partial"
        try:
            f = open(path_partial, "wb")
        except Exception:
            print("error opening", path)
            traceback.print_exc()
            return self.show_error(gettext("Could not open file for writing"))

        try:
            if disk_type == 0:
                self.create_adf(f)
            elif disk_type == 1:
                self.create_extended_adf(f)
        except Exception:
            traceback.print_exc()
            try:
                f.close()
            except Exception:
                pass
            try:
                os.unlink(path_partial)
            except Exception:
                pass
            return self.show_error(gettext("Error writing disk image"))
        else:
            f.close()
            try:
                shutil.move(path_partial, path)
            except Exception:
                print("error moving", path_partial, path)
                traceback.print_exc()
                return self.show_error(gettext("Error moving file into place"))

        self.show_success(gettext("Disk image created") + ": " + name)

    def create_adf(self, f):
        s = Resources("fsgs").stream("res/amiga/adf.dat")
        data = s.read()
        data = zlib.decompress(data)
        f.write(data)

    def create_extended_adf(self, f):
        # Workbench 3.1 does not like the adf_extended file, created by
        # WinUAE (must check why)
        s = Resources("fsgs").stream("res/amiga/adf_save_disk.dat")
        data = s.read()
        data = zlib.decompress(data)
        f.write(data)


# application = SimpleApplication(ADFCreatorWindow)
