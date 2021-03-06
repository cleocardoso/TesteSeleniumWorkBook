import unittest
import  pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.mark.usefixtures("setup")
class TestVisualizarProfissional:


    @allure.testcase("Testando visualizar dados do profissional valido") #testei pela tag da pagina
    def test_dados_profissional_visualizar(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)

        driver.forward()

        driver.find_element_by_name("termo").send_keys("Programador")
        driver.find_element_by_name("termo").send_keys(Keys.RETURN)

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[1]/div/div/div/div/a').click()

        result = driver.find_element_by_xpath('/html/body/main/div[1]/div/h1').text

        assert "Informações Profissionais" in result

    def tearDown(self):
        self.driver.close()



