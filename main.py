from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config
from gui import MainScreen
from settings import SettingsScreen

# Lock screen size to 1024x600
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', False)

class EntertainmentApp(App):
    def __init__(self, **kwargs):
        super(EntertainmentApp, self).__init__(**kwargs)
        self.sidebar_width = 0.1  # Default width for sidebar

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm

    def get_sidebar_width(self):
        return self.sidebar_width

    def set_sidebar_width(self, width):
        self.sidebar_width = width

    def update_sidebar_width(self, new_width):
        """Update the sidebar width globally."""
        self.sidebar_width = new_width

if __name__ == '__main__':
    EntertainmentApp().run()
