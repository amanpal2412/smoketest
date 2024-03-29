import os
import json
import boto3
import selenium
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import os
import shutil
import uuid
import time
from datetime import datetime
import datetime

timestr = time.strftime("%Y%m%d-%H%M%S")
#s3 = boto3.client('s3')

class WebDriver(object):

    def __init__(self):
        self.options = Options()

        self.options.binary_location = '/usr/bin/google-chrome'
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--start-fullscreen')
        self.options.add_argument('--single-process')
        self.options.add_argument('--disable-dev-shm-usage')

    def get(self):
        driver = webdriver.Chrome('/opt/chromedriver', options=self.options)
        return driver


def main():
    
    instance_ = WebDriver()
    driver = instance_.get()
    driver.get("https://www.youtube.com")
    time.sleep(5)
    driver.save_screenshot("/tmp/image.png")
    #obj_name = "image" + timestr + ".png"
    #s3.upload_file('/tmp/image.png', 'testseleniumchromedriver', 'image.png')
    print(driver.page_source)
    return True

if __name__ == "__main__":
    main()
