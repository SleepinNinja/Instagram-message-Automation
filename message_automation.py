from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def check_is_available(driver, query):
	count = 0

	while True:
		if count > 3:
			break

		try:
			element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((query[0], query[1])))

		except:
			time.sleep(3)
			continue

		else:
			usable_element = driver.find_element(query[0], query[1])
			break

		count += 1

	if count == 4:
		driver.close()

	return usable_element


def start_messaging(user_nme, pswd, message):
	driver = webdriver.Firefox()
	driver.get("https://www.instagram.com")

	username = check_is_available(driver, (By.NAME, "username"))
	password = check_is_available(driver, (By.NAME, "password"))
	login_button = check_is_available(driver, (By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button"))

	username.clear()
	password.clear()

	username.send_keys(user_nme)
	password.send_keys(pswd)
	login_button.click()

	not_now_button = check_is_available(driver, (By.XPATH, "/html/body/div[6]/div/div/div/div[3]/button[2]"))
	not_now_button.click()

	off_notification_button = check_is_available(driver, (By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]"))
	off_notification_button.click()

	inbox_button = check_is_available(driver, (By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a"))
	inbox_button.click()

	time.sleep(3)

	chat_count = driver.find_elements_by_class_name("_7UhW9.xLCgt.MMzan.KV-D4.fDxYl")
	chat_id_list = []
	done_id_list = []

	for chat in chat_count:
		if chat.text not in chat_id_list:
			chat_id_list.append(chat.text)

	id_index = 0

	while len(done_id_list) != len(chat_id_list):

		if chat_id_list[id_index] not in done_id_list:
			done_id_list.append(chat_id_list[id_index])

			message_button = check_is_available(driver, (By.CLASS_NAME, "wpO6b.ZQScA"))
			message_button.click()

			chat_search_button = check_is_available(driver, (By.CLASS_NAME, "j_2Hd.uMkC7.M5V28"))
			chat_search_button.clear()
			chat_search_button.send_keys(done_id_list[-1])

			time.sleep(3)

			first_result = check_is_available(driver, (By.CLASS_NAME, "Igw0E.rBNOH.eGOV_.ybXk5._4EzTm.XfCBB.HVWg4"))
			first_result.click()

			time.sleep(2)

			next_button = check_is_available(driver, (By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div[2]/div/button"))
			next_button.click()

			time.sleep(2)

			message_box = check_is_available(driver, (By.TAG_NAME, "textarea"))

			time.sleep(1)

			message_box.clear()
			message_box.send_keys(message)

			time.sleep(1)

			message_box.send_keys(Keys.RETURN)

			time.sleep(2)


		id_index += 1

		if id_index == len(chat_id_list):
			id_index = 0

	time.sleep(10)
	driver.close()
	return 1
