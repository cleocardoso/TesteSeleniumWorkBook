
import allure
import time
import pytest
import numpy as np

from utils.input import get__inputs, get__input_by_required, is__valid_by_required, find__inputs, find__inputs_by_xpath, is__valid_by_input_max_length, is__valid_by_max_length, get__input_by_id

@pytest.mark.usefixtures("setup")
class TestEditarDadosCliente:

    @allure.testcase("Testando o Editar cadastro cliente valido")
    def test_cadastro_editar_cliente_validos(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("2")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/aside/ul/li[4]/a/span').click()

        driver.forward()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div[2]/div/a').click()

        driver.forward()
        arrayEntrada = []
        arraySaida = []
        driver.find_element_by_xpath('//*[@id="id_username"]').clear()
        driver.find_element_by_xpath('//*[@id="id_username"]').send_keys("21")
        arrayEntrada.append(driver.find_element_by_xpath('//*[@id="id_username"]').get_attribute("value"))
        driver.find_element_by_xpath('//*[@id="id_first_name"]').clear()
        driver.find_element_by_xpath('//*[@id="id_first_name"]').send_keys("s")
        arrayEntrada.append(driver.find_element_by_xpath('//*[@id="id_first_name"]').get_attribute("value"))
        #arraySaida.append(driver.find_element_by_xpath('//*[@id="id_username"]').get_attribute("value"))
        driver.find_element_by_xpath('//*[@id="id_last_name"]').clear()
        driver.find_element_by_xpath('//*[@id="id_last_name"]').send_keys("testando")
        arrayEntrada.append(driver.find_element_by_xpath('//*[@id="id_last_name"]').get_attribute("value"))
        #arraySaida.append(driver.find_element_by_xpath('//*[@id="id_last_name"]').get_attribute("value"))
        driver.find_element_by_xpath('//*[@id="id_email"]').clear()
        driver.find_element_by_xpath('//*[@id="id_email"]').send_keys("testando@gmail.com")
        arrayEntrada.append(driver.find_element_by_xpath('//*[@id="id_email"]').get_attribute("value"))
        #arraySaida.append(driver.find_element_by_xpath('//*[@id="id_email"]').get_attribute("value"))
        driver.find_element_by_xpath('//*[@id="id_telefone"]').clear()
        driver.find_element_by_xpath('//*[@id="id_telefone"]').send_keys("99999999999")
        arrayEntrada.append(driver.find_element_by_xpath('//*[@id="id_telefone"]').get_attribute("value"))
        #arraySaida.append(driver.find_element_by_xpath('//*[@id="id_telefone"]').get_attribute("value"))
        driver.find_element_by_xpath('//*[@id="id_cidade"]').clear()
        driver.find_element_by_xpath('//*[@id="id_cidade"]').send_keys("testando")
        arrayEntrada.append(driver.find_element_by_xpath('//*[@id="id_cidade"]').get_attribute("value"))
        #arraySaida.append(driver.find_element_by_xpath('//*[@id="id_cidade"]').get_attribute("value"))
        driver.find_element_by_xpath('//*[@id="id_rua"]').clear()
        driver.find_element_by_xpath('//*[@id="id_rua"]').send_keys("testando")
        arrayEntrada.append(driver.find_element_by_xpath('//*[@id="id_rua"]').get_attribute("value"))
        #arraySaida.append(driver.find_element_by_xpath('//*[@id="id_rua"]').get_attribute("value"))
        driver.find_element_by_xpath('//*[@id="id_uf"]').clear()
        driver.find_element_by_xpath('//*[@id="id_uf"]').send_keys("2")
        #arrayEntrada.append(driver.find_element_by_xpath('//*[@id="id_uf"]').get_attribute("value"))
        #arraySaida.append(driver.find_element_by_xpath('//*[@id="id_uf"]').get_attribute("value"))
        driver.find_element_by_xpath('//*[@id="id_bairro"]').clear()
        driver.find_element_by_xpath('//*[@id="id_bairro"]').send_keys("testando")
        arrayEntrada.append(driver.find_element_by_xpath('//*[@id="id_bairro"]').get_attribute("value"))
        #arraySaida.append(driver.find_element_by_xpath('//*[@id="id_bairro"]').get_attribute("value"))

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        # result = driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div').text
        # print([result])
        # print("array " , arraySaida)
        # print(arraySaida in [result])
        table = driver.find_element_by_class_name("table")
        trs = table.find_elements_by_tag_name("tr")
        for tr in trs:
            arraySaida.append(tr.find_elements_by_tag_name("td")[0].text)
        arrayEntrada = np.array(arrayEntrada)
        arraySaida = np.array(arraySaida)
        print("\nentrada", arrayEntrada)
        print("saida", arraySaida)
        assert(np.array_equal(arrayEntrada, arraySaida) is True)

    @allure.testcase("Testando o Editar dados com campo usuario e nome vazio")  #verificar
    def test_cadastro_editar_cliente_vazio(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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
        driver.find_element_by_xpath('//*[@id="id_last_name"]').clear()
        driver.find_element_by_xpath('//*[@id="id_telefone"]').clear()
        driver.find_element_by_xpath('//*[@id="id_email"]').clear()
        #aqui vc pode colocar os demais inputs

        inputs = find__inputs(driver)
        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()
        username = get__input_by_required(inputs=inputs, id='id_username')
        last_name = get__input_by_required(inputs=inputs, id='id_last_name')
        email = get__input_by_required(inputs=inputs, id='id_email')
        telefone = get__input_by_required(inputs=inputs, id='id_telefone')
        # e aqui tb
        # e na funcao is__valid vc coloca dentro o array
        # ele vai verificar se existe o input com o required, se nao existe ele retorna False
        assert(is__valid_by_required([username, last_name, email, telefone]) is True)

    @allure.testcase("Testando o Editar dados com campo usuario com caractere especial")
    def test_cadastro_editar_usuario_caractere_especial(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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

        assert("Informe um nome de usuário válido." in result)

    @allure.testcase("Testando o Editar dados com campo usuario existente")#colocar email que ja exista
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

        assert("Um usuário com este nome de usuário já existe." in result)

    @allure.testcase("Testando o Editar dados com campo usuario com espaço")
    def test_cadastro_editar_usuario_com_espaco(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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

        assert("Este campo é obrigatório." in result)

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

        assert("Informe menos de 150 caracteres" in result)

    @allure.testcase("Testando o Editar dados com campo nome com espaço")
    def test_cadastro_editar_nome_com_espaco(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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

        assert("Este campo é obrigatório." in result)

    @allure.testcase("Testando o Editar dados com campo nome max 150")
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
        inputs = find__inputs(driver=driver)
        first_name = get__input_by_id(inputs=inputs, id="id_first_name")
        is_valid = is__valid_by_max_length(element=first_name, length=150) is True
        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        assert(is_valid is True)

    @allure.testcase("Testando o Editar dados com campo usuario com minimo 1 caractere")
    def test_cadastro_editar_usuario_tamanho_min(self):
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
        driver.find_element_by_xpath('//*[@id="id_username"]').send_keys("a")

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_xpath('//*[@id="error_1_id_username"]/strong').text

        # print("Result====>", result)

        assert("Dados alterados com sucesso" in result)

    @allure.testcase("Testando o Editar dados com campo nome com minimo 1 caractere")
    def test_cadastro_editar_nome_tamanho_min(self):
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
        driver.find_element_by_xpath('//*[@id="id_first_name"]').send_keys("a")

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_xpath('//*[@id="error_1_id_username"]/strong').text

        # print("Result====>", result)

        assert("Dados alterados com sucesso" in result)

    @allure.testcase("Testando o Editar dados com campo email com minimo ")#verificar
    def test_cadastro_editar_email_tamanho_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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
        driver.find_element_by_xpath('//*[@id="id_first_name"]').send_keys("a")

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_xpath('//*[@id="error_1_id_username"]/strong').text

        # print("Result====>", result)

        assert ("Dados alterados com sucesso" in result)

    @allure.testcase("Testando o Editar dados com campo email com max 254 ")  # verificar
    def test_cadastro_editar_email_tamanho_max(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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
        driver.find_element_by_xpath('//*[@id="id_first_name"]').send_keys("a")

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_xpath('//*[@id="error_1_id_username"]/strong').text

        # print("Result====>", result)

        assert ("Dados alterados com sucesso" in result)

    @allure.testcase("Testando o Editar dados com campo telefone com minimo 11 ")  # verificar
    def test_cadastro_editar_telefone_tamanho_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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
        driver.find_element_by_xpath('//*[@id="id_first_name"]').send_keys("a")

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_xpath('//*[@id="error_1_id_username"]/strong').text

        # print("Result====>", result)

        assert ("Dados alterados com sucesso" in result)

    @allure.testcase("Testando o Editar dados com campo telefone com max 15 ")  # verificar
    def test_cadastro_editar_telefone_tamanho_max(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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
        driver.find_element_by_xpath('//*[@id="id_first_name"]').send_keys("a")

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_xpath('//*[@id="error_1_id_username"]/strong').text

        # print("Result====>", result)

        assert ("Dados alterados com sucesso" in result)

    @allure.testcase("Testando o Editar dados com campo cidade com minimo 1 ")  # verificar
    def test_cadastro_editar_cidade_tamanho_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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
        driver.find_element_by_xpath('//*[@id="id_first_name"]').send_keys("a")

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_xpath('//*[@id="error_1_id_username"]/strong').text

        # print("Result====>", result)

        assert ("Dados alterados com sucesso" in result)

    @allure.testcase("Testando o Editar dados com campo cidade com max 40 ")  # verificar
    def test_cadastro_editar_cidade_tamanho_max(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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
        driver.find_element_by_xpath('//*[@id="id_first_name"]').send_keys("a")

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_xpath('//*[@id="error_1_id_username"]/strong').text

        # print("Result====>", result)

        assert ("Dados alterados com sucesso" in result)

    @allure.testcase("Testando o Editar dados com campo rua com minimo 1 ")  # verificar
    def test_cadastro_editar_rua_tamanho_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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
        driver.find_element_by_xpath('//*[@id="id_first_name"]').send_keys("a")

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_xpath('//*[@id="error_1_id_username"]/strong').text

        # print("Result====>", result)

        assert ("Dados alterados com sucesso" in result)

    @allure.testcase("Testando o Editar dados com campo rua com max 60 ")  # verificar
    def test_cadastro_editar_rua_tamanho_max(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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
        driver.find_element_by_xpath('//*[@id="id_first_name"]').send_keys("a")

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_xpath('//*[@id="error_1_id_username"]/strong').text

        # print("Result====>", result)

        assert ("Dados alterados com sucesso" in result)

    @allure.testcase("Testando o Editar dados com campo uf com minimo 1 ")  # verificar
    def test_cadastro_editar_uf_tamanho_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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
        driver.find_element_by_xpath('//*[@id="id_first_name"]').send_keys("a")

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_xpath('//*[@id="error_1_id_username"]/strong').text

        # print("Result====>", result)

        assert ("Dados alterados com sucesso" in result)

    @allure.testcase("Testando o Editar dados com campo uf com max 2 ")  # verificar
    def test_cadastro_editar_uf_tamanho_max(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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
        driver.find_element_by_xpath('//*[@id="id_first_name"]').send_keys("a")

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_xpath('//*[@id="error_1_id_username"]/strong').text

        # print("Result====>", result)

        assert ("Dados alterados com sucesso" in result)

    @allure.testcase("Testando o Editar dados com campo bairro com minimo 1 ")  # verificar
    def test_cadastro_editar_bairro_tamanho_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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
        driver.find_element_by_xpath('//*[@id="id_first_name"]').send_keys("a")

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_xpath('//*[@id="error_1_id_username"]/strong').text

        # print("Result====>", result)

        assert ("Dados alterados com sucesso" in result)

    @allure.testcase("Testando o Editar dados com campo bairro com max 40 ")  # verificar
    def test_cadastro_editar_bairro_tamanho_max(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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
        driver.find_element_by_xpath('//*[@id="id_first_name"]').send_keys("a")

        driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div/div/div/form/div[11]/div/button').click()

        result = driver.find_element_by_xpath('//*[@id="error_1_id_username"]/strong').text

        # print("Result====>", result)

        assert ("Dados alterados com sucesso" in result)

    def tearDown(self):
        self.driver.close()


