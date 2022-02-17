import unittest
import webbrowser

import allure
import time
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.mark.usefixtures("setup")
class TestListagemProfissional:

    @allure.testcase("Testando o Campos buscar profissional valido")
    def test_listar_profissional_valido(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(5)
        print("Antes ", driver.current_url)

        driver.forward()
        current = driver.current_url  # ele recebe essa rota /listarProfissional
        driver.find_element_by_name("termo").send_keys("Programador")
        driver.find_element_by_name("termo").send_keys(Keys.RETURN)

        driver.forward()  # a troca acontece aqui
        print("Depois do depois ", current)
        # result = driver.find_element_by_class_name('card-columns').text

        # assert "manicure" in result
        #assert current not in driver.current_url  # e essa recebe  buscar termo
        assert current not in driver.current_url

    @allure.testcase("Testando o Campos buscar profissional nao encontrado")
    def test_listar_profissional_invalido(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        driver.find_element_by_name("termo").send_keys("Pedreiro")
        driver.find_element_by_name("termo").send_keys(Keys.RETURN)

        driver.forward()

        result = driver.find_element_by_class_name('alert-danger').text

        #assert "Profissional não encontrado!" in result
        assert "Profissional não encontrado!" in result

    @allure.testcase("Testando o Campos buscar profissional vazio")
    def test_listar_profissional_vazio(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        driver.find_element_by_name("termo").send_keys("")
        driver.find_element_by_name("termo").send_keys(Keys.RETURN)

        driver.forward()

        result = driver.find_element_by_class_name('alert-danger').text

        #assert "Campo não pode ser vazio!" in result
        assert "Campo não pode ser vazio!" in result


    def tearDown(self):
        self.driver.close()



