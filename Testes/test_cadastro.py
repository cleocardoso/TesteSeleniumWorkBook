import random
import unittest
import webbrowser

import allure
import time

import requests
from selenium import webdriver
from utils.generate import __generate__phone__, __generate__


class TestCadastro(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome(executable_path=r"D:\Downloads\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome()
        # self.driver.get("http://127.0.0.1:8000/cadastro/")

    @allure.testcase("Testando o Cadastrar valido")
    def test_cadastro_campos_validos(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        obj = __generate__(is_valid_password=True)
        nome = obj['username']
        email = obj['email']
        cidade = obj['city']
        rua = obj['road']
        uf = obj['uf']
        bairro = obj['district']
        senha = obj['password']
        telefone = obj['phone']
        # Preencher usuario
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(nome)
        # Preencher nome
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(nome)
        # Preencher email
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        # Preencher telefone
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys(telefone)
        # Preencher cidade
        driver.find_element_by_xpath('//*[@id="cidade"]').send_keys(cidade)
        # Preencher rua
        driver.find_element_by_xpath('//*[@id="rua"]').send_keys(rua)
        # Preencher uf
        driver.find_element_by_xpath('//*[@id="uf"]').send_keys(uf)
        # Preencher bairro
        driver.find_element_by_xpath('//*[@id="bairro"]').send_keys(bairro)
        # Preencher senha
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys(senha)
        # Preencher confirmar senha
        driver.find_element_by_xpath('//*[@id="senha2"]').send_keys(senha)
        # botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()
        time.sleep(2)
        result = driver.find_element_by_class_name('alert-success').text
        #print("result---->",result)
        #assert "Usuário Registrado com Sucesso!" in result
        self.assertTrue("Usuário Registrado com Sucesso!" in result)

    @allure.testcase("Testando o Cadastrar vazio")
    def test_cadastro_campos_vazio(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        # Preencher usuario

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("")
        # Preencher nome
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys("")
        # Preencher email
        driver.find_element_by_xpath('//*[@id="email"]').send_keys("")
        # Preencher telefone
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys("")
        # Preencher cidade
        driver.find_element_by_xpath('//*[@id="cidade"]').send_keys("")
        # Preencher rua
        driver.find_element_by_xpath('//*[@id="rua"]').send_keys("")
        # Preencher uf
        driver.find_element_by_xpath('//*[@id="uf"]').send_keys("")
        # Preencher bairro
        driver.find_element_by_xpath('//*[@id="bairro"]').send_keys("")
        # Preencher senha
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys("")
        # Preencher confirmar senha
        driver.find_element_by_xpath('//*[@id="senha2"]').send_keys("")
        # botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

        # result = driver.find_element_by_xpath('/html/body/main/div/div[1]').text
        result = driver.find_element_by_class_name('alert-danger').text
        #print("resultado--->", result)
        assert "Preencha todos os Campos!" in result

    @allure.testcase("Testando o Campo usuario igual")
    def test_cadastro_campo_usuario_igual(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        obj = __generate__()
        nome = obj['username']
        email = obj['email']
        cidade = obj['city']
        rua = obj['road']
        uf = obj['uf']
        bairro = obj['district']
        senha = obj['password']
        telefone = obj['phone']
        # Preencher usuario
        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste")
        # Preencher nome
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(nome)
        # Preencher email
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        # Preencher telefone
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys(telefone)
        # Preencher cidade
        driver.find_element_by_xpath('//*[@id="cidade"]').send_keys(cidade)
        # Preencher rua
        driver.find_element_by_xpath('//*[@id="rua"]').send_keys(rua)
        # Preencher uf
        driver.find_element_by_xpath('//*[@id="uf"]').send_keys(uf)
        # Preencher bairro
        driver.find_element_by_xpath('//*[@id="bairro"]').send_keys(bairro)
        # Preencher senha
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys(senha)
        # Preencher confirmar senha
        driver.find_element_by_xpath('//*[@id="senha2"]').send_keys(senha)
        # botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

        result = driver.find_element_by_class_name('alert-danger').text
        print("RESULT -> ", result)
        #assert "Informe outro nome de usuário!" in result
        self.assertTrue("Informe outro nome de usuário!" in result)

    @allure.testcase("Testando o Campo usuario tamamho max de 150")
    def test_cadastro_campo_usuario_tamanho(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        obj = __generate__()
        nome = obj['username']
        email = obj['email']
        cidade = obj['city']
        rua = obj['road']
        uf = obj['uf']
        bairro = obj['district']
        senha = obj['password']
        telefone = obj['phone']
        # Preencher usuario
        driver.find_element_by_xpath('//*[@id="username"]').send_keys("ta" * 160)
        # Preencher nome
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(nome)
        # Preencher email
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        # Preencher telefone
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys(telefone)
        # Preencher cidade
        driver.find_element_by_xpath('//*[@id="cidade"]').send_keys(cidade)
        # Preencher rua
        driver.find_element_by_xpath('//*[@id="rua"]').send_keys(rua)
        # Preencher uf
        driver.find_element_by_xpath('//*[@id="uf"]').send_keys(uf)
        # Preencher bairro
        driver.find_element_by_xpath('//*[@id="bairro"]').send_keys(bairro)
        # Preencher senha
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys(senha)
        # Preencher confirmar senha
        driver.find_element_by_xpath('//*[@id="senha2"]').send_keys(senha)
        # botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

        result = driver.find_element_by_class_name('alert-success').text
        print("RESULT -> ", result)
        # assert "Informe outro nome de usuário!" in result
        self.assertTrue("Esse campo so aceita no maximo 150 caracteres." in result)

    @allure.testcase("Testando o Campo nome tamamho max de 150")
    def test_cadastro_campo_nome_tamanho(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        obj = __generate__()
        nome = obj['username']
        email = obj['email']
        cidade = obj['city']
        rua = obj['road']
        uf = obj['uf']
        bairro = obj['district']
        senha = obj['password']
        telefone = obj['phone']
        # Preencher usuario
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(nome)
        # Preencher nome
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys("t" * 160)
        # Preencher email
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        # Preencher telefone
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys(telefone)
        # Preencher cidade
        driver.find_element_by_xpath('//*[@id="cidade"]').send_keys(cidade)
        # Preencher rua
        driver.find_element_by_xpath('//*[@id="rua"]').send_keys(rua)
        # Preencher uf
        driver.find_element_by_xpath('//*[@id="uf"]').send_keys(uf)
        # Preencher bairro
        driver.find_element_by_xpath('//*[@id="bairro"]').send_keys(bairro)
        # Preencher senha
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys(senha)
        # Preencher confirmar senha
        driver.find_element_by_xpath('//*[@id="senha2"]').send_keys(senha)
        # botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

        result = driver.find_element_by_class_name('alert-success').text
        #print("RESULT -> ", result)
        # assert "Informe outro nome de usuário!" in result
        self.assertTrue("Esse campo so aceita no maximo 150 caracteres." in result)

    @allure.testcase("Testando o Campo email invalido")
    def test_cadastro_campo_email_invalido(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        obj = __generate__()
        nome = obj['username']
        email = obj['email']
        cidade = obj['city']
        rua = obj['road']
        uf = obj['uf']
        bairro = obj['district']
        senha = obj['password']
        telefone = obj['phone']

        # Preencher usuario
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(nome)
        # Preencher nome
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(nome)
        # Preencher email
        driver.find_element_by_xpath('//*[@id="email"]').send_keys("teste@a")
        # Preencher telefone
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys(telefone)
        # Preencher cidade
        driver.find_element_by_xpath('//*[@id="cidade"]').send_keys(cidade)
        # Preencher rua
        driver.find_element_by_xpath('//*[@id="rua"]').send_keys(rua)
        # Preencher uf
        driver.find_element_by_xpath('//*[@id="uf"]').send_keys(uf)
        # Preencher bairro
        driver.find_element_by_xpath('//*[@id="bairro"]').send_keys(bairro)
        # Preencher senha
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys(senha)
        # Preencher confirmar senha
        driver.find_element_by_xpath('//*[@id="senha2"]').send_keys(senha)
        # botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

        result = driver.find_element_by_class_name('alert-danger').text
        #print("Resuslt--->", result)
        #assert "Email Inválido!" in result
        self.assertTrue("Email Inválido!" in result)

    @allure.testcase("Testando o Campo email igual")
    def test_cadastro_campo_email_igual(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        obj = __generate__()
        nome = obj['username']
        email = obj['email']
        cidade = obj['city']
        rua = obj['road']
        uf = obj['uf']
        bairro = obj['district']
        senha = obj['password']
        telefone = obj['phone']
        # Preencher usuario
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(nome)
        # Preencher nome
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(nome)
        # Preencher email
        driver.find_element_by_xpath('//*[@id="email"]').send_keys("teste@gmail.com")
        # Preencher telefone
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys(telefone)
        # Preencher cidade
        driver.find_element_by_xpath('//*[@id="cidade"]').send_keys(cidade)
        # Preencher rua
        driver.find_element_by_xpath('//*[@id="rua"]').send_keys(rua)
        # Preencher uf
        driver.find_element_by_xpath('//*[@id="uf"]').send_keys(uf)
        # Preencher bairro
        driver.find_element_by_xpath('//*[@id="bairro"]').send_keys(bairro)
        # Preencher senha
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys(senha)
        # Preencher confirmar senha
        driver.find_element_by_xpath('//*[@id="senha2"]').send_keys(senha)
        # botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

        result = driver.find_element_by_class_name('alert-danger').text
        print("Resultado---->",result)
        #assert "Email já existente para um usuário!" in result
        self.assertTrue("Email já existente para um usuário!" in result)

    @allure.testcase("Testando o Campo email tamamho max de 254")
    def test_cadastro_campo_nome_tamanho(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        obj = __generate__()
        nome = obj['username']
        email = obj['email']
        cidade = obj['city']
        rua = obj['road']
        uf = obj['uf']
        bairro = obj['district']
        senha = obj['password']
        telefone = obj['phone']
        # Preencher usuario
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(nome)
        # Preencher nome
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(nome)
        # Preencher email
        driver.find_element_by_xpath('//*[@id="email"]').send_keys("f", * 255,"@gmail.com")
        # Preencher telefone
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys(telefone)
        # Preencher cidade
        driver.find_element_by_xpath('//*[@id="cidade"]').send_keys(cidade)
        # Preencher rua
        driver.find_element_by_xpath('//*[@id="rua"]').send_keys(rua)
        # Preencher uf
        driver.find_element_by_xpath('//*[@id="uf"]').send_keys(uf)
        # Preencher bairro
        driver.find_element_by_xpath('//*[@id="bairro"]').send_keys(bairro)
        # Preencher senha
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys(senha)
        # Preencher confirmar senha
        driver.find_element_by_xpath('//*[@id="senha2"]').send_keys(senha)
        # botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

        result = driver.find_element_by_class_name('alert-success').text
        print("RESULT -> ", result)
        # assert "Informe outro nome de usuário!" in result
        #self.assertTrue("Esse campo so aceita no maximo 254 caracteres." in result)

    @allure.testcase("Testando o Campo telefone tamamho max de 11")
    def test_cadastro_campo_telefone_tamanho(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        obj = __generate__()
        nome = obj['username']
        email = obj['email']
        cidade = obj['city']
        rua = obj['road']
        uf = obj['uf']
        bairro = obj['district']
        senha = obj['password']
        telefone = obj['phone']
        # Preencher usuario
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(nome)
        # Preencher nome
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(nome)
        # Preencher email
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        # Preencher telefone
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys(9999999999999)
        # Preencher cidade
        driver.find_element_by_xpath('//*[@id="cidade"]').send_keys(cidade)
        # Preencher rua
        driver.find_element_by_xpath('//*[@id="rua"]').send_keys(rua)
        # Preencher uf
        driver.find_element_by_xpath('//*[@id="uf"]').send_keys(uf)
        # Preencher bairro
        driver.find_element_by_xpath('//*[@id="bairro"]').send_keys(bairro)
        # Preencher senha
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys(senha)
        # Preencher confirmar senha
        driver.find_element_by_xpath('//*[@id="senha2"]').send_keys(senha)
        # botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

        result = driver.find_element_by_class_name('alert-success').text
        print("RESULT -> ", result)

        self.assertTrue("Informe no máximo 11 números." in result)

    @allure.testcase("Testando o Campo telefone inserindo caracteres")
    def test_cadastro_campo_telefone_inserindo_caractere(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        obj = __generate__()
        nome = obj['username']
        email = obj['email']
        cidade = obj['city']
        rua = obj['road']
        uf = obj['uf']
        bairro = obj['district']
        senha = obj['password']
        telefone = obj['phone']
        # Preencher usuario
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(nome)
        # Preencher nome
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(nome)
        # Preencher email
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        # Preencher telefone
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys("aaaaaaaaaaa")
        # Preencher cidade
        driver.find_element_by_xpath('//*[@id="cidade"]').send_keys(cidade)
        # Preencher rua
        driver.find_element_by_xpath('//*[@id="rua"]').send_keys(rua)
        # Preencher uf
        driver.find_element_by_xpath('//*[@id="uf"]').send_keys(uf)
        # Preencher bairro
        driver.find_element_by_xpath('//*[@id="bairro"]').send_keys(bairro)
        # Preencher senha
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys(senha)
        # Preencher confirmar senha
        driver.find_element_by_xpath('//*[@id="senha2"]').send_keys(senha)
        # botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

        result = driver.find_element_by_class_name('alert-success').text
        print("RESULT -> ", result)

        self.assertTrue("Informe somente números nesse campo." in result)

    @allure.testcase("Testando o Campo senha menor 6 numeros")
    def test_cadastro_campo_senha_menor_6(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        obj = __generate__()
        nome = obj['username']
        email = obj['email']
        cidade = obj['city']
        rua = obj['road']
        uf = obj['uf']
        bairro = obj['district']
        telefone = obj['phone']
        senha = obj['password']
        # Preencher usuario
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(nome)
        # Preencher nome
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(nome)
        # Preencher email
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        # Preencher telefone
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys(telefone)
        # Preencher cidade
        driver.find_element_by_xpath('//*[@id="cidade"]').send_keys(cidade)
        # Preencher rua
        driver.find_element_by_xpath('//*[@id="rua"]').send_keys(rua)
        # Preencher uf
        driver.find_element_by_xpath('//*[@id="uf"]').send_keys(uf)
        # Preencher bairro
        driver.find_element_by_xpath('//*[@id="bairro"]').send_keys(bairro)
        # Preencher senha
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys("1234")
        # Preencher confirmar senha
        driver.find_element_by_xpath('//*[@id="senha2"]').send_keys(senha)
        # botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

        result = driver.find_element_by_class_name('alert-danger').text

        #assert "Senha precisa ter pelo menos 6 Caracteres!" in result
        self.assertTrue("Senha precisa ter pelo menos 6 Caracteres!" in result)

    @allure.testcase("Testando o Campo senha tamanho max 128")
    def test_cadastro_campo_senha_tamanho_max(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        obj = __generate__()
        nome = obj['username']
        email = obj['email']
        cidade = obj['city']
        rua = obj['road']
        uf = obj['uf']
        bairro = obj['district']
        telefone = obj['phone']
        senha = obj['password']
        # Preencher usuario
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(nome)
        # Preencher nome
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(nome)
        # Preencher email
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        # Preencher telefone
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys(telefone)
        # Preencher cidade
        driver.find_element_by_xpath('//*[@id="cidade"]').send_keys(cidade)
        # Preencher rua
        driver.find_element_by_xpath('//*[@id="rua"]').send_keys(rua)
        # Preencher uf
        driver.find_element_by_xpath('//*[@id="uf"]').send_keys(uf)
        # Preencher bairro
        driver.find_element_by_xpath('//*[@id="bairro"]').send_keys(bairro)
        # Preencher senha
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys("1" * 130)
        # Preencher confirmar senha
        driver.find_element_by_xpath('//*[@id="senha2"]').send_keys("1" * 130)
        # botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

        result = driver.find_element_by_class_name('alert-danger').text

        self.assertTrue("Esse campo so aceita no maximo 128 caracteres." in result)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
