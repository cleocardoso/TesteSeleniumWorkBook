import unittest

import allure
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class TestMensagem(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    @allure.testcase("Testando o enviar mensagem")
    def test_enviar_mensagem(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste2")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()

        time.sleep(2)  # ele vai pausar por 2 segundos
        driver.forward()
        driver.find_element_by_name("termo").send_keys("manicure")
        driver.find_element_by_name("termo").send_keys(Keys.RETURN)

        time.sleep(2)  # ele vai pausar por 2 segundos
        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[1]/div/div/div[1]/div/a/h5').click()

        time.sleep(2)  # ele vai pausar por 2 segundos
        driver.forward()
        driver.find_element_by_xpath('//*[@id="enviar-mensagem-perfil"]').click()

        time.sleep(2)  # ele vai pausar por 2 segundos
        driver.forward()
        driver.find_element_by_xpath('//*[@id="direct-chat-footer"]/div/input').send_keys("oi")
        driver.find_element_by_xpath('//*[@id="direct-chat-footer"]/div/span/button').click()

        msg = driver.find_element_by_xpath('//*[@id="direct-chat"]/div[3]/div[2]').text
        data = driver.find_element_by_xpath('//*[@id="direct-chat"]/div[3]/div[1]/span[2]').text

        result = msg + data

        print("resultado=>>>", result)

        self.assertTrue("oi" + "07/02/2022" in result)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()