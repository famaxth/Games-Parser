from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

path = 'path/to/chromedriver.exe' #you need to change this

def parser():
    driver = webdriver.Chrome(path, chrome_options=options)
    driver.get('https://gamer-info.com/games/year2021/')
    games = driver.find_elements_by_class_name('name')

    for i in range(0, len(games)):
        print(games[i].text)

parser()