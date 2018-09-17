#!/usr/bin/python3
# coding: utf-8

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib , Gio , Gtk


MENU_XML = '''
<?xml version="1.0" encoding="UTF-8"?>
<interface>
	<menu id="app-menu" >
		<section>
			<item>
				<attribute name="action">app.about</attribute>
				<attribute name="label">_About</attribute>
			</item>
			<item>
				<attribute name="action">app.quit</attribute>
				<attribute name="label">_Quit</attribute>
			</item>
		</section>
	</menu>
</interface>
'''


win = Gtk.Window( title = 'Foody' )
win.set_title( 'Foody' )
win.connect("destroy", Gtk.main_quit)

builder = Gtk.Builder.new_from_string( MENU_XML , -1 )
set_app_menu( builder.get_object( 'app-menu' ) )

win.show_all()
Gtk.main()
