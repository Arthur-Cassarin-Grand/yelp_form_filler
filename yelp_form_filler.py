#! /usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

class YelpFormFiller(object):
    def __init__(self, csv_file_source="data.csv"):
        self.csv_file_source = csv_file_source

    def fill_yelp(self):

        biz_name_content = ""
        biz_address_content = ""
        biz_city_content = ""
        biz_zip_code_content = ""
        biz_phone_content = ""
        biz_website_content = ""
        biz_mail_content = ""

        driver = webdriver.Firefox()

        file = open(self.csv_file_source, "r", encoding="utf_8", newline='\n')
        csv_file = csv.reader(file, delimiter=';')
        for row in csv_file:
            biz_website_content = row[0]
            biz_name_content = row[1]
            biz_address_content = row[2]
            biz_zip_code_content = row[3]
            biz_city_content = row[4]
            biz_phone_content = row[5]

            driver.get("https://biz.yelp.fr/signup_business/new")

            # Nom
            biz_name = driver.find_element_by_id("biz_name")
            biz_name.send_keys(biz_name_content)

            # Adress
            biz_address = driver.find_element_by_id("biz_address1")
            biz_address.send_keys(biz_address_content)

            # City
            biz_city = driver.find_element_by_id("biz_city")
            biz_city.send_keys(biz_city_content)

            # Zip Code
            biz_zip_code = driver.find_element_by_id("biz_zip")
            biz_zip_code.send_keys(biz_zip_code_content)

            # Phone
            biz_phone = driver.find_element_by_id("biz_phone")
            biz_phone.send_keys(biz_phone_content)

            # Website
            biz_website = driver.find_element_by_id("biz_website")
            biz_website.send_keys(biz_website_content)

            # Category
            biz_category = driver.find_element_by_class_name("js-category-picker-input")
            biz_category.send_keys("Location de vacances")
            time.sleep(1)
            biz_category.send_keys(Keys.ARROW_DOWN)
            biz_category.send_keys(Keys.ENTER)

            # Email
            biz_mail = driver.find_element_by_name("email")
            biz_mail.send_keys("somebody@me.fr")

            # Input
            biz_input = driver.find_element_by_class_name("new-business-submit")
            biz_input.click()

            time.sleep(15)
        file.close()

        driver.close()
        print("Exécution terminée.")
