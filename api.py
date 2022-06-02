import subprocess

def get_path(path):
    return '"'+path+'"'

def send_commend(fn):
    subprocess.Popen("mpv "+get_path(fn)+" --loop-file=yes --fs --title=wallpaperce84aa7d-3cec-4ef8-b6fd-b3d76e56aa20")

def stop():
    subprocess.Popen("taskkill /f /im mpv.exe")