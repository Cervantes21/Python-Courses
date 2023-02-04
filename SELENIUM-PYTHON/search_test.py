import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
# By nos permite el uso de 2 métodos privados find_elements(selector, 'value') y find_element(By.ID, "search")
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class HomePageTests(unittest.TestCase):

    def setUp(self):
    # -----------------------variables---------------------------------- #
      # --- Brave configure --- # 
        # brave_path = '/usr/bin/brave-browser'
        # option = webdriver.ChromeOptions()
        # option.binary_location = brave_path
      # --- Chrome-Driver --- # 
        chromedriver = '/usr/bin/chromedriver'
        s = Service(chromedriver)  
    # ------------------------------------------------------------------ #
        # driver = self.driver = webdriver.Chrome(service=s, options=option) # Resolve for Brave
        driver = self.driver = webdriver.Chrome(service=s)
    # ---------------Driver Configure-------------- #
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)
    # --------------------------------------------- #

    # --- Testers --- #
    def test_search_text_field(self):
        search_field = self.driver.find_element(By.ID,"search")
 # ---
    def test_search_text_field(self):
        search_field = self.driver.find_element(By.NAME, "q")
 # ---
    def test_search_text_field_class(self):
        search_field = self.driver.find_element(By.CLASS_NAME, "input-text")
 # ---
    def test_search_button_enabled(self):
        button = self.driver.find_element(By.CLASS_NAME, 'button')
 # ---
    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element(By.CLASS_NAME, 'promos')
        banners = banner_list.find_elements(By.TAG_NAME, 'img')
        self.assertEqual(3,len(banners))
 # ---
    def test_vip_promo(self):
        vip_promo = self.driver.find_element(
            By.XPATH,
            "//*[@id='top']/body/div/div[2]/div[2]/div/div/div[2]/div/ul/li[4]/a/img"
            )
 # ---
    def test_icon_cart(self):
        icon_cart = self.driver.find_element(By.CSS_SELECTOR,"div.header-minicart span.icon")
        
    # -------------------------- # 

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'find_elements', report_name = 'Search_test'))
