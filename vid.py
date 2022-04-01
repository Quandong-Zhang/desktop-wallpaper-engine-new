from moviepy.editor import *
import pygame
 
def play(vname):
    cilp= VideoFileClip(vname)
    pygame.display.set_caption("wallpaper")
    pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    while True:
        cilp.preview()
 
#cap.release()
#cv2.destroyAllWindows()

if __name__=="__main__":
    pass