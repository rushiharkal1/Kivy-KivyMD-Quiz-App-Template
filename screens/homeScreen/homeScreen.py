from kivymd.uix.screen import MDScreen
import webbrowser

# Importing MenuScreen
from screens.menuScreen.menuScreen import MenuScreen

class HomeScreen(MDScreen):
    
    def load_Menu_Screen(self):
         self.manager.current = 'menuScreenPage'
         
         
    def switch_theme_style(self):
        #self.theme_cls.primary_palette = (
        # "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
        # )
         
        self.theme_cls.theme_style = (
         "Dark" if self.theme_cls.theme_style == "Light" else "Light"
         )
         
    def open_GitHub_Repo(self):
        print("open")
        webbrowser.open("https://github.com/rushiharkal1/Kivy-KivyMD-Quiz-App-Template")