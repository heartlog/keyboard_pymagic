# @royal78 Telegrm - t.me/diablo_13N
from pynput.keyboard import Key, Listener
import winsound
import random
# on each keyboard clock the sound will randomly change ...
# all files are given
sounds = ['AH.wav', 'AhH.wav', 'eeYAH.wav', 'iiYAH.wav', 'OH.wav', 'eghng.wav']

def on_press(key):
    sound()

def sound():
    winsound.PlaySound(random.choice(sounds), winsound.SND_ASYNC)

def on_release(key):
    print('{0} release'.format(
        key))

# Collect events until released and trigger a action
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
