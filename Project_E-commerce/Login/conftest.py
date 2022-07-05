import pytest
from selenium import webdriver

@pytest.fixture(scope = "class")
# class Browser:

def Chromebrowser(request):
    driver = webdriver.Chrome(executable_path="C:/Users/Kundan.kumar/Downloads/chromedriver_win32/chromedriver.exe")
    request.cls.driver = driver
    yield
    driver.quit()
