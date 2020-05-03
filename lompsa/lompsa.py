#!/usr/bin/env python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import sys


class MainWindow(Gtk.Window):
    base_box = None
    left_nav_box = None
    stack_widget = None

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title(title="Lompsa")
        self.set_size_request(800, 600)

        self.setup_window()
        self.add(self.base_box)

    def setup_window(self):
        self.base_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.left_nav_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.stack_widget = Gtk.Stack()

        self.base_box.pack_start(self.left_nav_box, False, False, 0)
        self.base_box.pack_start(self.stack_widget, True, True, 0)


def main(argv: list):
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    main(sys.argv)