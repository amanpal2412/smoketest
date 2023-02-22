import os
import json
import boto3
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import RemoteWebDriver
import time

timestr = time.strftime("%Y%m%d-%H%M%S")
s3 = boto3.client('s3')

PROJECT_ARN = "arn:aws:devicefarm:us-west-2:482218046771:testgrid-project:0d0a9d1b-c4b0-4393-a4c1-e07e25686ceb"

devicefarm = boto3.client('devicefarm', region_name='us-west-2')
remote_url = devicefarm.create_test_grid_url(
    projectArn=PROJECT_ARN,
    expiresInSeconds=300 # 5 minutes. Increase to longer if needed
)

def run_test():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")

    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities.update(chrome_options.to_capabilities())

    driver = RemoteWebDriver(
        command_executor=remote_url["url"],
        desired_capabilities=capabilities)

    driver.get("https://www.youtube.com")
    time.sleep(5)
    driver.save_screenshot("/tmp/image.png")
    s3.upload_file('/tmp/image.png', 'testseleniumchromedriver', 'image.png')
    print(driver.page_source)
    driver.quit()

def main():
    run_test()
    return True
