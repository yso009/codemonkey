import keyboard
import time
from PIL import ImageGrab



def screenshot():
    curr_time = time.strftime("_%Y-%m-%d_%H-%M-%S")
    img = ImageGrab.grab()
    img.save("image{0}.png".format(curr_time))

keyboard.add_hotkey(".", screenshot)

keyboard.wait("esc")