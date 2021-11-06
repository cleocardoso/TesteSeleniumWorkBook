import random
import unittest
import webbrowser

import allure
import time

import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.errorhandler import ErrorHandler


class Utils:

    def __utils__(self, array):
        size = len(array) - 1
        return array[int(random.uniform(0, size))]

    def generate(self):
        def __generate__city():
            resp = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/24/municipios')
            array = []
            if resp.status_code == 200:
                for json in resp.json():
                    name = json['microrregiao']['nome']
                    uf = json['microrregiao']['mesorregiao']['UF']['sigla']
                    obj = {
                        "city": name,
                        "uf": uf
                    }
                    array.append(obj)
            return self.__utils__(array=array)

        def __generate__district():
            return f'Av. {__generate__name().capitalize()} {__generate__name__last()}'

        def __generate__road():
            return f'Rua {__generate__name().capitalize()} {__generate__name__last()}'

        def __generate__name():
            resp = requests.get('https://servicodados.ibge.gov.br/api/v2/censos/nomes')
            array = []
            if resp.status_code == 200:
                for json in resp.json():
                    name = json['nome']
                    array.append(name)
            return self.__utils__(array=array)

        def __generate__name__last():
            names_last = [
                "Da silva",
                "Dos santos",
                "Pereira",
                "Alves",
                "Ferreira",
                "De oliveira",
                "Silva",
                "Rodrigues",
                "De souza",
                "Gomes",
                "Santos",
                "Oliveira",
                "Ribeiro",
                "Martins",
                "Soares",
                "Barbosa",
                "Lopes",
                "Vieira",
                "Souza",
                "Fernandes",
                "Lima",
                "Costa",
                "Batista",
                "Dias",
                "Moreira",
                "Nunes",
                "De lima",
                "De sousa",
                "Da costa",
                "De almeida",
                "Mendes",
                "Carvalho",
                "Araujo",
                "Cardoso",
                "Teixeira",
                "Marques",
                "Do nascimento",
                "Almeida",
                "Ramos",
                "Machado",
                "Rocha",
                "Nascimento",
                "De araujo",
                "Bezerra",
                "Sousa",
                "Borges",
                "Santana",
                "De carvalho",
                "Aparecido",
                "Pinto",
                "Pinheiro",
                "Monteiro",
                "Andrade",
                "Leite",
                "Correa",
                "Nogueira",
                "Garcia",
                "De freitas",
                "Henrique",
                "Tavares",
                "Coelho",
                "Pires",
                "De paula",
                "Correia",
                "Miranda",
                "De jesus",
                "Duarte",
                "Freitas",
                "Barros",
                "De andrade",
                "Campos",
                "De melo",
                "Da cruz",
                "Reis",
                "Moraes",
                "Do carmo",
                "Gonçalves",
                "Guimaraes",
                "Dos reis",
                "Viana",
                "De castro",
                "Silveira",
                "Moura",
                "Brito",
                "Neves",
                "Carneiro",
                "Melo",
                "Medeiros",
                "Cordeiro",
                "Farias",
                "Dantas",
                "Cavalcante",
                "Da rocha",
                "De assis",
                "Braga",
                "Cruz",
                "De lourdes",
                "Siqueira",
                "Macedo",
                "Antunes",
                "Castro",
                "Maciel",
                "Cunha",
                "Morais",
                "Fonseca",
                "Menezes",
                "De moraes",
                "Maia",
                "De moura",
                "Barreto",
                "Dacunha",
                "Chaves",
                "Magalhaes",
                "Azevedo",
                "Matos",
                "Torres",
                "Queiroz",
                "Freire",
                "Domingos",
                "Mota",
                "Sales",
                "Cabral",
                "Sampaio",
                "Amaral",
                "Leal",
                "Caetano",
                "Bueno",
                "Guedes",
                "Bispo",
                "Vasconcelos",
                "Amorim",
                "Franco",
                "De santana",
                "De brito",
                "Das gracas",
                "Marinho",
                "Aguiar",
                "Figueiredo",
                "Rosa",
                "Bastos",
                "Franca",
                "Inacio",
                "De barros",
                "Evangelista",
                "Pacheco",
                "Diniz",
                "Camargo",
                "Lemos",
                "Faria",
                "Bento",
                "Dos anjos",
                "Da silveira",
                "Mendonca",
                "De azevedo",
                "Sántos",
                "Filho",
                "Neto",
                "Dutra",
                "Paiva",
                "De morais",
                "Matias",
                "Muniz",
                "Simoes",
                "Domingues",
                "Santiago",
                "Da rosa",
                "Gonzaga",
                "Feitosa",
                "Coutinho",
                "Ferraz",
                "De abreu",
                "Peixoto",
                "Chagas",
                "Albuquerque",
                "Vaz",
                "Brandao",
                "Trindade",
                "De campos",
                "Rezende",
                "Nonato",
                "Assis",
                "De medeiros",
                "Afonso",
                "Abreu",
                "Teles",
                "De matos",
                "Pessoa",
                "Cavalcanti",
                "Furtado",
                "Pimentel",
                "Lacerda",
                "Braz",
                "Mesquita",
                "Messias",
                "Pontes",
                "Fagundes",
                "Da luz",
                "Cezar",
                "Arruda",
                "Da fonseca",
                "Saraiva",
                "Xavier",
                "Sanches",
                "Prado",
                "De sa",
                "Do amaral",
                "De cassia",
                "Sena",
                "Peres",
                "Passos",
                "Alencar",
                "De faria",
                "Rodriguês",
                "Lira",
                "Custodio",
                "Galvao",
                "Porto",
                "De queiroz",
                "Damasceno",
                "Cerqueira",
                "Deaguiar",
                "Firmino",
                "De mello",
                "Das dores",
                "Roque",
                "Pedroso",
                "Barroso",
                "De paiva",
                "Das chagas",
                "Das",
                "Lisboa",
                "Bernardes",
                "Vargas",
                "Lins",
                "Rabelo",
                "Do socorro",
                "Demiranda",
                "Barboza",
                "Paes",
                "Bandeira",
                "De albuquerque",
                "Resende",
                "Gama",
                "Baptista",
                "De farias",
                "Mello",
                "De franca",
                "Ramalho",
                "Vilela",
                "Pimenta",
                "De macedo",
                "Vidal",
                "Rangel",
                "Couto",
                "Amaro",
                "Francisco",
                "De menezes",
                "Veloso",
                "Lemes",
                "Flores",
                "Guerra",
                "Rossi",
                "Padilha",
                "Tomaz",
                "De camargo",
                "Moreno",
                "Esteves",
                "Brasil",
                "Henrique da silva",
                "Do rosario",
                "Muller",
                "Botelho",
                "Tenorio",
                "De arruda",
                "Serafim",
                "Fontes",
                "Do prado",
                "Leao",
                "De amorim",
                "De siqueira",
                "Goulart",
                "Dasneves",
                "Ventura",
                "Ferrari",
                "De vasconcelos",
                "Sobrinho",
                "Aquino",
                "Assuncao",
                "Nobre",
                "Simao",
                "Motta",
                "Bonfim",
                "De aquino",
                "Alcantara",
                "Da penha",
                "Novaes",
                "De deus",
                "Gouveia",
                "Toledo",
                "Holanda"
            ]
            return self.__utils__(array=names_last)

        def __generate__email(value):
            dominios = ['@gmail.com', '@hotmail.com', '@outlook.com.br', '@outlook.com']
            return value.lower() + self.__utils__(dominios)

        name = __generate__name()
        last_name = __generate__name__last()
        objCity = __generate__city()
        obj = {
            "first_name": name.capitalize(),  # primeiro nome
            "last_name": last_name,  # segundo nome
            "name_complete": name.capitalize() + " " + last_name,  # nome completo
            "email": __generate__email(name),  # email
            "password": "@" + name.lower(),  # senha
            "username": name.lower(),  # username
            "city": objCity['city'],  # cidade
            "uf": objCity['uf'],  # UF
            "district": __generate__district(),  # bairro
            "road": __generate__road(),  # rua
        }
        return obj



