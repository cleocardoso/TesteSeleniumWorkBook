import unittest
from datetime import datetime

import allure
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.mark.usefixtures("setup")
class TestMensagem:

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
        time.sleep(2)
        msgEntrada = "teste"
        driver.find_element_by_xpath('//*[@id="direct-chat-footer"]/div/input').send_keys(msgEntrada)
        driver.find_element_by_xpath('//*[@id="direct-chat-footer"]/div/span/button').click()
        time.sleep(2)
        elementos = driver.find_element_by_xpath('//*[@id="direct-chat"]').find_elements_by_class_name('direct-chat-msg')
        tamanho = len(elementos)-1
        elemento= elementos[tamanho]
        array = elemento.find_elements_by_tag_name('div')
        if len(array) > 0:
            elms = array[0].find_elements_by_tag_name('span')
            dataSaida = elms[1].text
            msgSaida = array[1].text

        resultEntrada= msgEntrada + datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        resultSaida = msgSaida + dataSaida

        #print("resultado Entrada=>>>", resultEntrada)
        #print("resultado saida=>>>", resultSaida)

        assert(resultEntrada in resultSaida)

    def tearDown(self):
        self.driver.close()


