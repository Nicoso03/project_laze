from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.app import App
from sidebar import Sidebar

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
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
        self.sidebar.size_hint_x = App.get_running_app().get_sidebar_width()
        layout.add_widget(self.sidebar)

        # Bind sidebar settings button to go back to the main screen
        self.sidebar.settings_button.bind(on_press=self.go_back_to_main)

        # Create buttons for Screen, Dash, and General settings
        self.screen_button = Button(text='Screen', size_hint=(None, None), size=(200, 100),
                                    pos_hint={'center_x': 0.5, 'y': 0.7},
                                    on_press=self.open_screen_popup)
        layout.add_widget(self.screen_button)

        self.dash_button = Button(text='Dash', size_hint=(None, None), size=(200, 100),
                                  pos_hint={'center_x': 0.5, 'y': 0.5},
                                  on_press=self.open_dash_popup)
        layout.add_widget(self.dash_button)

        self.general_button = Button(text='General', size_hint=(None, None), size=(200, 100),
                                     pos_hint={'center_x': 0.5, 'y': 0.3},
                                     on_press=self.open_general_popup)
        layout.add_widget(self.general_button)

        # Add a back button to return to the main screen
        self.back_button = Button(text='Back', size_hint=(None, None), size=(200, 100),
                                  pos_hint={'center_x': 0.5, 'y': 0.1},
                                  on_press=self.go_back_to_main)
        layout.add_widget(self.back_button)

        self.add_widget(layout)

    def open_screen_popup(self, instance):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Add a label for the slider's value
        self.slider_value_label = Label(text=f'Sidebar Width: {App.get_running_app().get_sidebar_width():.2f}')
        popup_layout.add_widget(self.slider_value_label)

        # Fetch the sidebar width from the App instance
        sidebar_width = App.get_running_app().get_sidebar_width()

        # Add a slider to adjust the sidebar width
        self.sidebar_slider = Slider(min=0.04, max=0.14, value=sidebar_width, step=0.01)
        self.sidebar_slider.bind(value=self.on_slider_value_change)
        popup_layout.add_widget(self.sidebar_slider)

        # Create and open the popup
        self.screen_popup = Popup(title='Screen Settings', content=popup_layout,
                                  size_hint=(0.8, 0.8), auto_dismiss=True)
        self.screen_popup.bind(on_dismiss=self.apply_sidebar_width)  # Apply sidebar width when closing popup
        self.screen_popup.open()

    def on_slider_value_change(self, instance, value):
        self.slider_value_label.text = f'Sidebar Width: {value:.2f}'

    def apply_sidebar_width(self, instance):
        new_width = self.sidebar_slider.value
        App.get_running_app().update_sidebar_width(new_width)

        # Update the sidebar width in the settings screen
        self.sidebar.size_hint_x = new_width
        self.sidebar.update_button_size(new_width)  # Adjust the sidebar button size

        # Notify MainScreen to update its sidebar width dynamically
        main_screen = self.manager.get_screen('main')
        main_screen.update_sidebar_width(new_width)

    def open_dash_popup(self, instance):
        dash_popup = Popup(title='Dash Settings', content=Label(text='Dash settings options here'),
                           size_hint=(0.8, 0.8), auto_dismiss=True)
        dash_popup.open()

    def open_general_popup(self, instance):
        general_popup = Popup(title='General Settings', content=Label(text='General settings options here'),
                              size_hint=(0.8, 0.8), auto_dismiss=True)
        general_popup.open()

    def go_back_to_main(self, instance):
        # Go back to the main screen when pressing the settings icon or back button
        print("Returning to main screen")
        self.manager.current = 'main'
