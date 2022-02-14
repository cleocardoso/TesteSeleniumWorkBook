
import allure
import time

import pytest
import requests
from selenium import webdriver
from utils.generate import __generate__phone__, __generate__
from utils.input import find__inputs, get__inputs, get__input_by_required, is__valid_by_required, get__input_by_id, \
    is__valid_by_max_length

@pytest.mark.usefixtures("setup")
class TestCadastro:

    @allure.testcase("Testando o Cadastrar valido")
    def test_cadastro_campos_validos(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        #self.assertIn("WorkBook", driver.title)
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
        # print("result---->",result)
        # assert "Usuário Registrado com Sucesso!" in result
        assert("Usuário Registrado com Sucesso!" in result)

    @allure.testcase("Testando o Cadastrar vazio")#deu problema
    def test_cadastro_campos_vazio(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        #self.assertIn("WorkBook", driver.title)
        # campos
        inputs = find__inputs(driver)
        username = get__input_by_id(inputs=inputs, id='username')
        first_name = get__input_by_id(inputs=inputs, id='first_name')
        email = get__input_by_id(inputs=inputs, id='email')
        telefone = get__input_by_id(inputs=inputs, id='telefone')
        cidade = get__input_by_id(inputs=inputs, id='cidade')
        rua = get__input_by_id(inputs=inputs, id='rua')
        uf = get__input_by_id(inputs=inputs, id='uf')
        bairro = get__input_by_id(inputs=inputs, id='bairro')
        senha = get__input_by_id(inputs=inputs, id='senha')
        senha2 = get__input_by_id(inputs=inputs, id='senha2')
        # Preencher usuario
        username['element'].send_keys('')
        first_name['element'].send_keys('')
        email['element'].send_keys('')
        telefone['element'].send_keys('')
        cidade['element'].send_keys('')
        bairro['element'].send_keys('')
        uf['element'].send_keys('')
        senha['element'].send_keys('')
        senha2['element'].send_keys('')
        rua['element'].send_keys('')
        # botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

        # print(driver.page_source)
        assert (is__valid_by_required([username, email, telefone, senha, senha2, rua, bairro, uf, cidade, first_name]) is True)

    @allure.testcase("Testando o Campo usuario igual")
    def test_cadastro_campo_usuario_igual(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        #self.assertIn("WorkBook", driver.title)
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
        # assert "Informe outro nome de usuário!" in result
        assert("Informe outro nome de usuário!" in result)

    @allure.testcase("Testando o Campo usuario tamamho max de 150")
    def test_cadastro_campo_usuario_tamanho(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        #self.assertIn("WorkBook", driver.title)
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
        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste" * 170)
        # Preencher nome
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys("emailteste" * 160)
        # Preencher email
        driver.find_element_by_xpath('//*[@id="email"]').send_keys("emailteste@gmail.com")
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
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys("123456")
        # Preencher confirmar senha
        driver.find_element_by_xpath('//*[@id="senha2"]').send_keys("123456")
        username = get__input_by_id(inputs=find__inputs(driver), id='username')
        # botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

        try:
            result = driver.find_element_by_class_name('alert-danger').text
        except:
            result = ""
        print("RESULT -> ", result)
        # assert "Informe outro nome de usuário!" in result
        assert("Esse campo so aceita no maximo 150 caracteres." in result and
                        is__valid_by_max_length(element=username, length=150) is True)

    @allure.testcase("Testando o Campo nome tamamho max de 150")
    def test_cadastro_campo_nome_tamanho(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        #self.assertIn("WorkBook", driver.title)
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
        # print("RESULT -> ", result)
        # assert "Informe outro nome de usuário!" in result
        assert("Esse campo so aceita no maximo 150 caracteres." in result)

    @allure.testcase("Testando o Campo email invalido")
    def test_cadastro_campo_email_invalido(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        #self.assertIn("WorkBook", driver.title)
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
        # print("Resuslt--->", result)
        # assert "Email Inválido!" in result
        assert("Email Inválido!" in result)

    @allure.testcase("Testando o Campo email igual")
    def test_cadastro_campo_email_igual(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        #self.assertIn("WorkBook", driver.title)
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
        print("Resultado---->", result)
        # assert "Email já existente para um usuário!" in result
        assert("Email já existente para um usuário!" in result)

    @allure.testcase("Testando o Campo email com caractere especial")
    def test_cadastro_campo_email_caractere_especial(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        #self.assertIn("WorkBook", driver.title)
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
        driver.find_element_by_xpath('//*[@id="email"]').send_keys("téte@gmail.com")
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
        print("Resultado---->", result)
        # assert "Email já existente para um usuário!" in result
        assert("required" in driver.page_source)

    @allure.testcase("Testando o Campo email com espaço")
    def test_cadastro_campo_email_com_espaco(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        #self.assertIn("WorkBook", driver.title)
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
        driver.find_element_by_xpath('//*[@id="email"]').send_keys("t1   @gmail.com")
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

        # result = driver.find_element_by_class_name('alert-danger').text
        # print("Resultado---->", result)
        # assert "Email já existente para um usuário!" in result
        assert("required" in driver.page_source)

    @allure.testcase("Testando o Campo email tamamho max de 254")
    def test_cadastro_campo_email_tamanho(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        #self.assertIn("WorkBook", driver.title)
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
        driver.find_element_by_xpath('//*[@id="email"]').send_keys("f" * 255 + "@gmail.com")
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
        assert("Esse campo so aceita no maximo 254 caracteres." in result)

    @allure.testcase("Testando o Campo telefone valido")
    def test_cadastro_campo_telefone_valido(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        #self.assertIn("WorkBook", driver.title)
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
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys(99999999999)
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
        # print("RESULT -> ", result)

        assert("Usuário Registrado com Sucesso!" in result)

    @allure.testcase("Testando o Campo telefone tamamho max de 15")
    def test_cadastro_campo_telefone_tamanho_max(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        #self.assertIn("WorkBook", driver.title)
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
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys(999999999999999999999999)
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
        # print("RESULT -> ", result)

        assert("Informe no máximo 15 números." in result)

    @allure.testcase("Testando o Campo telefone tamamho minimo 11 digitos")
    def test_cadastro_campo_telefone_tamanho_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        #self.assertIn("WorkBook", driver.title)
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
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys(999999)
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
        # print("RESULT -> ", result)

        assert("Informe no minimo 11 números." in result)

    @allure.testcase("Testando o Campo telefone inserindo caracteres")
    def test_cadastro_campo_telefone_inserindo_caractere(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        #self.assertIn("WorkBook", driver.title)
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

        assert("Informe somente números nesse campo." in result)

    @allure.testcase("Testando o Campo senha menor 6 numeros")
    def test_cadastro_campo_senha_menor_6(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        #self.assertIn("WorkBook", driver.title)
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

        # assert "Senha precisa ter pelo menos 6 Caracteres!" in result
        assert("Senha precisa ter pelo menos 6 Caracteres!" in result)

    @allure.testcase("Testando o Campo senha tamanho max 128")
    def test_cadastro_campo_senha_tamanho_max(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        #self.assertIn("WorkBook", driver.title)
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

        assert("Esse campo so aceita no maximo 128 caracteres." in result)

    @allure.testcase("Testando o Campo usuario tamamho minimo de 1 caractere")
    def test_cadastro_campo_usuario_tamanho_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        #self.assertIn("WorkBook", driver.title)
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
        driver.find_element_by_xpath('//*[@id="username"]').send_keys("t")
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
        # print("RESULT -> ", result)
        # assert "Informe outro nome de usuário!" in result
        assert("Usuário Registrado com Sucesso!" in result)

    @allure.testcase("Testando o Campo nome tamamho minimo de 1 caractere")
    def test_cadastro_campo_nome_tamanho_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        #self.assertIn("WorkBook", driver.title)
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
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys("r")
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
        # print("RESULT -> ", result)
        # assert "Informe outro nome de usuário!" in result
        assert("Usuário Registrado com Sucesso!" in result)

    @allure.testcase("Testando o Campo email tamamho minimo de 1 caractere")  # não e possivel testar
    def test_cadastro_campo_nome_tamanho_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        #self.assertIn("WorkBook", driver.title)
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
        driver.find_element_by_xpath('//*[@id="email"]').send_keys("a")
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
        # assert "Informe outro nome de usuário!" in result
        assert("Email incompleto!" in result)

    @allure.testcase("Testando o Campo senha minimo 1 caractere")
    def test_cadastro_campo_senha_tamanho_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        #self.assertIn("WorkBook", driver.title)
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
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys("1")
        # Preencher confirmar senha
        driver.find_element_by_xpath('//*[@id="senha2"]').send_keys(senha)
        # botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

        result = driver.find_element_by_class_name('alert-danger').text

        # assert "Senha precisa ter pelo menos 6 Caracteres!" in result
        assert("Senha precisa ter pelo menos 6 Caracteres!" in result)

    @allure.testcase("Testando o Campo cidade minimo 1 caractere")
    def test_cadastro_campo_cidade_tamanho_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        # self.assertIn("WorkBook", driver.title)
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
        driver.find_element_by_xpath('//*[@id="cidade"]').send_keys("a")
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


        assert ("Usuário Registrado com Sucesso!" in result)

    @allure.testcase("Testando o Campo cidade max 40 caractere")#verificar
    def test_cadastro_campo_cidade_tamanho_max(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        # self.assertIn("WorkBook", driver.title)
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
        driver.find_element_by_xpath('//*[@id="cidade"]').send_keys("a" * 50)
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

        assert ("Usuário Registrado com Sucesso!" in result)

    @allure.testcase("Testando o Campo rua minimo 1 caractere")
    def test_cadastro_campo_rua_tamanho_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        # self.assertIn("WorkBook", driver.title)
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
        driver.find_element_by_xpath('//*[@id="rua"]').send_keys("d")
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

        assert ("Usuário Registrado com Sucesso!" in result)

    @allure.testcase("Testando o Campo rua max 40 caractere")  # verificar
    def test_cadastro_campo_rua_tamanho_max(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        # self.assertIn("WorkBook", driver.title)
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
        driver.find_element_by_xpath('//*[@id="rua"]').send_keys("a" * 65)
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

        assert ("Usuário Registrado com Sucesso!" in result)

    @allure.testcase("Testando o Campo uf minimo 1 caractere")
    def test_cadastro_campo_uf_tamanho_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        # self.assertIn("WorkBook", driver.title)
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
        driver.find_element_by_xpath('//*[@id="uf"]').send_keys("a")
        # Preencher bairro
        driver.find_element_by_xpath('//*[@id="bairro"]').send_keys(bairro)
        # Preencher senha
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys(senha)
        # Preencher confirmar senha
        driver.find_element_by_xpath('//*[@id="senha2"]').send_keys(senha)
        # botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

        result = driver.find_element_by_class_name('alert-success').text

        assert ("Usuário Registrado com Sucesso!" in result)

    @allure.testcase("Testando o Campo uf max 2 caractere")  # verificar
    def test_cadastro_campo_uf_tamanho_max(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        # self.assertIn("WorkBook", driver.title)
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
        driver.find_element_by_xpath('//*[@id="uf"]').send_keys("A" * 3)
        # Preencher bairro
        driver.find_element_by_xpath('//*[@id="bairro"]').send_keys(bairro)
        # Preencher senha
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys(senha)
        # Preencher confirmar senha
        driver.find_element_by_xpath('//*[@id="senha2"]').send_keys(senha)
        # botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

        result = driver.find_element_by_class_name('alert-danger').text

        assert ("Usuário Registrado com Sucesso!" in result)

    @allure.testcase("Testando o Campo bairro minimo 1 caractere")
    def test_cadastro_campo_bairro_tamanho_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        # self.assertIn("WorkBook", driver.title)
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
        driver.find_element_by_xpath('//*[@id="bairro"]').send_keys("a")
        # Preencher senha
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys(senha)
        # Preencher confirmar senha
        driver.find_element_by_xpath('//*[@id="senha2"]').send_keys(senha)
        # botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

        result = driver.find_element_by_class_name('alert-success').text

        assert ("Usuário Registrado com Sucesso!" in result)

    @allure.testcase("Testando o Campo bairro max 40 caractere")  # verificar
    def test_cadastro_campo_bairro_tamanho_max(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        # self.assertIn("WorkBook", driver.title)
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
        driver.find_element_by_xpath('//*[@id="bairro"]').send_keys("q" * 50)
        # Preencher senha
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys(senha)
        # Preencher confirmar senha
        driver.find_element_by_xpath('//*[@id="senha2"]').send_keys(senha)
        # botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

        result = driver.find_element_by_class_name('alert-danger').text

        assert ("Usuário Registrado com Sucesso!" in result)



    def tearDown(self):
        self.driver.close()



