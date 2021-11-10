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
        driver.get("https://workbook-teste.herokuapp.com/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste1")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/aside/ul/li[2]/a/span').click()

        driver.forward()

        driver.find_element_by_xpath('//*[@id="id_profissao"]').send_keys("Professora")
        driver.find_element_by_xpath('//*[@id="id_categoria"]').send_keys("Aulas")
        #driver.find_element_by_xpath('//*[@id="id_imagem"]').send_keys('')
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("Aulas de Programação")

        driver.find_element_by_xpath('//html/body/main/div[2]/div/div/div/div/form/div[5]/button').click()

        result = driver.find_element_by_class_name('alert-success').text

        assert "Perfil profissional adicionado com sucesso!" in result

    @allure.testcase("Testando o Campos habilitar profissional invalido")
    def test_habilitar_profissional_invalido(self):
        driver = self.driver
        driver.get("https://workbook-teste.herokuapp.com/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste2")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/aside/ul/li[2]/a/span').click()

        driver.forward()
        driver.execute_script("""
                          var form = document.getElementsByTagName("form") // vai pegar todos os form da pagina
                          var inputs = form.item(0).getElementsByTagName("input") // vai pegar o primeiro e pegar todos os inputs do form
                          for (let i = 1; i < inputs.length; i++){ // vai percorrer todos, menos o primeiro que fica oculto
                             const input = inputs.item(i) // vai pegar o input na posicao do form
                             if (input.type === 'email'){ 
                               input.setAttribute('type', 'text')  
                               input.removeAttribute('required') // e remover o atributo required para ser disparado o submit
                               break;
                             }
                          }
                          """)
        driver.find_element_by_xpath('//*[@id="id_profissao"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="id_categoria"]').send_keys("")
        # driver.find_element_by_xpath('//*[@id="id_imagem"]').send_keys('')
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("")

        driver.find_element_by_xpath('//html/body/main/div[2]/div/div/div/div/form/div[5]/button').click()

        result = driver.find_element_by_class_name('alert-danger').text

        assert "Preencha os campos!" in result