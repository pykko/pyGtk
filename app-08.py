#!/usr/bin/python3
# coding: utf-8

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk , Gdk




win = Gtk.Window( title = 'Foody' )
win.set_title( 'Foody' )
win.connect("destroy", Gtk.main_quit)

uimanager = win.create_ui_manager()
menubar = uimanager.get_widget("/MenuBar")

box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
box.pack_start(menubar, False, False, 0)

win.add( box )

win.show_all()
Gtk.main()
