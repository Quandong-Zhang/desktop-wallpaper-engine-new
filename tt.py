from win32gui import FindWindow, FindWindowEx, SendMessageTimeout, SendMessage
def find_desktop_hwnd():
    hwnd = FindWindow("Progman", "Program Manager")
    SendMessageTimeout(hwnd, 0x052C, 0, None, 0, 0x03E8)
    hwnd_WorkW = None
    while 1:
        hwnd_WorkW = FindWindowEx(None, hwnd_WorkW, "WorkerW", None)
        if not hwnd_WorkW:
            continue
        hView = FindWindowEx(hwnd_WorkW, None, "SHELLDLL_DefView", None)
        if not hView:
            continue
        h = FindWindowEx(None, hwnd_WorkW, "WorkerW", None)
        while h:
            SendMessage(h, 0x0010, 0, 0); # WM_CLOSE
            h = FindWindowEx(None, hwnd_WorkW, "WorkerW", None)
        break
    return hwnd

if __name__=="__main__":
    print(find_desktop_hwnd())