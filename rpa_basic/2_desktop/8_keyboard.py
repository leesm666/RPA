import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개를 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("12345")
# pyautogui.write("NadoCoding", interval=0.25)
# pyautogui.write("나도코딩")

# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"],interval=0.25) 
# t e s t 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 2번, l a 순서대로 적고 enter 입력

# 특수 문자
# shift 4 -> $ 
# pyautogui.keyDown("shift")
# pyautogui.press("4") # 숫자 4를 입력하고 
# pyautogui.keyUp("shift")

# 조합키 (Hot Key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a") #press("a")
# pyautogui.keyUp("ctral") # Ctrl + A

# 간편한 조합키
# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# ctrt 누름 > Alt 누름 > shift 누름 > A 누름 > A 떼고 >......
# pyautogui.hotkey("ctrl", "a")

import pyperclip
# pyperclip.copy("나도코딩") # "나도코딩" 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl","v") #클립보드에 있는 내용 붙여넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")
    
my_write("아아아르")

# 자동화 프로그램 종료
# win: ctrl + alt + del