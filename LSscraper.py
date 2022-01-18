import random
from string import ascii_lowercase,digits
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import urllib.request
import os

folder_name = input("Input the directory name: ")
max = int(input("Input number of images: "))
chrome_options = Options()
chrome_options.add_argument("--headless")
path = os.path.join(os.getcwd(),folder_name)

try:
    os.mkdir(path)
except:
    print("path already exists")


for a in range(0,max):
    amount_of_num = random.randint(1,3)
    digits_lst = [random.choice(digits) for e in range(0,amount_of_num)]
    pic_seed_lst = []
    for i in range(0,6):
        pic_seed_lst.append(random.choice(ascii_lowercase))
    for dig in digits_lst:
        pic_seed_lst[random.randint(0,5)] = dig
    pic_seed = ''.join(pic_seed_lst)
    print(pic_seed)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(f"https://prnt.sc/{pic_seed}")
    time.sleep(1.5)
    try:
        img = driver.find_element(By.XPATH,'//div[@class="under-image"]/img')
        src = img.get_attribute('src')
        time.sleep(1.5)
        dir = os.path.join(path,f"{a+1}({pic_seed}).png")
        urllib.request.urlretrieve(src,dir)
        time.sleep(1)
    except:
        print("wrong url (error)")
driver.quit()