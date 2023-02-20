import os
import json
import boto3
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import RemoteWebDriver
import time

timestr = time.strftime("%Y%m%d-%H%M%S")
s3 = boto3.client('s3')

def run_test():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")

    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities.update(chrome_options.to_capabilities())

    driver = RemoteWebDriver(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=capabilities)

    driver.get("https://www.youtube.com")
    time.sleep(5)
    driver.save_screenshot("/tmp/image.png")
    s3.upload_file('/tmp/image.png', 'testseleniumchromedriver', 'image.png')
    print(driver.page_source)
    driver.quit()

def lambda_handler(event, context):
    run_test()
    return True
