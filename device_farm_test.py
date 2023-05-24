import os
import json
import boto3
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time

timestr = time.strftime("%Y%m%d-%H%M%S")
s3 = boto3.client('s3')
devicefarm = boto3.client('devicefarm', region_name='us-west-2')

remote_url = devicefarm.create_test_grid_url(
    projectArn="arn:aws:devicefarm:us-west-2:482218046771:testgrid-project:0d0a9d1b-c4b0-4393-a4c1-e07e25686ceb",
    expiresInSeconds=900
)

driver = webdriver.Remote(remote_url["url"], webdriver.DesiredCapabilities.CHROME)

try:
    driver.get("https://www.youtube.com")
    time.sleep(120)
    driver.save_screenshot("/tmp/image.png")
    object_key = 'image-' + timestr + '.png'
    s3.upload_file('/tmp/image.png', 'testseleniumchromedriver', object_key)
except Exception as e:
    print(e)
finally:
    driver.quit()
