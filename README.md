# cv2-botgame
ทำบอท auto click ด้วย pyautogui และ opencv

### - ติดตั้ง python3 ให้เรียบร้อย
[python3](https://www.python.org/downloads/)

### - ดับเบิ้ลคลิ้ก init.bat
ทำการเตรียมสภาพแวดล้อมต่าง ๆ ให่เหมาะกับการใช้งาน
- สร้างโฟลเด้อร์ต่าง ๆ ที่ต้องใช้
- สร้าง venv สำหรับ python

### - ลง library ต่างสหรับ python
  ``pip install opencv-python pyautogui``

***
### - setting ตำแหน่งที่จะให้บอททำงาน
- ในไฟล์ setting.py ทำการแก้ไขค่า `emu_position = [
    [0,0,600,400],
    [0,0,200,200],
    [0,0,300,300],
    [0,0,400,400],
    [0,0,200,400]
]` [0,0,600,400] ==> [x-start, y-start, x-end, y-end]
- การหาตำแหน่งหน้าทำได้โดย กดปุ่ม window พิมพ์ `cmd` กด enter พิมพ์ `python mouse_position.py`
