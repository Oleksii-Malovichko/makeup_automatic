import pyautogui
import keyboard
from time import sleep
import pyperclip

x1 = 618
x2 = 935
x3 = 1252
x4 = 1569
# y = 444
y = 432
trash = (1243, 346)
url_position = (369, 95)
remove_page = (494, 56)
quantity_item_position = (843, 351)
buy = (1548, 705)
add = (884, 350)
arr_info = []
q_item = 0
position_remove_trash = (1241, 350)

add_exception = (884, 324)
quantity_item_position_exception = (843, 332)
trash_exception = (1243, 330)


quantity_item_position_exception1 = (843, 302)
trash_exception1 = (1237, 302)
trash_exception1_to_delete = (1242, 320)
quantity_item_position_exception_not_discount = (838, 491)

def write_q_item(q_item):
	with open("/home/alex/makeup_project/q_items", 'a') as f:
		f.write(str(q_item)+'\n')

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
		return (item)
	return item

def has_item():
	position = (1365, 761) # позиция слова "есть" 
	word = copy_elem(position)
	if (word == "Есть"):
		return (1)
	return(0)

def clean_page():
	global remove_page
	pyautogui.click(remove_page)

def click_plus(add, q):
	i = 0
	while (i < q):
		if keyboard.is_pressed('esc'):
			write_q_item(q_item)
			exit(1)
		pyautogui.click(add)
		sleep(0.5)
		i+=1
	
def click_trash_exception(i_sum):
	while (i_sum >= 0):
		if keyboard.is_pressed('esc'):
			write_q_item(q_item)
			exit(1)
		sleep(0.5)
		pyautogui.click(trash_exception)
		i_sum-=1

def click_trash_exception2(temp, trash_ko):
	while (temp >= 0):
		if keyboard.is_pressed('esc'):
			write_q_item(q_item)
			exit(1)
		sleep(0.5)
		pyautogui.click(trash_ko)
		temp-=1

def find_q_elems_exception():
	i_sum = 0
	n = 5
	temp = 0
	num_before = 1
	while (True):
		if keyboard.is_pressed('esc'):
			write_q_item(q_item)
			exit(1)
		click_plus(add_exception, 10)
		sleep(2.5)
		i_sum = copy_elem(quantity_item_position_exception) # !!!!!!!!!!!!!!!!!!!!!
		print("This is func find_q_elems_exception")
		print("this i_sum in exception: "+str(i_sum))
		print("this is num_before: " + str(num_before) + "\nthis is i_sum: " + str(i_sum))
		if (i_sum == "None"):
			print("This is main condition in find_q_elems_exception")
			i_sum = copy_elem(quantity_item_position_exception1)
			if (i_sum == "None"):
				return (find_q_elems((879, 372), (834, 376),(1239, 376)))
			temp = int(i_sum)
			print(temp)
			i_sum = copy_elem(quantity_item_position_exception_not_discount)
			print(i_sum)
			temp += int(i_sum)
			pyautogui.click(trash_exception1)
			print("this is temp: "+ str(temp))
			sleep(5)
			click_trash_exception2(int(i_sum), trash_exception1_to_delete)
			click_trash_exception2(int(i_sum), trash)
			pyautogui.click(1238, 355)
			clean_page()
			return (str(temp))

		if (num_before >= int(i_sum) or n > int(i_sum)):
			sleep(3)
			click_trash_exception(int(i_sum))
			pyautogui.click(trash)
			clean_page()
			return (i_sum)
		n+=5
		num_before = int(i_sum)
	

def find_q_elems(add, quantity_item_position, trash):
	i_sum = 0
	n = 5
	num_before = 0
	while (True):
		# pyautogui.click(add) # добавить товар (кнопка +)
		if keyboard.is_pressed('esc'):
			write_q_item(q_item)
			exit(1)
		click_plus(add, 10)
		sleep(1.5)
		i_sum = copy_elem(quantity_item_position) # !!!!!!!!!!!!!!!!!!!!!
		print("This is func find_q_elems")
		if (i_sum == "None1"):
			return (find_q_elems_exception())
		print("this is num_before: " + str(num_before) + "\nthis is i_sum: " + str(i_sum))
		if (num_before >= int(i_sum) or n > int(i_sum)):
			sleep(3)
			pyautogui.click(trash)
			clean_page()
			return (i_sum)
		n+=5
		num_before = int(i_sum)

