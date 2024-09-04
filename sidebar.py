from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.app import App
import display_map  # Import the display map

class Sidebar(BoxLayout):
    def __init__(self, **kwargs):
        super(Sidebar, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_x = App.get_running_app().get_sidebar_width()  # Default sidebar width
        self.spacing = display_map.BUTTON_SPACING  # Space between buttons

        # Set background color for the sidebar
        with self.canvas.before:
            Color(0.9, 0.9, 0.9, 1)  # Light grey background
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)

        # Bind size and position to update the background rectangle
        self.bind(size=self._update_bg_rect, pos=self._update_bg_rect)

        # Create buttons for the sidebar
        self.settings_button = Button(size_hint=(None, None), size=(80, 80),
                                      background_normal=r'E:\Files\Projects\project_laze\assets\gear_icon.png')
        self.music_button = Button(size_hint=(None, None), size=(80, 80),
                                   background_normal=r'E:\Files\Projects\project_laze\assets\music-icon.png')
        self.steering_button = Button(size_hint=(None, None), size=(80, 80),
                                      background_normal=r'E:\Files\Projects\project_laze\assets\steering-icon.png')

        # Add buttons to the sidebar
        self.add_widget(self.settings_button)
        self.add_widget(self.music_button)
        self.add_widget(self.steering_button)

        # Scale the buttons and ensure they are centered on initialization
        self.update_button_size(App.get_running_app().get_sidebar_width())
        self.center_buttons()

        # Bind the sidebar width to update button size dynamically when the sidebar size changes
        self.bind(size=self.on_sidebar_resize)

    def _update_bg_rect(self, instance, value):
        """Update the background rectangle to cover the sidebar."""
        self.bg_rect.size = self.size
        self.bg_rect.pos = self.pos

    def update_button_size(self, new_width):
        """Update the button size when the sidebar width changes."""
        button_size = new_width * 800  # Scale buttons with sidebar width
        for button in [self.settings_button, self.music_button, self.steering_button]:
            button.size = (self.width * display_map.BUTTON_SIZE_RATIO, self.width * display_map.BUTTON_SIZE_RATIO)

        # Call center_buttons to ensure buttons are still centered after resizing
        self.center_buttons()

    def center_buttons(self):
        """Center the buttons vertically by adding padding."""
        total_button_height = sum([child.height for child in self.children]) + self.spacing * (len(self.children) - 1)
        available_height = self.height

        # Calculate the vertical padding required to center the buttons
        if available_height > total_button_height:
            vertical_padding = (available_height - total_button_height) / 2
            self.padding = [0, vertical_padding, 0, vertical_padding]  # Top, bottom padding to center
        else:
            # If the sidebar is too small, just remove padding
            self.padding = [0, 0, 0, 0]

        # Ensure buttons are centered horizontally
        for button in [self.settings_button, self.music_button, self.steering_button]:
            button.size_hint = (None, None)
            button.width = self.width * display_map.BUTTON_SIZE_RATIO
            button.height = button.width  # Keep it square
            button.pos_hint = {'center_x': 0.5}  # Center horizontally

    def on_sidebar_resize(self, instance, value):
        """Callback for when the sidebar size changes."""
        self.update_button_size(self.width)  # Update button sizes immediately after sidebar width changes
