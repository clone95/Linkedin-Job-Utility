from selenium import webdriver
import time

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

    time.sleep(6)
    print("launch")
    keyword = browser.find_element_by_id('jobs-search-box-keyword-id-ember45')
    place = browser.find_element_by_id('jobs-search-box-location-id-ember45')

    keyword.send_keys("big data")
    place.send_keys("Bologna, Italia")
    search = browser.find_element_by_class_name('jobs-search-box')
    search.click()
    if search:
            print("found")

main()
