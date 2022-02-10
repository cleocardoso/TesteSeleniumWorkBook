
import unittest
import webbrowser

import allure
import time


from selenium import webdriver
from utils.generate import __generate__phone__, __generate__


class TestEditarDadosCliente(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(executable_path=r"D:\Downloads\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome()
        # self.driver.get("http://127.0.0.1:8000/cadastro/")

    @allure.testcase("Testando o Editar cadastro cliente valido") #observação verificar depois se possa testar pela url ou tag da pagina
    def test_cadastro_editar_cliente_validos(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste1")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/aside/ul/li[4]/a/span').click()

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div[2]/div/a').click()

        driver.forward()
        driver.find_element_by_xpath('//*[@id="id_username"]').send_keys("teste21")
        driver.find_element_by_xpath('//*[@id="id_last_name"]').send_keys("testando")

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_class_name('alert-success').text

        self.assertTrue("Dados alterados com sucesso" in result)

    @allure.testcase("Testando o Editar dados com campo usuario e nome vazio")  # observação required não permite
    def test_cadastro_editar_cliente_vazio(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/aside/ul/li[4]/a/span').click()

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div[2]/div/a').click()

        driver.forward()
        driver.find_element_by_xpath('//*[@id="id_username"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="id_last_name"]').send_keys("")

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_class_name('alert-danger').text

        self.assertTrue("Prencha os campos vazio!" in result)

    @allure.testcase("Testando o Editar dados com campo usuario e nome vazio")
    def test_cadastro_editar_usuario_vazio(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste1")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/aside/ul/li[4]/a/span').click()

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div[2]/div/a').click()

        driver.forward()
        driver.find_element_by_xpath('//*[@id="id_username"]').send_keys("/")


        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_xpath('//*[@id="error_1_id_username"]/strong').text

        #print("Result====>", result)

        self.assertTrue("Informe um nome de usuário válido." in result)

    @allure.testcase("Testando o Editar dados com campo usuario existente")
    def test_cadastro_editar_usuario_igual(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/aside/ul/li[4]/a/span').click()

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div[2]/div/a').click()

        driver.forward()
        driver.find_element_by_xpath('//*[@id="id_username"]').send_keys("2")

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_xpath('//*[@id="error_1_id_username"]/strong').text

        # print("Result====>", result)

        self.assertTrue("Um usuário com este nome de usuário já existe." in result)

    @allure.testcase("Testando o Editar dados com campo usuario com espaço")
    def test_cadastro_editar_usuario_com_espaco(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/aside/ul/li[4]/a/span').click()

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div[2]/div/a').click()

        driver.forward()
        driver.find_element_by_xpath('//*[@id="id_username"]').clear()
        driver.find_element_by_xpath('//*[@id="id_username"]').send_keys(" ")

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_xpath('//*[@id="error_1_id_username"]/strong').text

        #print("Result====>", result)

        self.assertTrue("Este campo é obrigatório." in result)

    @allure.testcase("Testando o Editar dados com campo usuario max 150")  # verificar o retorno se dados pela url ou tag
    def test_cadastro_editar_usuario_max_150(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste2")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/aside/ul/li[4]/a/span').click()

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div[2]/div/a').click()

        driver.forward()
        driver.find_element_by_xpath('//*[@id="id_username"]').clear()
        driver.find_element_by_xpath('//*[@id="id_username"]').send_keys("1" * 156)

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_xpath('//*[@id="error_1_id_username"]/strong').text

        # print("Result====>", result)

        self.assertTrue("Informe menos de 150 caracteres" in result)

    @allure.testcase("Testando o Editar dados com campo nome com espaço")
    def test_cadastro_editar_nome_com_espaco(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/aside/ul/li[4]/a/span').click()

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div[2]/div/a').click()

        driver.forward()
        driver.find_element_by_xpath('//*[@id="id_first_name"]').clear()
        driver.find_element_by_xpath('//*[@id="id_first_name"]').send_keys(" ")

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_xpath('//*[@id="error_1_id_username"]/strong').text

        #print("Result====>", result)

        self.assertTrue("Este campo é obrigatório." in result)

    @allure.testcase("Testando o Editar dados com campo nome max 150")# verificar o retorno se dados pela url ou tag
    def test_cadastro_editar_nome_max_150(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/aside/ul/li[4]/a/span').click()

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div[2]/div/a').click()

        driver.forward()
        driver.find_element_by_xpath('//*[@id="id_first_name"]').clear()
        driver.find_element_by_xpath('//*[@id="id_first_name"]').send_keys("2" * 157)

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_xpath('//*[@id="error_1_id_username"]/strong').text

        # print("Result====>", result)

        self.assertTrue("Informe menos de 150 caracteres" in result)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
        unittest.main()