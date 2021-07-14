# -*- coding: utf-8 -*-
import os
from datetime import datetime
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import ThreeLineListItem
from kivy.clock import Clock

from kivy.lang import Builder
from pysnmp.proto.rfc1902 import IpAddress

from src.OidFinder import OidFinder
from src.SNMP import SNMP
from kvfile import *
import threading

from kivy.core.window import Window
Window.size = (900, 600)



class MainScreen(Screen):
    pass

class AddItemScreen(Screen):
    pass


class RedesApp(MDApp):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.oidFinder = OidFinder()
        self.snmp = SNMP()

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.primary_hue = "A700"


        self.screen = Builder.load_string(KV)

    def build(self):
        return self.screen
    

    def on_start(self):

        print("Application started")

    def button_find(self):
        
        ipAddress = str(self.root.ids.mainscreen.ids.ipaddress.text)
        self.root.ids.mainscreen.ids.oid_ip.text = ipAddress
        try:
            oid_list = self.oidFinder.getList(ipAddress)
        except:
            self.show_data("Error while getting OID list")
            return
        self.update_oid_items(oid_list)

    def button_get(self):
        ip = self.root.ids.mainscreen.ids.oid_ip.text

        try:
            port = int(self.root.ids.mainscreen.ids.oid_port.text)
        except:
            self.show_data("PORT must be a integer")
            return
        
        oid = self.root.ids.mainscreen.ids.oidaddress.text
        response = self.snmp.send_request(oid, ip, port)
        self.root.ids.mainscreen.ids.oidtext.text = str(response)
        

    def button_reset_action(self):
        pass
        # self.root.ids.mainscreen.ids.ipaddress.text = ""
        # self.root.ids.mainscreen.ids.oiditems.clear_widgets()

    def update_oid_items(self, oid_list):
        self.root.ids.mainscreen.ids.oiditems.clear_widgets()

        ITEM = '''
OneLineAvatarIconListItem:
    text: "[font=fonts/Oswald-Regular.ttf]{itemname}[/font]"
    font_name: 'fonts/Oswald-ExtraLight.ttf'

    IconRightWidget:
        icon: "content-copy"
        name: '{name}'
        on_press: Clipboard.copy(self.name) 
'''
        for line, oid in oid_list:
            c_item = ITEM.format(itemname=line, name=oid)
            listitem = Builder.load_string(c_item)
            self.root.ids.mainscreen.ids.oiditems.add_widget(listitem)

    def button_trap(self):
        print("Esperando joao")

        # response = self.trap_server()
        # self.root.ids.mainscreen.ids.traptext.text = str(response)


    def show_data(self, text):

        self.dialog = MDDialog(title="[font=fonts/Oswald-Regular.ttf]Informação[/font]",
                            size_hint=[0.8, 0.4],
                            text=f"[font=fonts/Oswald-ExtraLight.ttf]{text}[/font]",
                            buttons=[MDFlatButton(text='Fechar',
                                                    font_name='fonts/Oswald-ExtraLight.ttf',
                                                    on_release=self.close_dialog)])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

RedesApp().run()