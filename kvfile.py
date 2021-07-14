KV = """
#:import Clipboard kivy.core.clipboard.Clipboard

ScreenManager:
    MainScreen:
        id: mainscreen

<MainScreen>:
    name: 'main'

    BoxLayout:
        orientation: "vertical"

        MDToolbar:
            id: toolbar
            md_bg_color:  [0, 0, 0, 1]

        MDBottomNavigation:
            panel_color: 1, 1, 1, 1
            font_name: 'fonts/Oswald-ExtraLight.ttf'
            
            MDBottomNavigationItem:
                name: 'search_oids'
                text: 'Search'
                icon: 'search-web'
                on_tab_press: app.button_reset_action()

                MDLabel:
                    text: 'Simple Network Management Protocol  OID Finder'
                    font_style: 'H5'
                    font_name: 'fonts/Oswald-Regular.ttf'
                    pos_hint: {'center_y': .95}
                    halign: 'center'

                MDTextField:
                    id: ipaddress
                    adaptive_height: False
                    hint_text: "Type the IP address"
                    mode: "rectangle"
                    input_type: 'text'
                    helper_text: "Example: 127.0.0.1"
                    helper_text_mode: "on_focus"
                    font_name: 'fonts/Oswald-Regular.ttf'
                    icon_right: "pencil"
                    icon_right_color: app.theme_cls.primary_color
                    pos_hint: {'center_x': .4, 'center_y': .81}
                    size_hint_x: .5
                    size_hint_y: .14

                MDRectangleFlatButton:
                    adaptive_height: False
                    text: 'Find'
                    font_size: "16sp"
                    font_name: 'fonts/Oswald-ExtraLight.ttf'
                    pos_hint: {'center_x': .78, 'center_y': .8}
                    size_hint: .15, .1
                    on_press: app.button_find()

                MDBoxLayout:
                    md_bg_color:  [0, 0, 0, 0.1]
                    adaptive_height: False
                    size_hint_y: .6
                    size_hint_x: .9
                    pos_hint: {'center_x': 0.5, 'center_y': .32}
                    
                    ScrollView:
                        do_scroll_x: False
                        do_scroll_y: True
                        MDList:                    
                            id: oiditems

                MDLabel:
                    font_style: 'Body1'
                    font_name: 'fonts/Oswald-Regular.ttf'
                    text: 'Object Identifier List'
                    font_size: "18sp"
                    pos_hint: {'center_x': .55, 'center_y': .69}
                    size_hint_x: 1
                    size_hint_y: None
                    halign: 'left'

                MDLabel:
                    id: oidlist
                    font_style: 'Body1'
                    font_name: 'fonts/Oswald-Regular.ttf'
                    pos_hint: {'center_x': .78, 'center_y': .24}
                    size_hint: .3, .065
                    halign: 'center'                    


            MDBottomNavigationItem:
                name: 'get_oid_value'
                text: 'Get value'
                icon: 'playlist-edit'
                on_tab_press: app.button_reset_action()

                MDLabel:
                    text: 'Get Object Identifier Value'
                    font_style: 'H5'
                    font_name: 'fonts/Oswald-Regular.ttf'
                    pos_hint: {'center_y': .95}
                    halign: 'center'
                
                MDTextField:
                    id: oid_ip
                    adaptive_height: False
                    hint_text: "IP address"
                    mode: "rectangle"
                    input_type: 'text'
                    helper_text: "Example: 127.0.0.1"
                    helper_text_mode: "on_focus"
                    font_name: 'fonts/Oswald-Regular.ttf'
                    icon_right: "pencil"
                    icon_right_color: app.theme_cls.primary_color
                    pos_hint: {'center_x': .16, 'center_y': .81}
                    size_hint_x: .2
                    size_hint_y: .14
                
                MDTextField:
                    id: oid_port
                    adaptive_height: False
                    hint_text: "PORT"
                    mode: "rectangle"
                    input_type: 'text'
                    text: "161"
                    helper_text: "Example: 161"
                    helper_text_mode: "on_focus"
                    font_name: 'fonts/Oswald-Regular.ttf'
                    icon_right: "pencil"
                    icon_right_color: app.theme_cls.primary_color
                    pos_hint: {'center_x': .4, 'center_y': .81}
                    size_hint_x: .16
                    size_hint_y: .14
                
                MDTextField:
                    id: oidaddress
                    adaptive_height: False
                    hint_text: "OID address"
                    mode: "rectangle"
                    input_type: 'text'
                    helper_text: "Example: 1.3.6.1.2.1.1.1.0"
                    helper_text_mode: "on_focus"
                    font_name: 'fonts/Oswald-Regular.ttf'
                    icon_right: "pencil"
                    icon_right_color: app.theme_cls.primary_color
                    pos_hint: {'center_x': .65, 'center_y': .81}
                    size_hint_x: .2
                    size_hint_y: .14

                MDRectangleFlatButton:
                    adaptive_height: False
                    text: 'Get Value'
                    font_size: "16sp"
                    font_name: 'fonts/Oswald-ExtraLight.ttf'
                    pos_hint: {'center_x': .88, 'center_y': .8}
                    size_hint: .15, .1
                    on_press: app.button_get()

                MDBoxLayout:
                    md_bg_color:  [0, 0, 0, 0.1]
                    adaptive_height: False
                    size_hint_y: .5
                    size_hint_x: .9
                    pos_hint: {'center_x': 0.5, 'center_y': .45}
                    
                    ScrollView:
                        do_scroll_x: False
                        do_scroll_y: True

                        MDLabel:
                            id: oidtext
                            font_name: 'fonts/Oswald-Regular.ttf'
                            font_style: 'Body1'
                            height: self.texture_size[1]
                            pos_hint: {'center_y': .95}
                            size_hint_x: 1
                            size_hint_y: None
                            halign: 'left'
                
                MDRectangleFlatButton:
                    text: 'Copy OID Value'
                    font_name: 'fonts/Oswald-ExtraLight.ttf'
                    pos_hint: {"center_x": .5, "center_y": .12}
                    size_hint: .15, .1
                    on_press: Clipboard.copy(oidtext.text) 
            
            MDBottomNavigationItem:
                
                name: 'get_snmp_trap'
                text: 'SNMP Trap'
                icon: 'playlist-edit'
                on_tab_press: app.button_reset_action()

                MDLabel:
                    text: 'SNMP Trap'
                    font_style: 'H5'
                    font_name: 'fonts/Oswald-Regular.ttf'
                    pos_hint: {'center_y': .95}
                    halign: 'center'

                MDLabel:
                    font_style: 'Body1'
                    font_name: 'fonts/Oswald-Regular.ttf'
                    text: 'Response from Client'
                    font_size: "18sp"
                    pos_hint: {'center_x': .13, 'center_y': .85}
                    size_hint_x: 1
                    size_hint_y: None
                    halign: 'left'
                    halign: 'center'

                MDRectangleFlatButton:
                    adaptive_height: False
                    text: 'Start Server'
                    font_size: "16sp"
                    font_name: 'fonts/Oswald-ExtraLight.ttf'
                    pos_hint: {'center_x': .5, 'center_y': .10}
                    size_hint: .15, .1
                    on_press: app.button_trap()

                MDBoxLayout:
                    md_bg_color:  [0, 0, 0, 0.1]
                    adaptive_height: False
                    size_hint_y: .6
                    size_hint_x: .9
                    pos_hint: {'center_x': 0.5, 'center_y': .50}
                    ScrollView:
                        do_scroll_x: False
                        do_scroll_y: True

                        MDLabel:
                            id: traptext
                            font_name: 'fonts/Oswald-Regular.ttf'
                            font_style: 'Body1'
                            height: self.texture_size[1]
                            pos_hint: {'center_y': .95}
                            size_hint_x: 1
                            size_hint_y: None
                            halign: 'left'
                
"""