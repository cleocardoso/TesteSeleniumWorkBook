import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    #driver = webdriver.Chrome(executable_path=r"D:\Downloads\chromedriver_win32\chromedriver.exe") #if not added in PATH
    #driver.maximize_window()
    driver = webdriver.Chrome()
    request.cls.driver = driver

    yield driver
    driver.close()