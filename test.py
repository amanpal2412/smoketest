#try:
import json
import boto3
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import os
import shutil
import uuid
import time
from datetime import datetime
import datet
print("All Modules are ok ...")

timestr = time.strftime("%Y%m%d-%H%M%S")
s3 = boto3.client('s3')

#except Exception as e:

#    print("Error in Imports ")



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
        driver = Chrome('/opt/chromedriver', options=self.options)
        return driver
    
        instance_ = WebDriver()
        print("Printing instance value :" + instance_)
        return "Testing"
