import subprocess

def get_path(path):
    return '"'+path+'"'

def send_commend(fn):
    subprocess.Popen("mpv "+get_path(fn)+" --loop-file=yes --fs --volume=0 --title=wallpaper")

def stop():
    subprocess.Popen("taskkill /f /im mpv.exe")