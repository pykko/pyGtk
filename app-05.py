#!/usr/bin/python3
# coding: utf-8

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


win = Gtk.Window( title = 'Foody' )
win.set_title( 'Foody' )
win.connect("destroy", Gtk.main_quit)

b1 = Gtk.Button( label = 'Bouton 1' )
b2 = Gtk.Button( label = 'Bouton 2' )
b3 = Gtk.Button( label = 'Bouton 3' )
b4 = Gtk.Button( label = 'Bouton 4' )
b5 = Gtk.Button( label = 'Bouton 5' )
b6 = Gtk.Button( label = 'Bouton 6' )
b7 = Gtk.Button( label = 'Bouton 7' )
b8 = Gtk.Button( label = 'Bouton 8' )


g = Gtk.Grid()
g.add( b1 )
g.add( b2 )
g.add( b3 )

g.attach( b4 , 1 , 1 , 2 , 1 )
g.attach( b5 , 0 , 1 , 1 , 1 )


win.add( g )
win.show_all()
Gtk.main()
