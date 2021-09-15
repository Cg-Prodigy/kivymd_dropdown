from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.menu import MDDropdownMenu


class Menus(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        drop_items=[
            {
            'viewclass':'OneLineListItem',
            'text':f'{i}',
            'on_release':lambda x=f'{i}':self.switch_screens(x)
            }for i in ['Sign Up','Login']
        ]

        self.drop_menu=MDDropdownMenu(
            items=drop_items,
            width_mult=4
        )
    
    def open_drop(self,btn):
        self.drop_menu.caller=btn
        self.drop_menu.open()
    
    def switch_screens(self,txt):
        self.drop_menu.dismiss()