import os
import sys
import time
import webbrowser
from _ast import Assert
from lib2to3.pgen2 import driver
from telnetlib import EC
import random

import unittest
from selenium.webdriver.common.by import By
from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver
from robot.run import RobotFramework
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import signal
from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as ec
i=0
moviename = 'null'
class PythonKeywords:

    def __init__(self):
        pass

    @staticmethod
    def current():
        seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
        current_driver = seleniumlib.driver
        return current_driver

    @staticmethod
    def maximize_the_browser():
        driver = PythonKeywords.current()
        driver.maximize_window()


    @staticmethod
    def please_close_browser():
        os.system("taskkill /im chrome.exe /f")

    @staticmethod
    def wait_element_is_visible(elementvariable):
        driver = PythonKeywords.current()

        wait = WebDriverWait(driver, 15)
        wait.until(ec.visibility_of_element_located((By.XPATH, elementvariable)))
        #WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, elementvariable)))



    @staticmethod
    def click_this_element(elementvariable):
        driver = PythonKeywords.current()
        driver.find_element_by_xpath(elementvariable).click()

    @staticmethod
    def get_text_of_element(elementvariable):
        driver = PythonKeywords.current()
        text = driver.find_element_by_xpath(elementvariable).text
        return text

    @staticmethod
    def elements_should_be_equal(x,y):
        if ((str(x).strip()) == (str(y).strip())):
            print(str(x) + " equals " + str(y))

        else:
            raise ValueError(str(x)+' doesn t equal'+ str(y))

    @staticmethod
    def elements_should_not_be_equal(x, y):
        if ((str(x).strip()) != (str(y).strip())):
            print(str(x) + " doesnt equals " + str(y))

        else:
            raise ValueError(str(x) + ' equal' + str(y))


    @staticmethod
    def random(upperlimit):
        rnd_value = random.randint(0, upperlimit)
        return rnd_value

    @staticmethod
    def click_on_any_your_rating():
        i = PythonKeywords.random(249)
        print(i)
        driver = PythonKeywords.current()

        wait = WebDriverWait(driver, 10)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#main > div > span > div > div > div.lister > table > tbody > tr > td:nth-child(4) > div > div.inline > div.unseen')))

        find = driver.find_elements_by_css_selector('#main > div > span > div > div > div.lister > table > tbody > tr > td:nth-child(4) > div > div.inline > div.unseen')
        print(len(find))



        driver.execute_script("arguments[0].scrollIntoView();", find[i])

        find[i].click()

    @staticmethod
    def type_something(elementvariable,text):
        driver = PythonKeywords.current()
        inputElement = driver.find_element_by_xpath(elementvariable)
        inputElement.send_keys(text)

    @staticmethod
    def hover_over_any_add_to_wathclist(elementvariable):
        global i
        i = PythonKeywords.random(249)

        print(i)
        driver = PythonKeywords.current()

        wait = WebDriverWait(driver, 10)
        wait.until(ec.visibility_of_element_located((By.XPATH,elementvariable)))

        find = driver.find_elements_by_xpath(elementvariable)

        driver.execute_script("arguments[0].scrollIntoView();", find[i])

        hover = ActionChains(driver).move_to_element(find[i])
        hover.perform()




        #learn the movie's name
        find3 = driver.find_elements_by_css_selector('#main > div > span > div > div > div.lister > table > tbody > tr > td.titleColumn > a')
        moviesname= find3[i].text
        print(moviesname)
        return i


    @staticmethod
    def check_tooltip_before_adding():
        driver = PythonKeywords.current()
        find2 = driver.find_elements_by_css_selector("#main > div > span > div > div > div.lister > table > tbody > tr > td.watchlistColumn > div > div")
        print(i)


        PythonKeywords.elements_should_be_equal(find2[i].get_attribute("title"),'Click to add to watchlist')
        find3 = driver.find_elements_by_css_selector(
            '#main > div > span > div > div > div.lister > table > tbody > tr > td.titleColumn > a')
        global moviename
        moviename = find3[i].text
        print(moviename)
        return moviename

    @staticmethod
    def click_to_add_to_watchlist(elementvariable):
        driver = PythonKeywords.current()
        find = driver.find_elements_by_xpath(elementvariable)
        find[i].click()

    @staticmethod
    def check_tooltip_after_adding():
        driver = PythonKeywords.current()
        find2 = driver.find_elements_by_css_selector(
            "#main > div > span > div > div > div.lister > table > tbody > tr > td.watchlistColumn > div > div")
        print(i)
        print(moviename)
        time.sleep(3)
        PythonKeywords.elements_should_be_equal(find2[i].get_attribute("title"), 'Click to remove from watchlist')

    @staticmethod
    def hover_over_element(elementvariable):
        driver = PythonKeywords.current()
        find = driver.find_element_by_xpath(elementvariable)
        hover = ActionChains(driver).move_to_element(find)
        hover.perform()
        time.sleep(5)



    @staticmethod
    def find_my_movie_in_watchlist(elementvariable):
        driver = PythonKeywords.current()
        wait = WebDriverWait(driver, 15)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, elementvariable)))
        movienamesinwatchlist = driver.find_elements_by_css_selector(elementvariable)
        for k in range(0, len(movienamesinwatchlist)):
            if (movienamesinwatchlist[k].text ==  moviename):
                print(moviename+ ' movie was added to your watchlist')
            else:
                print(moviename + ' can not be found in your watchlist')




