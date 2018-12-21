from selenium import webdriver
import time
import os
import SimpleCV as cv
from selenium.webdriver.common.by import By

# disabling notifications browser-level popUP

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(chrome_options=chrome_options)


def main():


    your_email = 'giac290595@gmail.com'
    your_pwd = 'Jellyash95'

    time.sleep(1)
    browser.get('https://www.linkedin.com/jobs/')

    # finding login input areas
    login = browser.find_element_by_class_name('nav-item__link')
    login.click()
    mail_element = browser.find_element_by_name('session_key')
    pwd_element = browser.find_element_by_name('session_password')
    # filling login form

    mail_element.send_keys(str(your_email))
    pwd_element.send_keys(str(your_pwd))

    # login

    submit_element = browser.find_element_by_name('signin')
    submit_element.click()

    time.sleep(2)

    keyword = browser.find_element_by_id('jobs-search-box-keyword-id-ember45')
    place = browser.find_element_by_id('jobs-search-box-location-id-ember45')

    keyword.send_keys("big data")
    place.send_keys("Bologna, Italia")
    search = browser.find_element_by_class_name('button-secondary-large-inverse')
    search.click()

    time.sleep(2)
    type_of_job = browser.find_element_by_class_name('neptune-grid')
    lista = list(type_of_job.find_elements_by_tag_name("ul"))
    filter_list = lista[0]
    for n, el in enumerate(lista):
        print(lista[n].text)
        print(lista[n].tag_name)
        print(lista[n].id)
        print("\n\n")
    #xperience = filter_list.find_elements_by_tag_name('li')[3]
    a = list(filter_list.find_elements_by_tag_name('li'))

    for n, el in enumerate(a):
        print("______")
        print(a[n].tag_name)

    # type_of_job.click()
    # thesis = browser.find_element_by_id('f_E-1')
    # thesis.click()


main()
