import pytest
import allure
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.mark.usefixtures("setup")
class TestVisualizarAvaliacoes:

    @allure.testcase("Testando visualizar avaliacoes profissional ")
    def test_visualizar_avaliacoes_profissional(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("Ana")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()

        time.sleep(2)
        driver.forward()
        driver.find_element_by_xpath('/html/body/aside/ul/li[2]/a/span').click()

        time.sleep(2)
        driver.forward()
        result = driver.find_element_by_xpath('/html/body/main/div[3]/div/div').text

        # print("RESULT--->", result)

        assert "Nenhuma Avaliação encontrada!" is not result

    @allure.testcase("Testando visualizar avaliacoes profissional vazio")
    def test_visualizar_avaliacoes_profissional_vazio(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste2")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()

        time.sleep(2)
        driver.forward()
        driver.find_element_by_xpath('/html/body/aside/ul/li[2]/a/span').click()

        time.sleep(2)
        driver.forward()
        result = driver.find_element_by_xpath('/html/body/main/div[3]/div/div').text

        #print("RESULT--->", result)

        assert "Nenhuma Avaliação encontrada!" in result


    def tearDown(self):
        self.driver.close()
