from pynput.keyboard import Key, Listener
import winsound
import random

sounds = ['AH.wav', 'AhH.wav', 'eeYAH.wav', 'iiYAH.wav', 'OH.wav', 'eghng.wav']

def on_press(key):
    sound()

def sound():
    winsound.PlaySound(random.choice(sounds), winsound.SND_ASYNC)

def on_release(key):
    print('{0} release'.format(
        key))

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
