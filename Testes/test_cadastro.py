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
        driver.get("https://workbook-teste.herokuapp.com/cadastro/")
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

        assert "Usuário Registrado com Sucesso!" in result

    def test_cadastro_campos_vazio(self):
        driver = self.driver
        driver.get("https://workbook-teste.herokuapp.com/cadastro/")
        self.assertIn("WorkBook", driver.title)
        # Preencher usuario
        driver.execute_script("""
            var form = document.getElementsByTagName("form") // vai pegar todos os form da pagina
            var inputs = form.item(0).getElementsByTagName("input") // vai pegar o primeiro e pegar todos os inputs do form
            for (let i = 1; i < inputs.length; i++){ // vai percorrer todos, menos o primeiro que fica oculto
                const input = inputs.item(i) // vai pegar o input na posicao do form
                input.removeAttribute('required') // e remover o atributo required para ser disparado o submit
            }
            """)
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

        assert "Preencha todos os Campos!" in result

    @allure.testcase("Testando o Campo usuario igual")
    def test_cadastro_campo_usuario_igual(self):
        driver = self.driver
        driver.get("https://workbook-teste.herokuapp.com/cadastro/")
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
        # print("RESULT -> ", result)

    @allure.testcase("Testando o Campo email invalido")
    def test_cadastro_campo_email_invalido(self):
        driver = self.driver
        driver.get("https://workbook-teste.herokuapp.com/cadastro/")
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
        # Preencher usuario
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(nome)
        # Preencher nome
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(nome)
        # Preencher email
        driver.find_element_by_xpath('//*[@id="email"]').send_keys("teste@")
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

        assert "Email Inválido!" in result

    @allure.testcase("Testando o Campo email igual")
    def test_cadastro_campo_email_igual(self):
        driver = self.driver
        driver.get("https://workbook-teste.herokuapp.com/cadastro/")
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

        assert "Email já existente para um usuário!" in result

    @allure.testcase("Testando o Campo telefone maior ou menor de 11 numeros")
    def test_cadastro_campo_telefone_maior_ou_menor(self):
        driver = self.driver
        driver.get("https://workbook-teste.herokuapp.com/cadastro/")
        self.assertIn("WorkBook", driver.title)
        obj = __generate__()
        nome = obj['username']
        email = obj['email']
        cidade = obj['city']
        rua = obj['road']
        uf = obj['uf']
        bairro = obj['district']
        senha = obj['password']
        # Preencher usuario
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(nome)
        # Preencher nome
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(nome)
        # Preencher email
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        # Preencher telefone
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys(__generate__phone__(is_number=True, is_len=True))
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

        assert "Informe no máximo 15 números." in result

    @allure.testcase("Testando o Campo telefone informe so numeros")
    def test_cadastro_campo_telefone_invalido(self):
        driver = self.driver
        driver.get("https://workbook-teste.herokuapp.com/cadastro/")
        self.assertIn("WorkBook", driver.title)
        obj = __generate__()
        nome = obj['username']
        email = obj['email']
        cidade = obj['city']
        rua = obj['road']
        uf = obj['uf']
        bairro = obj['district']
        senha = obj['password']
        # Preencher usuario
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(nome)
        # Preencher nome
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(nome)
        # Preencher email
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        # Preencher telefone
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys(__generate__phone__(is_number=False, is_len=True))
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

        assert "Informe somente números nesse campo." in result

    @allure.testcase("Testando o Campo senha menor 6 numeros")
    def test_cadastro_campo_senha_menor_6(self):
        driver = self.driver
        driver.get("https://workbook-teste.herokuapp.com/cadastro/")
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

        assert "Senha precisa ter pelo menos 6 Caracteres!" in result

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
