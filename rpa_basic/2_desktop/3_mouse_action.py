import pyautogui

pyautogui.sleep(3) # 3초 대기
# print(pyautogui.position())

# pyautogui.click(64,17, duration=1) # 이 좌표를 마우스 클릭
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# pyautogui.click(clicks=500)

# 드래그 
# pyautogui.moveTo(200,200)
# pyautogui.mouseDown() # 마우스 버튼 누른 상태
# pyautogui.moveTo(300,300)
# pyautogui.mouseUp() # 마우스 버튼 뗀 상태

# 마우스 오른쪽 버튼 클릭 
# pyautogui.rightClick()
# 마우스 휠 클릭
# pyautogui.middleClick()

# print(pyautogui.position())
# pyautogui.moveTo(1329,269)
# pyautogui.drag(100,0) # 현재 위치 기준으로 x 100 만큼 이동
# pyautogui.drag(100,0, duration=0.25) # 너무 빠른 동작으로 drag 수행이 안될때는 duration 설정
# pyautogui.dragTo(1614,269, duration=0.25) # 절대 좌표 기준으로 x, y 값 이동

pyautogui.scroll(-800) # 양수이면 위 방향으로, 음수이면 아래 방향으로 300만큼 스크롤