
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

class selectflight:

    def __init__(self, driver):
        self.driver = driver

    def pick_flight(self):
        price = []

        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(5)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        # no_of_flights = self.driver.find_elements(By.XPATH, "//div[@class ='Box-sc-kv6pi1-0 iVaeyN']")
        no_of_flights = WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "//div[@class ='Box-sc-kv6pi1-0 iVaeyN']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[4]")))
        select_filghts = self.driver.find_elements(By.XPATH, "//div[@data-component='flight-card-price-container']/following-sibling::div/div[@class='Box-sc-kv6pi1-0 hQFBdk']/button")

        for flight in no_of_flights:
            price.append(flight.text)
        print("The cheapest ticket price is ", price[0], "and the expensive ticket price is ", price[-1])

        flight_to_book = "Cheap"
        if flight_to_book == "Cheap":
            for select_flight in select_filghts:
                select_flight.click()
                self.driver.find_element(By.XPATH, "//span[text() ='No Thanks']").click()
                break
        else:
            for select_flight in reversed(select_filghts):
                select_flight.click()
                self.driver.find_element(By.XPATH, "//span[text() ='No Thanks']").click()
                break

