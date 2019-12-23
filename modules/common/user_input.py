from pynput import keyboard
import input


def on_press(key):
    try:
        input.user_input = key.char
        return False
    except AttributeError as ex:
        print()


def on_release(key):
    if key == keyboard.Key.esc:
        input.user_input = "esc"
        return False


def wait_for_user_input():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()
