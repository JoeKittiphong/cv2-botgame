import pyautogui as pg
import numpy as np
import cv2, os, random
import setting

accurency = setting.accurency
position = setting.emu_position

def main_screen():
    pg.screenshot().save("./mainscreen/screen.png")

# ทำการเช็คว่าภาพที่ cap ไว้มีตรงกับภาพที่ขึ้นในหน้าจอรึป่าว
def check_img(image, compare_image):
    capture_img = cv2.imread(image)
    screen_img = cv2.imread(compare_image)
    # เทียบโดยใช้วิธี TM_SQDIFF_NORMED
    matching_img = cv2.matchTemplate(capture_img, screen_img,cv2.TM_SQDIFF_NORMED)

    # เลือกเอาตำแหน่งที่มีความใกล้เคียงกันที่สุด    
    filter_img = np.where(matching_img <= 0.03) # 1 = 100%
    # แยกตำแหน่งพิกัด xy แต่ละจุดที่ match กันออกมา
    xy = list(zip(*filter_img[::-1]))
    
    for loc in xy:
        pg.moveTo(loc[0]+random.randint(0,accurency),loc[1]+random.randint(0,accurency))
        pg.click()
        return

# cap หน้าจอจากตำแหน่งต่าง ๆ ที่ระบุไว้
def emu_capture():
    count = len(position)
    for i in range(count):    
        screen = pg.screenshot(region=(position[i]))
        screen.save("{}/{}".format("./screenshot","{}.png".format(i)))

def main():
    test = os.listdir("./compare-image")
    for k in os.listdir("./screenshot"):
        for i in test:
            for j in os.listdir(os.path.join("./compare-image",i)):
                check_image = os.path.join("./compare-image",i,j)
                screen_img = os.path.join("./screenshot",k)
                check_img(check_image, screen_img)

def run():
    main_screen()
    emu_capture()
    main()