class TestCadastro(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome(executable_path=r"D:\Downloads\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome()
        #self.driver.get("http://127.0.0.1:8000/cadastro/")

    @allure.testcase("Testando o Cadastrar valido")
    def test_cadastro_campos_validos(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        obj = Utils().generate()
        nome = obj['username']
        email = obj['email']
        cidade = obj['city']
        rua = obj['road']
        uf = obj['uf']
        bairro = obj['district']
        senha = obj['password']
        #Preencher usuario
        driver.find_element_by_xpath('//*[@id="username"]').send_keys(nome)
        # Preencher nome
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(nome)
        # Preencher email
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        # Preencher telefone
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys("99999999999")
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
        #botao
        driver.find_element_by_xpath('//*[@id="show_class"]/div[11]/button').click()


        result = driver.find_element_by_class_name('alert-success').text


        assert "Usuário Registrado com Sucesso!" in result

    def test_cadastro_campos_vazio(self):
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

        assert "Preencha todos os Campos!" in result

    @allure.testcase("Testando o Campo usuario igual")
    def test_cadastro_campo_usuario_igual(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        obj = Utils().generate()
        nome = obj['username']
        email = obj['email']
        cidade = obj['city']
        rua = obj['road']
        uf = obj['uf']
        bairro = obj['district']
        senha = obj['password']
        # Preencher usuario
        driver.find_element_by_xpath('//*[@id="username"]').send_keys("ana")
        # Preencher nome
        driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(nome)
        # Preencher email
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        # Preencher telefone
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys("999999999")
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
        #print("RESULT -> ", result)


    @allure.testcase("Testando o Campo email invalido")
    def test_cadastro_campo_email_invalido(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        obj = Utils().generate()
        nome = obj['username']
        email = obj['email']
        cidade = obj['city']
        rua = obj['road']
        uf = obj['uf']
        bairro = obj['district']
        senha = obj['password']
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
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys("99999999999")
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
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        obj = Utils().generate()
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
        driver.find_element_by_xpath('//*[@id="email"]').send_keys("teste@gmail.com")
        # Preencher telefone
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys("99999999999")
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

    @allure.testcase("Testando o Campo telefone maior de 15 numeros")
    def test_cadastro_campo_telefone_maior(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        obj = Utils().generate()
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
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys("aaa")
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
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        obj = Utils().generate()
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
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys("aaa")
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
        driver.get("http://127.0.0.1:8000/cadastro/")
        self.assertIn("WorkBook", driver.title)
        obj = Utils().generate()
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
        driver.find_element_by_xpath('//*[@id="telefone"]').send_keys("999999999999999999")
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