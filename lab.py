import win32gui
import tt

def get_jb_id(title):
    '''
    根据标题找句柄
    :param title: 标题
    :return:返回句柄所对应的ID
    '''
    jh = []
    hwnd_title = dict()

    def get_all_hwnd(hwnd, mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if t:
            if title in t:
                jh.append(h)

    if len(jh) == 0:
        print("壁纸启动中")
    else:
        return jh

def setson(sonid):
    #son=2099386
    #father=3475208
    #t.main()
    #father=t.e
    #global father
    #global sonid_list
    #sonid_list.append(sonid)
    father=tt.find_desktop_hwnd()
    win32gui.SetParent(sonid,father)

if __name__=="__main__":
    print(get_jb_id("wallpaper"))
    print(win32gui.FindWindow("StandardFrame_DingTalk", "钉钉"))