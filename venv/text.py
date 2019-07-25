from selenium import webdriver

browser = webdriver.Chrome(executable_path=r'/Driver/chromedriver.exe')
browser.get('https://phoenix.vetstoria.com/login#!/')
