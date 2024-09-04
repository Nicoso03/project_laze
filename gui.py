from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from sidebar import Sidebar

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        # Fetch the global sidebar width from the App instance
        self.sidebar_width = App.get_running_app().get_sidebar_width()

        layout = FloatLayout()

        # Load default background
        self.background = Image(source=r'E:\Files\Projects\project_laze\assets\background.jpg',
                                allow_stretch=True,
                                keep_ratio=False,
                                size_hint=(1, 1),
                                pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(self.background)

        # Add the sidebar to the screen
        self.sidebar = Sidebar()
        self.sidebar.size_hint_x = self.sidebar_width  # Set initial size based on global width
        layout.add_widget(self.sidebar)

        # Bind sidebar buttons to their respective actions
        self.sidebar.settings_button.bind(on_press=self.open_settings)
        self.sidebar.music_button.bind(on_press=self.toggle_music_popup)
        self.sidebar.steering_button.bind(on_press=self.open_steering_controls)

        self.add_widget(layout)

    def update_sidebar_width(self, width):
        # Update the sidebar width based on the global value
        self.sidebar_width = width
        self.sidebar.size_hint_x = width  # Update the size of the sidebar dynamically

        # Scale buttons accordingly inside the sidebar
        self.sidebar.update_button_size(width)

    def open_settings(self, instance):
        # Open the settings screen
        self.manager.current = 'settings'

    def toggle_music_popup(self, instance):
        # Toggle the music player popup
        print("Toggling music player...")

    def open_steering_controls(self, instance):
        # Open steering controls or related screen
        print("Opening steering controls...")
