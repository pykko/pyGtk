#!/usr/bin/python3
# coding: utf-8

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk



def traiterValeur( bouton ) :
	print( 'Récupération valeur' )
	print( '> '+ enValeur.get_text() )


if __name__ == '__main__' :
	
	fenetre = Gtk.Window()
	fenetre.connect("destroy", Gtk.main_quit)

	boPrincipale = Gtk.Box( orientation = Gtk.Orientation.VERTICAL , spacing = 2 )
	
	laDirective = Gtk.Label()
	laDirective.set_label( 'Valeur :' )

	enValeur = Gtk.Entry()
	enValeur.set_text( '0')

	buValider = Gtk.Button()
	buValider.set_label( 'Valider' )
	buValider.connect( 'clicked' , traiterValeur )
	
	boPrincipale.pack_start( laDirective , False , False , 2 )
	boPrincipale.pack_start( enValeur , False , False , 2 )
	boPrincipale.pack_start( buValider , False , False , 2 )
	
	fenetre.add( boPrincipale )

	fenetre.show_all()
	Gtk.main()





