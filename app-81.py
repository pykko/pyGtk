#!/usr/bin/python3
# coding: utf-8

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


REMUNERATION_COURSE = 2.5

def calculerRemuneration( bouton ) :

	valeurSaisie = ent_nbLiv.get_text()
	
	if valeurSaisie.isdigit() == True :
		nbCourses = int( valeurSaisie )
		remuneration = nbCourses * REMUNERATION_COURSE ;
		ent_remun.set_text( str( remuneration ) + ' €' )
	else :
		md_erreur = Gtk.MessageDialog( fenetre , 0 , Gtk.MessageType.ERROR , Gtk.ButtonsType.OK , "Saisie incorrecte." )
		md_erreur.format_secondary_text( 'Veuillez saisir une grandeur numérique entière.' )
		md_erreur.run()


	
if __name__ == '__main__' :
	
	fenetre = Gtk.Window()
	fenetre.set_title( 'Foody' )
	fenetre.connect("destroy", Gtk.main_quit)

	lab_nbLiv = Gtk.Label()
	lab_nbLiv.set_label( 'Nombre de courses :' )
	lab_nbLiv.set_halign( Gtk.Align.START )

	ent_nbLiv = Gtk.Entry()
	ent_nbLiv.set_text( '0' )
	ent_nbLiv.set_alignment( xalign = 1 )
	
	but_calculerRem = Gtk.Button()
	but_calculerRem.set_label( 'Calculer la rémunération' )
	but_calculerRem.connect( 'clicked' , calculerRemuneration )
	
	lab_remun = Gtk.Label()
	lab_remun.set_label( 'Rémunération :' )
	lab_remun.set_halign( Gtk.Align.START )
	
	ent_remun = Gtk.Entry()
	ent_remun.set_text( '0 €' )
	ent_remun.set_editable( False )
	ent_remun.set_alignment( xalign = 1 )

	
	
	box_principale = Gtk.Box()
	box_principale.set_orientation( Gtk.Orientation.VERTICAL )
	box_principale.set_spacing( 2 )
	box_principale.set_margin_top( 10 )
	box_principale.set_margin_bottom( 10 )
	box_principale.set_margin_left( 10 )
	box_principale.set_margin_right( 10 )
	
	
	box_principale.pack_start( lab_nbLiv , False , False , 2 )
	box_principale.pack_start( ent_nbLiv , False , False , 2 )
	box_principale.pack_start( but_calculerRem , False , False , 2 )
	box_principale.pack_start( lab_remun , False , False , 2 )
	box_principale.pack_start( ent_remun , False , False , 2 )
	
	
	
	fenetre.add( box_principale )

	fenetre.show_all()
	Gtk.main()
