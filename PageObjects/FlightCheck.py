
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from time import sleep
class Flight:

    flightTab = (By.CSS_SELECTOR, "span[data-selenium='header-flights-links-text']")
    fromcity = (By.CSS_SELECTOR, "input[placeholder='Flying from']")
    tocity  = (By.CSS_SELECTOR, "input[placeholder='Flying to']")

    def __init__(self, driver):
        self.driver = driver

    def checkflight(self):
        windowPage = []
        self.driver.find_element(*Flight.flightTab).click()
        windows = self.driver.window_handles
        for windoe in windows:
            self.driver.switch_to.window(windoe)
            windowPage.append(self.driver.title)
            # assert
        print(windowPage)
        flyfrom = self.driver.find_element(*Flight.fromcity)
        flyfrom.send_keys("Kem")
        actions = AC(self.driver)
        actions.move_to_element(self.driver.find_element_by_css_selector("div[class ='Popup__content']")).perform()
        actions.click(self.driver.find_element(By.CSS_SELECTOR, "li[data-text='Kempegowda International Airport']")).perform()
        flyto = self.driver.find_element(*Flight.tocity)
        flyto.send_keys("ind")
        actions.click(self.driver.find_element(By.CSS_SELECTOR, "li[data-text='Indira Gandhi International Airport']")).perform()
        count = 0
        val = []
        while count < 5:
            try:
                val = self.driver.find_element(By.XPATH, "//div[text()='November 2022']")
                if val:
                    self.driver.find_element(By.XPATH, "//div[text()='November 2022']")
                    break
            except Exception as e:
                pass
            self.driver.find_element(By.XPATH, "//span[@aria-label='Next Month']").click()
            # sleep(5)
            count += 1

        self.driver.find_element(By.XPATH,"//div[text()='November 2022']/parent::div/parent::div//span[text()='9']").click()
        Passenger = self.driver.find_elements(By.XPATH, "//div[@class='SearchBoxTextDescription__title']")
        for ticketype in Passenger:
            type = ticketype.text
            if "Economy" in type:
                # self.driver.find_element(By.XPATH, "//div[@class='ChipSetContainer']//div[text()='Economy']").click()
                ticketype.click()
        self.driver.find_element(By.XPATH, "//span[text() = 'SEARCH FLIGHTS']").click()
