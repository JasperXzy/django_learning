from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = webdriver.chrome.service.Service('../chromedriver/chromedriver.exe')
browser = webdriver.Chrome(service=service)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
