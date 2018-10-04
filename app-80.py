#!/usr/bin/python3
# coding: utf-8

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def indiquerSiMajeur( bouton ) :

	age = int( en_age.get_text() )
	if age < 18 :
		la_majorite.set_label( 'Livreur mineur' )
	else :
		la_majorite.set_label( 'Livreur majeur' )

	
if __name__ == '__main__' :
	
	fenetre = Gtk.Window()
	fenetre.set_title( 'Foody' )
	fenetre.connect("destroy", Gtk.main_quit)

	la_age = Gtk.Label()
	la_age.set_label( 'Âge du Livreur :' )
	la_age.set_halign( Gtk.Align.START )

	en_age = Gtk.Entry()
	en_age.set_text( '0')
	en_age.set_alignment( xalign = 1 )
	
	la_majorite = Gtk.Label()
	la_majorite.set_label( 'Livreur mineur' )
	la_majorite.set_halign( Gtk.Align.CENTER )

	bu_testMajorite = Gtk.Button()
	bu_testMajorite.set_label( 'Majorité ?' )
	bu_testMajorite.connect( 'clicked' , indiquerSiMajeur )
	
	bo_principale = Gtk.Box()
	bo_principale.set_orientation( Gtk.Orientation.VERTICAL )
	bo_principale.set_spacing( 2 )
	bo_principale.set_margin_top( 10 )
	bo_principale.set_margin_bottom( 10 )
	bo_principale.set_margin_left( 10 )
	bo_principale.set_margin_right( 10 )
	
	
	bo_principale.pack_start( la_age , False , False , 2 )
	bo_principale.pack_start( en_age , False , False , 2 )
	bo_principale.pack_start( bu_testMajorite , False , False , 2 )
	bo_principale.pack_start( la_majorite , False , False , 2 )
	
	
	
	fenetre.add( bo_principale )

	fenetre.show_all()
	Gtk.main()
