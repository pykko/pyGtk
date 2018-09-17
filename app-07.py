#!/usr/bin/python3
# coding: utf-8

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


app = Gtk.Application()


win = Gtk.Window( title = 'Foody' )
win.set_title( 'Foody' )
win.connect("destroy", Gtk.main_quit)

builder = Gtk.Builder()
builder.add_from_file( "menubar-07.ui" )
win.set_app_menu( builder.get_object( 'menubar' ) )

win.show_all()
Gtk.main()



