import pytest
import allure
import time

import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

@pytest.mark.usefixtures("setup")
class TestLogin:

    @allure.testcase("Testando o login valido")
    def test_login_valido(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)  # ele vai pausar por 2 segundos
        driver.forward()
        result = ""
        try:
            result = driver.find_element_by_class_name('alert-success').text
            print("RESULT -> ", result)
        except NoSuchElementException:
            print('Error')

        #assert "Login Efetuado Sucesso!" in result
        assert "Login Efetuado Sucesso!" in result

    @allure.testcase("Testando o login invalido")
    def test_login_invalido(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("test")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)  # ele vai pausar por 2 segundos
        #driver.forward()
        result2 = ""
        # result = driver.get("http://127.0.0.1:8000/listarProfissional")
        try:
            result2 = driver.find_element_by_class_name('alert-danger').text
            print("RESULT -> ", result2)
        except NoSuchElementException:
            print('Error')

        #assert "Usuário ou senha inválido." in result2
        assert "Usuário ou senha inválido." in result2

    def tearDown(self):
            self.driver.close()


