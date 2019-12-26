from time import sleep
import sys
import gi
from gi.repository import Gdk
import pyautogui as pag
gi.require_version("Gtk", "3.0")


def PixelAt(x, y):
    w = Gdk.get_default_root_window()
    pb = Gdk.pixbuf_get_from_window(w, x, y, 1, 1)
    return pb.get_pixels()


# print(tuple(PixelAt(int(sys.argv[1]), int(sys.argv[2]))))


# while True:
#     x, y = pag.position()
#     print(str(x) + ", " + str(y))

# left_x, left_y = 488, 989
# right_x, right_y = 733, 990
left_x, left_y = 192, 1007
right_x, right_y = 462, 1012


# while(True):
# print(tuple(PixelAt(453, 1007)), tuple(PixelAt(743, 1004)))
# print(tuple(PixelAt(488, 989)), tuple(PixelAt(733, 990)))
# print(tuple(PixelAt(left_x, left_y)), tuple(PixelAt(right_x, right_y)))


pag.moveTo(left_x, left_y)


def isPink(t):
    x, y, z = t[0], t[1], t[2]
    if x >= 250 and y >= 15 and y <= 25 and z >= 250:
        return True
    else:
        return False


def isCyan(t):
    x, y, z = t[0], t[1], t[2]
    if x >= 15 and y >= 182 and z >= 180:
        return True
    else:
        return False


while True:
    if isPink(PixelAt(left_x, left_y)):
        # pag.moveTo(left_x, left_y)
        pag.click(left_x, left_y)
        sleep(0.06)
    elif isPink(PixelAt(right_x, right_y)):
        pag.click(right_x, right_y)
        sleep(0.06)
    elif isCyan(PixelAt(left_x, left_y)):
        pag.click(left_x, left_y)
        sleep(0.03)
    # print(tuple(PixelAt(left_x, left_y)), tuple(PixelAt(right_x, right_y)))
