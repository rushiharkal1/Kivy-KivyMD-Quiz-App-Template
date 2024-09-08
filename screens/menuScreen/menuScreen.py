from kivymd.uix.screen import MDScreen

class MenuScreen(MDScreen):
    
    def switch_theme_style(self):
        #self.theme_cls.primary_palette = (
        # "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
        # )
         
        self.theme_cls.theme_style = (
         "Dark" if self.theme_cls.theme_style == "Light" else "Light"
         )
         