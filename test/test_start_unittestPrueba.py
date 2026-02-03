#convertir a unittest
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class FindbyIdName(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://NelsonGabriel2003.github.io/PaginasPruebas/")

    def testId(self):
        # Busca elemento por ID "noImportante"
        elemento = self.driver.find_element(By.ID, "noImportante")
        if elemento is not None:
            print("El elemento by ID fue encontrado")

    def testName(self):
        # Busca elemento por NAME "ultimo"
        elemento2 = self.driver.find_element(By.NAME, "ultimo")
        if elemento2 is not None:
            print("El elemento by NAME fue encontrado")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()