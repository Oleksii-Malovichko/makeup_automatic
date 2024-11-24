import pyautogui
import pyperclip
from time import sleep

def copy_elem(position):
	item_before = pyperclip.paste()
	print("This is the old item from copy_elem "+item_before)
	pyautogui.doubleClick(position)
	pyautogui.hotkey('ctrl', 'c')
	sleep(0.5)
	item = pyperclip.paste()
	print("This is the item from copy_elem "+item)
	if (item == ""):
		return ("None1")
	if (item == item_before):
		print("from copy_elem: None")
		return ("None")
	return item

item_before = pyperclip.paste()
print(item_before)