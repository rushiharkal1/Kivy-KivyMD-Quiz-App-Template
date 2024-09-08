from kivy.config import Config
Config.set('graphics', 'width', '375')
Config.set('graphics', 'height', '650')

from kivymd.app import MDApp

# importing homeScreen
from screens.homeScreen.homeScreen import HomeScreen


## Main Class of KivyMD App
class MainApp(MDApp):
    
    ## KivyMD build function
    def build(self):
        self.title = 'KivyMD Quiz App'

    
    ## KivyMD on_start function
    def on_start(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "White"
        self.root.current = 'homeScreenPage'
        
  
## Starting App  
if __name__ == '__main__':
    MainApp().run()