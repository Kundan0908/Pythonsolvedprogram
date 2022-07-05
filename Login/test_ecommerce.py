import pytest
from Utilities.Baseclass import BaseClass
from PageObjects.login import Login
from PageObjects.FlightCheck import Flight
from PageObjects.SelectFlight import selectflight
from time import sleep


# @pytest.mark.usefixtures("Chromebrowser")
class TestLogin(BaseClass):

    def test_login(self):

        self.driver.implicitly_wait(10)
        self.driver.get("https://www.agoda.com/")
        self.driver.maximize_window()

        homepage = Login(self.driver)
        homepage.header_tab()

        newAccount = False

        if newAccount:
            homepage.CreateAccount()
        else:
            homepage.signin()
        # self.driver.find_element_by_xpath("//span[text()='Flights']").click()
        flight = Flight(self.driver)

        flight.checkflight()

        findflight = selectflight(self.driver)
        findflight.pick_flight()
