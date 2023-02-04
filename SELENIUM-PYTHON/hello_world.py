import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class HelloWorld(unittest.TestCase):

    def setUp(self):
    # -----------------------variables---------------------------------- #
        chromedriver = '/usr/bin/chromedriver'
        brave_path = "/usr/bin/brave-browser-stable"
        driver = self.driver = webdriver.Chrome(executable_path = chromedriver)
        option = webdriver.ChromeOptions()
    # ------------------------------------------------------------------ #
    
        option.binary_location = brave_path 
        driver.implicitly_wait(10)

    # --- Testers --- #
     
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_visit_kaggle(self):
        driver = self.driver
        driver.get('https://www.kaggle.com')

    # -------------------------- # 

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))
