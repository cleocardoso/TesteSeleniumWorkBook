
import pytest
import allure
import time

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
        assert("Perfil profissional adicionado com sucesso!" in result)

    @allure.testcase("Testando o Campos habilitar profissional campos vazio")
    def test_habilitar_profissional_campos_vazio(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("teste")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")

        driver.find_element_by_xpath('//*[@id="submit_login"]').click()
        time.sleep(2)
        driver.forward()

        time.sleep(2)
        driver.find_element_by_xpath('/html/body/aside/ul/li[2]/a/span').click()

        driver.forward()

        driver.find_element_by_xpath('//*[@id="id_profissao"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="id_categoria"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="id_imagem"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("")

        driver.find_element_by_xpath('//html/body/main/div[2]/div/div/div/div/form/div[5]/button').click()

        result = driver.find_element_by_class_name('alert-danger').text

        assert("Preencha os campos!" in result)

    @allure.testcase("Testando o Campos habilitar profissional campo profissão com no minimo 3 caracteres")
    def test_habilitar_profissional_campo_profissão_tamanho_min(self):
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

        driver.find_element_by_xpath('//*[@id="id_profissao"]').send_keys("AD")
        driver.find_element_by_xpath('//*[@id="id_categoria"]').send_keys("Aulas")
        #driver.find_element_by_xpath('//*[@id="id_imagem"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("aluas de ingles")

        driver.find_element_by_xpath('//html/body/main/div[2]/div/div/div/div/form/div[5]/button').click()

        result = driver.find_element_by_class_name('alert-danger').text

        assert("Insira pelo menos 3 caracteres!" in result)

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

        driver.find_element_by_xpath('//*[@id="id_profissao"]').send_keys("geografia")
        driver.find_element_by_xpath('//*[@id="id_categoria"]').send_keys("Aulas")
        # driver.find_element_by_xpath('//*[@id="id_imagem"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("a")

        driver.find_element_by_xpath('//html/body/main/div[2]/div/div/div/div/form/div[5]/button').click()

        result = driver.find_element_by_class_name('alert-success').text

        assert("Perfil profissional adicionado com sucesso!" in result)

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

        driver.find_element_by_xpath('//html/body/main/div[2]/div/div/div/div/form/div[5]/button').click()

        result = driver.find_element_by_class_name('alert-danger').text

        assert("Informe menos de 250 caracteres" in result)

    @allure.testcase("Testando o Campos habilitar profissional campo descrição com no max 250")
    def test_habilitar_profissional_campo_descricaoo_tamanho_max(self):
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

        driver.find_element_by_xpath('//*[@id="id_profissao"]').send_keys("ADS")
        driver.find_element_by_xpath('//*[@id="id_categoria"]').send_keys("Aulas")
        # driver.find_element_by_xpath('//*[@id="id_imagem"]').send_keys("")
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("aluas de ingles"  * 251)

        driver.find_element_by_xpath('//html/body/main/div[2]/div/div/div/div/form/div[5]/button').click()

        result = driver.find_element_by_class_name('alert-danger').text

        assert("Informe menos de 250 caracteres" in result)

    def tearDown(self):
        self.driver.close()


