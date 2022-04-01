import win32gui

def hd(hwnd,n):
    global e
    global p
    if win32gui.GetWindowText(hwnd) =="Program Manager":
        e=p
        print(p)
        return p
        #print(n,hwnd,win32gui.GetWindowText(hwnd))
    p = hwnd

def main():
    win32gui.EnumWindows(hd, 0)
