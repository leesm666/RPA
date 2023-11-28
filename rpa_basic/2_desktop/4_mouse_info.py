import pyautogui
# pyautogui.FAILSAFE = False # 마우스를 끝에 놔둬도 실행 안멈추는 기능 
pyautogui.PAUSE = 1 #모든 동작에 1초식 sleep 적용
# pyautogui.mouseInfo() #마우스 좌표값, RGB 값 알려주는 유용한 기능

for i in range(10):
    pyautogui.move(100,100)
