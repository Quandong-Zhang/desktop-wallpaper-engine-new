import win32gui
#import _thread
import multiprocessing
import lab
#import vid
import api
import time
import pywintypes
from tkinter import filedialog
import tkinter
import tt

def protect():
    pt=multiprocessing.Process(target=protectcallback,args=(pid,))
    pt.start()

def get_boswore_path():
    return filedialog.askopenfilename()

def protectcallback(pid):
    print("233")
    #global pid
    global dshandle
    dshandle = tt.find_desktop_hwnd()
    while 1:#皮一下
        thishandle = tt.find_desktop_hwnd()
        print(thishandle,dshandle)
        #if dshandle != thishandle:
        if 1:
            for handle in pid:
                lab.setson(handle)
        dshandle = thishandle
        time.sleep(5)

def main():
    global pid
    #_thread.start_new_thread( vid.play, ("3.mp4", ) )

    #time.sleep(.5)
    while True:
        if lab.get_jb_id("wallpaper") is None:
            time.sleep(.05)
        else:
            pid = lab.get_jb_id("wallpaper")
            break


    for handle in lab.get_jb_id("wallpaper"):
        lab.setson(handle)

    #protect = multiprocessing.Process(target=protectcallback)
    #protect.start()

#    while True:
#        time.sleep(999999)

def start():
    vidpath = get_boswore_path()
    #maintrade =  multiprocessing.Process(target=main)
    #vplayer = multiprocessing.Process(target=api.send_commend, args=(vidpath,))
    #maintrade.start()
    #vplayer.start()
    api.send_commend(vidpath)
    main()

if __name__=="__main__":
    multiprocessing.freeze_support()
    top = tkinter.Tk()
    top.geometry("400x100")
    B1 = tkinter.Button(top, text ="启动壁纸", command = start)
    B2 = tkinter.Button(top, text ="停止壁纸", command = api.stop)
    B3 = tkinter.Button(top, text="启动win11多桌面兼容进程（不知道干啥的不要乱按（doge））" ,command=protect)
    B1.pack()
    B2.pack()
    B3.pack()
    top.mainloop()