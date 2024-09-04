from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
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
        self.sidebar.steering_button.bind(on_press=self.toggle_steering_popup)

        # Music Popup Window (initially hidden)
        self.music_popup = Popup(title='Music Player',
                                 content=Label(text='Music Player Interface'),
                                 size_hint=(0.8, 0.8),
                                 auto_dismiss=True)  # auto_dismiss=True allows clicking outside to close
        self.music_popup_open = False  # Track if the popup is open

        # Steering Popup Window (initially hidden)
        self.steering_popup = Popup(title='Steering Controls',
                                    content=Label(text='Steering Control Interface'),
                                    size_hint=(0.8, 0.8),
                                    auto_dismiss=True)  # auto_dismiss=True allows clicking outside to close
        self.steering_popup_open = False  # Track if the popup is open

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
        if self.music_popup_open:
            self.close_music_popup()
        else:
            self.open_music_popup()

    def open_music_popup(self):
        # Open the music popup
        self.music_popup.open()
        self.music_popup_open = True
        self.music_popup.bind(on_dismiss=self.on_music_popup_dismiss)

    def close_music_popup(self):
        # Close the music popup
        self.music_popup.dismiss()

    def on_music_popup_dismiss(self, instance):
        # Handle when the popup is dismissed
        self.music_popup_open = False

    def toggle_steering_popup(self, instance):
        # Toggle the steering controls popup
        if self.steering_popup_open:
            self.close_steering_popup()
        else:
            self.open_steering_popup()

    def open_steering_popup(self):
        # Open the steering controls popup
        self.steering_popup.open()
        self.steering_popup_open = True
        self.steering_popup.bind(on_dismiss=self.on_steering_popup_dismiss)

    def close_steering_popup(self):
        # Close the steering controls popup
        self.steering_popup.dismiss()

    def on_steering_popup_dismiss(self, instance):
        # Handle when the steering popup is dismissed
        self.steering_popup_open = False
