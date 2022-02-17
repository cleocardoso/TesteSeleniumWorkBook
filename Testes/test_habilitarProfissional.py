
import pytest
import allure
import time
from utils.input import find__inputs, get__elements, is__valid_by_required, get__element_by_id, \
    is__valid_by_max_length,get__input_by_required, find__by_elements
@pytest.mark.usefixtures("setup")
class TestHabilitarProfissional:

    @allure.testcase("Testando o Campos habilitar profissional valido")
    def test_habilitar_profissional_valido(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste2")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/aside/ul/li[2]/a/span').click()

        driver.forward()

        driver.find_element_by_xpath('//*[@id="id_profissao"]').send_keys("Professora")
        driver.find_element_by_xpath('//*[@id="id_categoria"]').send_keys("Aulas")
        driver.find_element_by_xpath('//*[@id="id_imagem"]').send_keys("D://Area de Trabalho/teste/001.jpg")
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("Aulas de Programação")

        driver.find_element_by_xpath('//html/body/main/div[2]/div/div/div/div/form/div[5]/button').click()

        result = driver.find_element_by_class_name('alert-success').text

        #assert "Perfil profissional adicionado com sucesso!" in result
        assert "Perfil profissional adicionado com sucesso!" in result

    @allure.testcase("Testando o Campos habilitar profissional campos vazio")
    def test_habilitar_profissional_campos_vazio(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/aside/ul/li[2]/a/span').click()
        time.sleep(2)
        # campos
        inputs = find__by_elements(driver=driver, tag_name='input')
        selects = find__by_elements(driver=driver, tag_name='select')
        text_areas = find__by_elements(driver=driver, tag_name='textarea')
        profissao = get__element_by_id(elements=inputs, id='id_profissao')
        categoria = get__element_by_id(elements=selects, id='id_categoria')
        #imagem = get__element_by_id(inputs=inputs, id='id_imagem')
        descricao = get__element_by_id(elements=text_areas, id='id_descricao')

        # Preencher usuario
        profissao['element'].send_keys('')
        categoria['element'].send_keys('Selecione')
        #imagem['element'].send_keys('')
        descricao['element'].send_keys('')
        print("aqui==>",profissao)
        #print("aqui==>", categoria)
        print("aqui==>", descricao)
        is_valid = is__valid_by_required([profissao, categoria, descricao])
        # botao
        driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/form/div[5]/button').click()

        # print(driver.page_source)
        assert is_valid is True

    @allure.testcase("Testando o Campos habilitar profissional campo profissão com no minimo 3 caracteres")
    def test_habilitar_profissional_campo_profissão_tamanho_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("2")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/aside/ul/li[2]/a/span').click()

        driver.forward()

        driver.find_element_by_xpath('//*[@id="id_profissao"]').send_keys("AD")
        driver.find_element_by_xpath('//*[@id="id_categoria"]').send_keys("Aulas")
        #driver.find_element_by_xpath('//*[@id="id_imagem"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("aluas de ingles")

        driver.find_element_by_xpath('//html/body/main/div[2]/div/div/div/div/form/div[5]/button').click()

        result = driver.find_element_by_class_name('alert-success').text

        assert "Insira pelo menos 3 caracteres!" in result

    @allure.testcase("Testando o Campos habilitar profissional campo descrição com no minimo 1 caracteres")
    def test_habilitar_profissional_campo_descrição_tamanho_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("5")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/aside/ul/li[2]/a/span').click()

        driver.forward()

        driver.find_element_by_xpath('//*[@id="id_profissao"]').send_keys("g")
        driver.find_element_by_xpath('//*[@id="id_categoria"]').send_keys("Aulas")
        # driver.find_element_by_xpath('//*[@id="id_imagem"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("a")

        driver.find_element_by_xpath('//html/body/main/div[2]/div/div/div/div/form/div[5]/button').click()

        result = driver.find_element_by_class_name('alert-success').text

        assert "Perfil profissional adicionado com sucesso!" in result

    @allure.testcase("Testando o Campos habilitar profissional campo profissão com no max 250")
    def test_habilitar_profissional_campo_profissão_tamanho_max(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("1")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/aside/ul/li[2]/a/span').click()

        driver.forward()
        driver.find_element_by_xpath('//*[@id="id_profissao"]').send_keys("A" * 251)
        driver.find_element_by_xpath('//*[@id="id_categoria"]').send_keys("Aulas")
        # driver.find_element_by_xpath('//*[@id="id_imagem"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("aluas de ingles")

        inputs = find__inputs(driver=driver)
        profissao = get__element_by_id(elements=inputs, id="id_profissao")
        is_valid = is__valid_by_max_length(element=profissao, length=250) is True
        driver.find_element_by_xpath('//html/body/main/div[2]/div/div/div/div/form/div[5]/button').click()

        # print("Result====>", result)
        assert is_valid is True

    @allure.testcase("Testando o Campos habilitar profissional campo descrição com no max 250") #errooooooo funcao
    def test_habilitar_profissional_campo_descricaoo_tamanho_max(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/aside/ul/li[2]/a/span').click()

        driver.forward()

        driver.find_element_by_xpath('//*[@id="id_profissao"]').send_keys("ADS")
        driver.find_element_by_xpath('//*[@id="id_categoria"]').send_keys("Aulas")
        # driver.find_element_by_xpath('//*[@id="id_imagem"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("aluas de ingles"  * 251)

        text_area = find__by_elements(driver=driver, tag_name='textarea')
        descricao = get__element_by_id(elements=text_area, id='id_descricao')
        is_valid = is__valid_by_max_length(element=descricao, length=250) is True
        driver.find_element_by_xpath('//html/body/main/div[2]/div/div/div/div/form/div[5]/button').click()

        # print("Result====>", result)
        assert is_valid is True

    def tearDown(self):
        self.driver.close()


