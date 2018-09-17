#!/usr/bin/python3
# coding: utf-8

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def cliquer( bouton ) :
	print( 'clic' )
	print( 'Bouton> '+ str( bouton ) )
	

#win = Gtk.Window( title = 'Foody' )

win = Gtk.Window( title = 'Foody' )
win.set_title( 'Foody' )
print( dir( win ) )
win.connect("destroy", Gtk.main_quit)

b = Gtk.Button( label = 'clic' )
b.connect( 'clicked' , cliquer )
win.add( b )


win.show_all()
Gtk.main()
