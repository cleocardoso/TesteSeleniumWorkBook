import unittest
import pytest
import allure
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from utils.input import find__inputs, is__valid_by_max_length, get__element_by_id, find__inputs__textarea, \
    find__by_elements


@pytest.mark.usefixtures("setup")
class TestAvaliarProfissional:

    @allure.testcase("Avaliar Profissional valido")
    def test_Avaliar_profissional_valido(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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
        nota = driver.find_element_by_xpath('//*[@id="show_class"]/div[1]/div/input[4]').get_attribute("value")
        print(nota)
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("Bom")
        msg = driver.find_element_by_xpath('//*[@id="id_descricao"]').get_attribute("value")

        driver.find_element_by_xpath('//*[@id="show_class"]/div[3]/button').click()

        driver.forward()
        time.sleep(2)
        driver.find_element_by_name("termo").send_keys("manicure")
        driver.find_element_by_name("termo").send_keys(Keys.RETURN)

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[1]/div/div/div/div/a/h5').click()

        driver.forward()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div/div/div[1]/div/div[2]/a').click()

        elemets = driver.find_elements_by_class_name("tab-content")
        descricao = elemets[0].find_elements_by_class_name('post-content')[0].find_element_by_tag_name('p').text
        n = elemets[0].find_elements_by_class_name('text-muted')[0].find_element_by_tag_name('small').text
        print(descricao,  n[6:7])
        assert (descricao == msg) and (nota == n[6:7])

    @allure.testcase("Avaliar Profissional campo vazio")
    def test_Avaliar_profissional_vazio(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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

        driver.find_element_by_xpath('//*[@id="show_class"]/div[1]/div').click()
        nota = driver.find_element_by_xpath('//*[@id="show_class"]/div[1]/div').get_attribute("value")
        print(nota)
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("")
        msg = driver.find_element_by_xpath('//*[@id="id_descricao"]').get_attribute("value")

        driver.find_element_by_xpath('//*[@id="show_class"]/div[3]/button').click()

        driver.forward()
        time.sleep(2)
        driver.find_element_by_name("termo").send_keys("manicure")
        driver.find_element_by_name("termo").send_keys(Keys.RETURN)

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[1]/div/div/div/div/a/h5').click()

        driver.forward()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div/div/div[1]/div/div[2]/a').click()

        elemets = driver.find_elements_by_class_name("tab-content")
        descricao = elemets[0].find_elements_by_class_name('post-content')[0].find_element_by_tag_name('p').text
        n = elemets[0].find_elements_by_class_name('text-muted')[0].find_element_by_tag_name('small').text
        print(descricao, n[6:7])
        assert (descricao != msg) and (nota != n[6:7])

    @allure.testcase("Avaliar Profissional nota minima")
    def test_Avaliar_profissional_nota_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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

        driver.find_element_by_xpath('//*[@id="show_class"]/div[1]/div/label[1]').click()
        nota = driver.find_element_by_xpath('//*[@id="show_class"]/div[1]/div/input[2]').get_attribute("value")
        print(nota)
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("otimo")
        msg = driver.find_element_by_xpath('//*[@id="id_descricao"]').get_attribute("value")

        driver.find_element_by_xpath('//*[@id="show_class"]/div[3]/button').click()

        driver.forward()
        time.sleep(2)
        driver.find_element_by_name("termo").send_keys("manicure")
        driver.find_element_by_name("termo").send_keys(Keys.RETURN)

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[1]/div/div/div/div/a/h5').click()

        driver.forward()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div/div/div[1]/div/div[2]/a').click()

        elemets = driver.find_elements_by_class_name("tab-content")
        descricao = elemets[0].find_elements_by_class_name('post-content')[0].find_element_by_tag_name('p').text
        n = elemets[0].find_elements_by_class_name('text-muted')[0].find_element_by_tag_name('small').text
        print(descricao, n[6:7])
        assert (nota == n[6:7])

    @allure.testcase("Avaliar Profissional nota maxima")
    def test_Avaliar_profissional_nota_max(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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
        nota = driver.find_element_by_xpath('//*[@id="show_class"]/div[1]/div/input[6]').get_attribute("value")
        print(nota)
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("otimo")
        msg = driver.find_element_by_xpath('//*[@id="id_descricao"]').get_attribute("value")

        driver.find_element_by_xpath('//*[@id="show_class"]/div[3]/button').click()

        driver.forward()
        time.sleep(2)
        driver.find_element_by_name("termo").send_keys("manicure")
        driver.find_element_by_name("termo").send_keys(Keys.RETURN)

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[1]/div/div/div/div/a/h5').click()

        driver.forward()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div/div/div[1]/div/div[2]/a').click()

        elemets = driver.find_elements_by_class_name("tab-content")
        descricao = elemets[0].find_elements_by_class_name('post-content')[0].find_element_by_tag_name('p').text
        n = elemets[0].find_elements_by_class_name('text-muted')[0].find_element_by_tag_name('small').text
        print(descricao, n[6:7])
        assert (nota == n[6:7])

    @allure.testcase("Avaliar Profissional descricao minima")
    def test_Avaliar_profissional_descricao_min(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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
        nota = driver.find_element_by_xpath('//*[@id="show_class"]/div[1]/div/input[4]').get_attribute("value")
        print(nota)
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("B")
        msg = driver.find_element_by_xpath('//*[@id="id_descricao"]').get_attribute("value")

        driver.find_element_by_xpath('//*[@id="show_class"]/div[3]/button').click()

        driver.forward()
        time.sleep(2)
        driver.find_element_by_name("termo").send_keys("manicure")
        driver.find_element_by_name("termo").send_keys(Keys.RETURN)

        driver.forward()
        driver.find_element_by_xpath('/html/body/main/div[1]/div/div/div/div/a/h5').click()

        driver.forward()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/main/div[3]/div/div/div/div/div[1]/div/div[2]/a').click()

        elemets = driver.find_elements_by_class_name("tab-content")
        descricao = elemets[0].find_elements_by_class_name('post-content')[0].find_element_by_tag_name('p').text
        n = elemets[0].find_elements_by_class_name('text-muted')[0].find_element_by_tag_name('small').text
        print(descricao, n[6:7])
        assert (descricao == msg)

    @allure.testcase("Avaliar Profissional descricao maxima")  # não foi possivel realizar
    def test_Avaliar_profissional_descricao_max(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/submit_login/")

        driver.find_element_by_xpath('//*[@id="username"]').send_keys("21")
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
        nota = driver.find_element_by_xpath('//*[@id="show_class"]/div[1]/div/input[4]').get_attribute("value")
        print(nota)
        driver.find_element_by_xpath('//*[@id="id_descricao"]').send_keys("B" * 251)

        text_area = find__by_elements(driver=driver, tag_name='textarea')
        descricao = get__element_by_id(elements=text_area, id='id_descricao')
        is_valid = is__valid_by_max_length(element=descricao, length=250) is True
        driver.find_element_by_xpath('//*[@id="show_class"]/div[3]/button').click()

        assert is_valid is True

    def tearDown(self):
        self.driver.close()






