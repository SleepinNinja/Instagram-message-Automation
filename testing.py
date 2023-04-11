from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def start_messaging(user_nme, pas, message):
	keyboard = Controller()
	print(user_nme,  type(user_nme))
	driver = webdriver.Firefox()
	driver.get("https://www.instagram.com")

	try:
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")))

	finally:
		user_name = driver.find_element_by_name("username")
		password = driver.find_element_by_name("password")
		submit_button = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")

		user_name.clear()
		password.clear()

		user_name.send_keys("yaakovchikin")
		password.send_keys("y@@kovchikin")
		submit_button.click()

	while True:
		not_now_button_wait = WebDriverWait(driver, 10)
		not_now_button = not_now_button_wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")))

		if not_now_button:
			break

	not_now = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
	not_now.click()

	while True:
		off_notification_button_wait = WebDriverWait(driver, 10)
		off_notification_button = off_notification_button_wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]")))
		
		if off_notification_button:
			break


	off_notification = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
	off_notification.click()

	while True:
		inbox_wait = WebDriverWait(driver, 10)
		inbox = inbox_wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a")))
		
		if inbox:
			break

	inbox.click()
	time.sleep(3)

	chat_count = driver.find_elements_by_class_name("_7UhW9.xLCgt.MMzan.KV-D4.fDxYl")
	print(len(chat_count))
	chat_id_list = [chat.text for chat in chat_count]
	print(set(chat_id_list))

	for chat_id in set(chat_id_list):

		while True:
			message_button_check = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "wpO6b.ZQScA"))) 
			print(bool(message_button_check))

			if message_button_check:
				break

		message_button = driver.find_element_by_class_name("wpO6b.ZQScA")
		message_button.click()

		while True:
			chat_search_check = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "j_2Hd.uMkC7.M5V28"))) 

			if chat_search_check:

				break
		chat_search = driver.find_element_by_class_name("j_2Hd.uMkC7.M5V28")
		chat_search.clear()
		chat_search.send_keys(chat_id)

		time.sleep(3)
		
		while True:
			first_result_check = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "Igw0E.rBNOH.eGOV_.ybXk5._4EzTm.XfCBB.HVWg4")))

			if first_result_check:
				break

		f_result = driver.find_element_by_class_name("Igw0E.rBNOH.eGOV_.ybXk5._4EzTm.XfCBB.HVWg4")
		f_result.click()

		time.sleep(3)
			
		next_button = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/div/button")
		next_button.click()

		time.sleep(3)

		while True:
			message_box_check = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))

			if message_box_check:
				break

		message_box = driver.find_element_by_tag_name("textarea")
		message_box.click()
		message_box.clear()
		message_box.send_keys("test_message_2")
		time.sleep(2)

		message_box.send_keys(Keys.RETURN)
		time.sleep(2)


start_messaging(1123, 445, 5454)
				


	                                                              