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
        driver.get("http://127.0.0.1:8000/listarProfissional")



        driver.find_element_by_xpath('/html/body/aside/ul/li[2]/a/span').click()

        driver.forward()

        driver.find_element_by_xpath('//*[@id="id_profissao"]').send_keys("Professora")
        driver.find_element_by_xpath('//*[@id="id_categoria"]').send_keys("Aulas")
        driver.find_element_by_xpath('//*[@id="id_imagem"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("")

        driver.find_element_by_xpath('//html/body/main/div[2]/div/div/div/div/form/div[5]/button').click()
