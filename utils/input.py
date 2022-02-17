from selenium.webdriver.common.by import By


def is__required(input=None):
    if input:
        return input
    return False


def get_attr(input=None, attr=''):
    if input:
        try:
            # print(input['element'])
            value = input.get_attribute(attr)
            if value:
                return value
        except Exception as e:
            print(e)
            return None
    return None


def get__input_by_required(inputs=[], id=None):
    elements = get__elements(inputs)
    if len(elements) == 0:
        return None
    for ele in elements:
        # print(ele)
        if ele['id'] == id:
            if ele['is_required'] == 'true':
                # print("AQUI==>",ele['is_required'])
                return ele
    return None


def get__element_by_id(elements=[], id=None):
    elements = get__elements(elements)
    if len(elements) == 0:
        return None
    for ele in elements:
        print(ele)
        if ele['id'] == id:
            print("element ", ele, "\n")
            return ele
    return None


def is__valid_by_required(elements):
    if len(elements) > 0:
        for ele in elements:
            if ele:
                if ele['is_required'] is False:
                    return False
            else:
                return False
        return True

    return False


def is__valid_by_elements_max_length(elements, lengths):
    if len(elements) > 0:
        for i in len(elements):
            ele = elements[i]
            l = lengths[i]
            if ele:
                if ele['maxlength']:
                    if l > ele['maxlength']:
                        return False
            else:
                return False
        return True

    return False


def is__valid_by_max_length(element, length):
    if element:
        ele = element['element']
        if ele:
            if element['maxlength']:
                if element['maxlength'] <= len(ele.get_attribute('value')):
                    return True
            if len(ele.get_attribute('value')) > length:
                return False
            return True
    return False


def is__valid_by_input_max_length(element, length):
    if element.get_attribute('value') > length:
        return False
    return True


def find__inputs(driver):
    return driver.find_elements_by_tag_name("input")

def find__inputs__textarea(driver):
    return driver.find_elements_by_tag_name("textarea")


def find__by_elements(driver=None, tag_name=None):
    return driver.find_elements_by_tag_name(tag_name)


def find__inputs_by_xpath(driver):
    return driver.find_elements(By.XPATH, '//input')


def get__elements(inputs=[]):
    if len(inputs) > 0:
        elements = []
        for i in inputs:
            input = {
                "is_required": is__required(input=get_attr(input=i, attr='required')),
                "id": get_attr(input=i, attr='id'),
                "maxlength": get_attr(input=i, attr='max-length'),
                "name": get_attr(input=i, attr='name'),
                "element": i,
            }
            elements.append(input)
        return elements
    return []

