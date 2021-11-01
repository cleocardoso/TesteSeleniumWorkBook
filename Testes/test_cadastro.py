import unittest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestCadastro(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome(executable_path=r"D:\Downloads\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome()
        #self.driver.get("http://127.0.0.1:8000/cadastro/")

    @allure.testcase("Testando o Cadastrar valido")
    def test_cadastro(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        #Preencher usuario
        driver.find_element_by_xpath('//*[@id="username"]').send_keys("test24")
        # Preencher nome
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys("Teste do sistema")
        # Preencher email
        driver.find_element_by_xpath('//*[@id="email"]').send_keys("test24@gmail.com")
        # Preencher telefone
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys("999999999")
        # Preencher cidade
        driver.find_element_by_xpath('//*[@id="cidade"]').send_keys("Pau Dos Ferros")
        # Preencher rua
        driver.find_element_by_xpath('//*[@id="rua"]').send_keys("São João")
        # Preencher uf
        driver.find_element_by_xpath('//*[@id="uf"]').send_keys("RN")
        # Preencher bairro
        driver.find_element_by_xpath('//*[@id="bairro"]').send_keys("Centro ")
        # Preencher senha
        driver.find_element_by_xpath('//*[@id="senha"]').send_keys("123456")
        # Preencher confirmar senha
        driver.find_element_by_xpath('//*[@id="senha2"]').send_keys("123456")
        #botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

        #result = driver.find_element_by_xpath('/html/body/main/div/div[1]').text
        result = driver.find_element_by_class_name('alert-success').text
        print("RESULT -> ",result)
       # time.sleep(20)
       # print("TESTE:",result)
        assert "Usuário Registrado com Sucesso!" in result

    def test_cadastro_vazio(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        #Preencher usuario
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
        #botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()

        #result = driver.find_element_by_xpath('/html/body/main/div/div[1]').text
        result = driver.find_element_by_class_name('alert-danger').text
        #print("RESULT -> ",result)
        #time.sleep(1000)
       # print("TESTE:",result)
        assert "Preencha todos os Campos!" in result




    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()