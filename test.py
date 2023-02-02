import os
# Add path to shared libraries
#os.environ['LD_LIBRARY_PATH'] = '/opt'
#os.environ['PYTHONPATH'] = '/opt'
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
s3 = boto3.client('s3')

class WebDriver(object):

    def __init__(self):
        self.options = Options()

        self.options.binary_location = '/opt/headless-chromium'
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--start-fullscreen')
        self.options.add_argument('--single-process')
        self.options.add_argument('--disable-dev-shm-usage')

    def get(self):
        driver = webdriver.Chrome('/opt/chromedriver', options=self.options)
        return driver


def lambda_handler(event, context):
    
    instance_ = WebDriver()
    driver = instance_.get()
    driver.get("https://www.youtube.com")
    time.sleep(5)
    driver.save_screenshot("/tmp/image.png")
    obj_name = "image" + timestr + ".png"
    s3.upload_file('/tmp/image.png', 'testseleniumchromedriver', obj_name)
    print(driver.page_source)
    return True
