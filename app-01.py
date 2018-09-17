#!/usr/bin/python3
# coding: utf-8

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)

label = Gtk.Label()
label.set_label("Foody")
label.set_angle(25)
label.set_halign(Gtk.Align.END)
win.add( label )

win.show_all()
Gtk.main()
