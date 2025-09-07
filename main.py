import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import subprocess
import json
import os
import sys

def test():
    print("TEST PASSED")

def check_exists_by_xpath(webdriver, xpath):
    try:
        webdriver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_id(webdriver,ID):
    try:
        webdriver.find_element(By.ID, ID)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_class(webdriver,Class):
    try:
        webdriver.find_element(By.CLASS_NAME, Class)
    except NoSuchElementException:
        return False
    return True

def upload_image():
    #usage: python main.py <file_path> <message>
    file_path = sys.argv[1]
    message = sys.argv[2]
    user_nsec = os.environ['USER_NSEC']
    
    servico=Service(ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("prefs", {"profile.default_content_setting_values.clipboard": 1})

    navegador=webdriver.Chrome(service=servico, options=options)

    regional_settings = {
        'enter_button': 'Entrar',
	    'config_button': 'Configurações',
	    'post_settings': 'Configurações de Postagem',
	    'cancel_button': 'Cancelar'
	}

    navegador.get("https://jumble.social/")
    navegador.set_window_size(1024, 768)
    wait = WebDriverWait(navegador, 20) # waits for a maximum of 10 seconds
	
	#Login Page
    for x in range(10):
        if check_exists_by_xpath(navegador, '//button[@title="'+regional_settings['enter_button']+'"]'):
            navegador.find_element(By.XPATH, '//button[@title="'+regional_settings['enter_button']+'"]').click()
            break
        time.sleep(1)

    for x in range(10):
        if check_exists_by_xpath(navegador, '//button[@title="Login"]'):
            navegador.find_element(By.XPATH, '//button[@title="Login"]').click()
            break
        time.sleep(1)
        
    for x in range(10):
        if check_exists_by_xpath(navegador, "//div[contains(@role,'dialog')]"):
            navegador.find_element(By.XPATH,"//div[contains(@role,'dialog')]")
            navegador.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div[2]/button[2]').click()
            break
        time.sleep(1)

    for x in range(10):
        if check_exists_by_xpath(navegador, "//div[contains(@role,'dialog')]"):
            navegador.find_element(By.XPATH,"//div[contains(@role,'dialog')]")
            navegador.find_element(By.ID,'nsec-input').send_keys(user_nsec)
            break
        time.sleep(1)

    for x in range(10):
        if check_exists_by_xpath(navegador, "//button[contains(@type,'submit')]"):
            navegador.find_element(By.XPATH,"//button[contains(@type,'submit')]").click()
            break
        time.sleep(1)

    # Go to Post
    for x in range(10):
        if check_exists_by_xpath(navegador, '//button[@title="New post"]'):
            navegador.find_element(By.XPATH, '//button[@title="New post"]').click()
            break
        time.sleep(1)

    # Click upload image
    for x in range(10):
        if check_exists_by_xpath(navegador, "//div[contains(@role,'dialog')]"):
            navegador.find_element(By.XPATH,"//div[contains(@role,'dialog')]")
            break
        time.sleep(1)
   
    for x in range(10):
        if check_exists_by_xpath(navegador, "//div[contains(@role,'dialog')]//button[contains(@class,'hover:text-accent-foreground')]"):
          navegador.find_element(By.XPATH,"//div[contains(@role,'dialog')]//button[contains(@class,'hover:text-accent-foreground')]")
          
          # Find the hidden input element (replace with your actual locator)
          hidden_input = navegador.find_element(By.XPATH,"//input[contains(@type,'file')]") 

          # Make the hidden input element visible
          navegador.execute_script("arguments[0].style.display = 'block';", hidden_input)

          # Send the file path to the now-visible input
          hidden_input.send_keys(file_path)
          time.sleep(1)
          break
        time.sleep(1)

    for x in range(10):
        if check_exists_by_xpath(navegador, '//div[contains(@role,"dialog")]//div[contains(@class,"tiptap")]/p'):
            paragraph = navegador.find_element(By.XPATH,'//div[contains(@role,"dialog")]//div[contains(@class,"tiptap")]/p')
            paragraph.send_keys(message)
            break
        time.sleep(1)

    # check if the image was uploaded
    for x in range(10):
        if check_exists_by_xpath(navegador, '//div[contains(@role,"dialog")]//div[contains(@class,"tiptap")]/p'):
            paragraph = navegador.find_elements(By.XPATH,'//div[contains(@role,"dialog")]//div[contains(@class,"tiptap")]/p')
            for p in paragraph:
                if "https://image.nostr.build" in p.text:
                    print(p.text)
                    break
            break
        time.sleep(1)

    for x in range(10):
        if check_exists_by_xpath(navegador, '//div[contains(@role,"dialog")]//button[contains(@type, "submit")]'):
            submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@role,"dialog")]//button[contains(@type, "submit")]')))
            submit.click()
            break
        time.sleep(1)

    #Closing Browser
    time.sleep(10)
    navegador.quit()

def main():
    upload_image()

if __name__=='__main__':
    main()
