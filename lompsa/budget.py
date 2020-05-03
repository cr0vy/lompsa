#!/usr/bin/env python3


import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class BudgetWidget(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
