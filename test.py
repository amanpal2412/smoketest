try:
    import json
    import boto3
    #from selenium.webdriver import Chrome
    #from selenium.webdriver.chrome.options import Options
    import os
    import shutil
    import uuid
    import time
    from datetime import datetime
    import datetime
    import sys
    sys.path.append('/opt')
    import selenium
    from selenium import webdriver
    from selenium.webdriver import Chrome
    from selenium.webdriver import chrome.options.Options

    print("All Modules are ok ...")

    timestr = time.strftime("%Y%m%d-%H%M%S")
    s3 = boto3.client('s3')

except Exception as e:

    print("Error in Imports ")



class WebDriver(object):

    def __init__(self):
        self.options = chrome.options.Options()

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


if __name__ == "__main__":
    
    instance_ = WebDriver()
    driver = instance_.get()
    driver.get("https://www.youtube.com")
    time.sleep(5)
    driver.save_screenshot("/tmp/image.png")
    s3.upload_file('/tmp/image.png', 'testseleniumchromedriver', 'image.png_'+timestr)
    print(driver.page_source)
    #return True
