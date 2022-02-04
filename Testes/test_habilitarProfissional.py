import random
import unittest
import webbrowser

import allure
import time

import requests
from selenium import webdriver


class TestHabilitarProfissional(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    @allure.testcase("Testando o Campos habilitar profissional valido")
    def test_habilitar_profissional_valido(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste2")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/aside/ul/li[2]/a/span').click()

        driver.forward()

        driver.find_element_by_xpath('//*[@id="id_profissao"]').send_keys("Professora")
        driver.find_element_by_xpath('//*[@id="id_categoria"]').send_keys("Aulas")
        driver.find_element_by_xpath('//*[@id="id_imagem"]').send_keys("D://Area de Trabalho/teste/001.jpg")
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("Aulas de Programação")

        driver.find_element_by_xpath('//html/body/main/div[2]/div/div/div/div/form/div[5]/button').click()

        result = driver.find_element_by_class_name('alert-success').text

        #assert "Perfil profissional adicionado com sucesso!" in result
        self.assertTrue("Perfil profissional adicionado com sucesso!" in result)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()