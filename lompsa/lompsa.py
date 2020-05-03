#!/usr/bin/env python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import sys

from budget import BudgetWidget


class MainWindow(Gtk.Window):
    base_box = None
    left_nav_box = None
    stack_widget = None

    main_button = None
    budget_button = None

    main_widget = None
    budget_widget = None

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

        self.left_nav_box.set_size_request(150, 600)

        self.main_button = Gtk.Button.new_with_label(label="Main")
        self.budget_button = Gtk.Button.new_with_label(label="Budget")

        self.left_nav_box.pack_start(self.main_button, False, False, 2)
        self.left_nav_box.pack_start(self.budget_button, False, False, 2)

        self.main_widget = MainWidget()
        self.budget_widget = BudgetWidget()

        self.stack_widget.add_named(self.main_widget, "main")
        self.stack_widget.add_named(self.budget_widget, "budget")

        self.budget_button.connect("clicked", self.budget_button_clicked)
        self.main_button.connect("clicked", self.main_button_clicked)

        self.base_box.pack_start(self.left_nav_box, False, False, 0)
        self.base_box.pack_start(self.stack_widget, True, True, 0)

    def budget_button_clicked(self, event):
        self.stack_widget.set_visible_child_name("budget")

    def main_button_clicked(self, event):
        self.stack_widget.set_visible_child_name("main")


class MainWidget(Gtk.Box):
    grid = None

    month_label = None

    def __init__(self):
        Gtk.Box.__init__(self)

        self.setup_widget()

    def setup_widget(self):
        self.grid = Gtk.Grid()

        self.month_label = Gtk.Label(label="May")

        self.grid.attach(self.month_label, 0, 0, 1, 1)

        self.pack_start(self.grid, False, True, 0)


def main(argv: list):
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    main(sys.argv)