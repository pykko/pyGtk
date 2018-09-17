#!/usr/bin/python3
# coding: utf-8

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def cliquer( bouton ) :
	print( 'clic' )
	print( 'Bouton> '+ str( bouton ) )
	


win = Gtk.Window( title = 'Foody' )
win.set_title( 'Foody' )
print( dir( win ) )
win.connect("destroy", Gtk.main_quit)

b1 = Gtk.Button( label = 'clic' )
b1.connect( 'clicked' , cliquer )

b2 = Gtk.Button( label = 'clic' )
b2.connect( 'clicked' , cliquer )

box = Gtk.Box( spacing = 10 )
box.pack_start( b1 , True , False , 2 )
box.pack_start( b2 , True , True , 2 )

win.add( box )


win.show_all()
Gtk.main()
