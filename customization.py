import os
from kivy.uix.image import Image

class CustomizationManager:
    def __init__(self, screen):
        self.screen = screen

    def set_background(self, image_path):
        if os.path.exists(image_path):
            self.screen.background.source = image_path
        else:
            print(f"Background image {image_path} not found.")
