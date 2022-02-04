import unittest
import webbrowser

import allure
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestAvaliarProfissional(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    @allure.testcase("Testando visualizar avaliacoes profissional vazio")
    def test_visualizar_avaliacoes_profissional_vazio(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("Ana")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        driver.find_element_by_name("termo").send_keys("manicure")
        driver.find_element_by_name("termo").send_keys(Keys.RETURN)

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/main/div[1]/div/div/div/div/a').click()
        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div/div/div[1]/div/div[2]/a').click()

        time.sleep(2)
        driver.forward()
        result = driver.find_element_by_xpath('/html/body/main/div[2]/div/div').text

        #print("RESULT--->", result)

        #assert "Nenhuma Avaliação encontrada!" in result
        self.assertTrue("Nenhuma Avaliação encontrada!" in result)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()




