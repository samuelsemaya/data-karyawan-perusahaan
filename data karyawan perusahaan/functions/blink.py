import sys
import time
import msvcrt

def blink_text(text):
    stop = False
    while not stop:
        sys.stdout.write('\033[5m' + text + '\033[0m')
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()
        time.sleep(0.5)
        
        if msvcrt.kbhit():
            key = msvcrt.getch().decode("utf-8")
            if key == 'q':  # Press 'q' to break out of the loop
                stop = True
