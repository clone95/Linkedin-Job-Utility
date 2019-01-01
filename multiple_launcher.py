from selenium import webdriver
import time
import scraper

with open("linkedin_data.txt") as file: # Use file to refer to the file object

   data = file.readlines()
   mail = data[0]
   pwd = data[1]
   keywords_wanted = data[2:]


def main(email, password, keys):

    for n, keyword in enumerate(keys):
        scraper.main(email, password, keyword, n)


if __name__ == '__main__':
    main(mail, pwd, keywords_wanted)