import unittest
import webbrowser

import allure
import time

import requests
from selenium import webdriver

from selenium.webdriver.common.keys import Keys


class TestMensagens(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    @allure.testcase("Testando enviar mensagem")
    def test_enviar_mensagem_profissional(self):
        driver = self.driver
        driver.get("https://workbook-teste.herokuapp.com/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste1")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        driver.find_element_by_name("termo").send_keys("manicure")
        driver.find_element_by_name("termo").send_keys(Keys.RETURN)

        time.sleep(2)
        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[1]/div/div/div/div/a').click()
        driver.find_element_by_xpath('//*[@id="enviar-mensagem-perfil"]').click()

        time.sleep(2)
        driver.forward()
        driver.find_element_by_xpath('//*[@id="enviar-mensagem-perfil"]').click()
        time.sleep(2)
        driver.forward()
        time.sleep(2)
        driver.find_element_by_name("texto").send_keys("Boa tarde")
        time.sleep(2)
        #driver.find_element_by_xpath('//*[@id="direct-chat-footer"]/div/span/button').click()

        #result = driver.find_element_by_class_name('direct-chat-text').text
        #print("RESULT--->", result)

        #assert "Boa tarde" in result