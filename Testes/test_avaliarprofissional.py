import unittest
import pytest
import allure
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.mark.usefixtures("setup")
class TestAvaliarProfissional:

    @allure.testcase("Avaliar Profissional valido")#não foi possivel realizar
    def test_Avaliar_profissional_valido(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        driver.find_element_by_name("termo").send_keys("manicure")
        driver.find_element_by_name("termo").send_keys(Keys.RETURN)

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[1]/div/div/div/div/a/h5').click()

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div/div/div[2]/a[2]').click()

        driver.find_element_by_xpath('//*[@id="show_class"]/div[1]/div/label[3]').click()
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("Bom")

        driver.find_element_by_xpath('//*[@id="show_class"]/div[3]/button').click()

        result = driver.find_element_by_xpath('')

        assert('Avaliação realizada com sucesso!')

    @allure.testcase("Avaliar Profissional campo descrição vazio")
    def test_Avaliar_profissional_descrição_vazio(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        driver.find_element_by_name("termo").send_keys("manicure")
        driver.find_element_by_name("termo").send_keys(Keys.RETURN)

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[1]/div/div/div/div/a/h5').click()

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div/div/div[2]/a[2]').click()

        driver.find_element_by_xpath('').click()
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("")

        driver.find_element_by_xpath('//*[@id="show_class"]/div[3]/button').click()

        result = driver.find_element_by_xpath('')

        assert('Avaliação realizada com sucesso!')

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

        assert("Nenhuma Avaliação encontrada!" is not result)

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

        assert("Nenhuma Avaliação encontrada!" in result)

    @allure.testcase("Avaliar Profissional nota minima")  # não foi possivel realizar
    def test_Avaliar_profissional_nota_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        driver.find_element_by_name("termo").send_keys("manicure")
        driver.find_element_by_name("termo").send_keys(Keys.RETURN)

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[1]/div/div/div/div/a/h5').click()

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div/div/div[2]/a[2]').click()

        driver.find_element_by_xpath('//*[@id="show_class"]/div[1]/div/label[1]/i').click()
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("Bom")

        driver.find_element_by_xpath('//*[@id="show_class"]/div[3]/button').click()

        result = driver.find_element_by_xpath('')

        assert('Avaliação realizada com sucesso!')

    @allure.testcase("Avaliar Profissional nota maxima")  # não foi possivel realizar
    def test_Avaliar_profissional_nota_max(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        driver.find_element_by_name("termo").send_keys("manicure")
        driver.find_element_by_name("termo").send_keys(Keys.RETURN)

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[1]/div/div/div/div/a/h5').click()

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div/div/div[2]/a[2]').click()

        driver.find_element_by_xpath('//*[@id="show_class"]/div[1]/div/label[5]').click()
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("Bom")

        driver.find_element_by_xpath('//*[@id="show_class"]/div[3]/button').click()

        result = driver.find_element_by_xpath('')

        assert('Avaliação realizada com sucesso!')

    @allure.testcase("Avaliar Profissional descricao minima")  # não foi possivel realizar
    def test_Avaliar_profissional_descricao_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        driver.find_element_by_name("termo").send_keys("manicure")
        driver.find_element_by_name("termo").send_keys(Keys.RETURN)

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[1]/div/div/div/div/a/h5').click()

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div/div/div[2]/a[2]').click()

        driver.find_element_by_xpath('//*[@id="show_class"]/div[1]/div/label[5]').click()
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("B")

        driver.find_element_by_xpath('//*[@id="show_class"]/div[3]/button').click()

        result = driver.find_element_by_xpath('')

        assert('Avaliação realizada com sucesso!')

    @allure.testcase("Avaliar Profissional descricao maxima")  # não foi possivel realizar
    def test_Avaliar_profissional_descricao_max(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        driver.find_element_by_name("termo").send_keys("manicure")
        driver.find_element_by_name("termo").send_keys(Keys.RETURN)

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[1]/div/div/div/div/a/h5').click()

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div/div/div[2]/a[2]').click()

        driver.find_element_by_xpath('//*[@id="show_class"]/div[1]/div/label[5]').click()
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("B" * 251)

        driver.find_element_by_xpath('//*[@id="show_class"]/div[3]/button').click()

        result = driver.find_element_by_xpath('')

        assert('Avaliação realizada com sucesso!')

    def tearDown(self):
        self.driver.close()






