import os
import time

class DebugLogger:
    def __init__(self, log_folder='debug'):
        self.log_folder = log_folder
        self.touch_log_path = os.path.join(log_folder, 'touch_log.txt')
        self.screen_log_path = os.path.join(log_folder, 'screen_log.txt')

        # Ensure the log directory exists
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        # Clear previous logs on startup (optional)
        self.clear_logs()

    def log_touch(self, button_name):
        """Log button press with timestamp."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open(self.touch_log_path, 'a') as log_file:
            log_file.write(f"[{timestamp}] Button Pressed: {button_name}\n")

    def log_screen_transition(self, from_screen, to_screen):
        """Log screen transition with timestamp."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open(self.screen_log_path, 'a') as log_file:
            log_file.write(f"[{timestamp}] Screen Transition: {from_screen} -> {to_screen}\n")

    def clear_logs(self):
        """Clear previous logs (optional)."""
        open(self.touch_log_path, 'w').close()
        open(self.screen_log_path, 'w').close()