def write_to_file():
	s = '\t'.join(arr_info)
	with (open('/home/alex/makeup_project/result', 'a')) as f:
		f.write(s+'\n')
		arr_info.clear()
		return

def go_to_buy(x, y):
	pyautogui.click(x, y, button="right")
	if (q_item % 4 == 0):
		pyautogui.click(x-29,y+20) # если окно для открытия ссылки слева (только с каждым 4-м элементом)
	else:
		pyautogui.click(x+29,y+20) 
	sleep(5)
	pyautogui.hotkey('ctrl','tab')
	sleep(2)
	arr_info.append(copy_elem(url_position))
	sleep(2)
	# проверить, есть ли товар в наличии
	if (has_item() == 0):
		arr_info.append("Нет в наличии")
		write_to_file()
		clean_page()
		return
	pyautogui.click(buy) # кнопка купить
	sleep(2)

	i_sum = find_q_elems(add, quantity_item_position, trash)
	if (i_sum == "None"):
		print("None")
		return
	arr_info.append(i_sum)
	write_to_file()
	

def buy_item():
	global x1, x2, x3, x4, y, q_item
	sleep(1)
	if (q_item == 72):
		q_item+=2
		sleep(0.5)
		q_item+=1
		go_to_buy(x3,y)
		print(q_item)
		q_item+=1
		sleep(0.5)
		go_to_buy(x4,y)
		print(q_item)
		sleep(0.5)
		return 
	
	q_item+=1
	go_to_buy(x1,y)
	print(q_item)
	q_item+=1
	sleep(0.5)
	go_to_buy(x2,y)
	print(q_item)
	# if (q_item == 34): # первый баннер (справа)
	if (q_item == 34): # 36
		q_item+=2
		return 
	q_item+=1
	sleep(0.5)
	go_to_buy(x3,y)
	print(q_item)
	q_item+=1
	sleep(0.5)
	go_to_buy(x4,y)
	print(q_item)
	sleep(0.5)

def check_item():
	pass

press_q = 0
def scroll_screen_buy(q):
	i = 0
	while (i < q):
		if keyboard.is_pressed('esc'):
			write_q_item(q_item)
			exit(1)
		sleep(1)
		buy_item()
		sleep(1)
		pyautogui.press('down', presses=14)
		sleep(1)
		buy_item()
		sleep(1)
		pyautogui.press('down', presses=13)
		sleep(1)
		buy_item()
		sleep(1)
		pyautogui.press('down', presses=14)
		i+=1

def scroll_screen_check(q):
	i = 0
	while (i < q):
		if keyboard.is_pressed('esc'):
			write_q_item(q_item)
			exit(1)
		sleep(1)
		pyautogui.press('down', presses=14)
		sleep(1)
		buy_item()
		sleep(1)
		pyautogui.press('down', presses=13)
		sleep(1)
		buy_item()
		sleep(1)
		pyautogui.press('down', presses=14)
		sleep(1)
		buy_item()
		i+=1



def main():

	try: 
		while True:
			if keyboard.is_pressed('esc'):
				write_q_item(q_item)
				exit(1)
			sleep(1)
			pyautogui.hotkey('alt','tab') # фиксированная локация баннеров
			sleep(3)
			
			# sleep(5)
			scroll_screen_buy(7)
			pyautogui.press('down', presses=4) # вернуть точку
			scroll_screen_buy(9)
			pyautogui.press('down', presses=14) # последний товар в наличии

			sleep(5)
			scroll_screen_check(6)
	except KeyboardInterrupt:
		print("Принудительная остановка")

if __name__ == "__main__":
	main()


""" 
Увлажняющая маска для лица с овсом """