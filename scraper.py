from selenium import webdriver
import time

# disabling notifications browser-level popUP

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(chrome_options=chrome_options)


def main(mail, password, word, n):

    browser.execute_script("window.open('about:blank', 'tab{}');".format(n))
    browser.switch_to.window("tab{}".format(n))
    time.sleep(1)
    browser.get('https://www.linkedin.com/jobs/')
    # finding login input areas

    if n == 0:
        login = browser.find_element_by_class_name('nav-item__link')
        login.click()
        mail_element = browser.find_element_by_name('session_key')
        pwd_element = browser.find_element_by_name('session_password')
        # filling login form

        mail_element.send_keys(str(mail))
        pwd_element.send_keys(str(password))

    # login

        #submit_element = browser.find_element_by_name('signin')
        #submit_element.click()

    time.sleep(2)

    keyword = browser.find_element_by_id('jobs-search-box-keyword-id-ember45')
    place = browser.find_element_by_id('jobs-search-box-location-id-ember45')

    keyword.send_keys(word)
    place.send_keys("Bologna, Italia")
    search = browser.find_element_by_class_name('button-secondary-large-inverse')
    search.click()

    time.sleep(2)


    # type_of_job.click()
    # thesis = browser.find_element_by_id('f_E-1')
    # thesis.click()


