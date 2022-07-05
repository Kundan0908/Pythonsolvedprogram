
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Login:

    loginHeader = (By.XPATH, "//button[@class='ab-close-button']")
    createAccountTab = (By.XPATH, "//span[text()='Create account']")
    createaccount = (By.XPATH, "//p[text()='Create account']")
    headerMenu = (By.CSS_SELECTOR, "svg[class='SvgIconstyled__SvgIconStyled-sc-1i6f60b-0 coLXuD']")
    firstname = (By.NAME, "firstName")
    frame = (By.XPATH, "//iframe[@title='Universal login']")
    lastName = (By.ID, "lastName")
    email = (By.ID, "email")
    password = (By.ID, "password")
    confirmPassword = (By.ID, "confirmPassword")
    text = (By.XPATH, "//span[text()='Google']")

    signintab = (By.XPATH, "//span[text() = 'Sign in']")
    emailid = (By.ID, 'email')
    loginpassword = (By.ID, 'password')

    def __init__(self, driver):
        self.driver = driver

    def header_tab(self):

        count = 0
        while count < 5:
            try:
                element_found = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(Login.loginHeader))
                if element_found:
                    self.driver.find_element(*Login.loginHeader).click()
                    print(count)
                    break
            except Exception as e:
                pass
            count +=1


    def CreateAccount(self):

        # webelement_CreateAccount = self.driver.find_element(Login.createAccountTab)
        # if len(webelement_CreateAccount) > 0:
        #     webelement_CreateAccount.click()
        # else:
        self.driver.find_element(*Login.headerMenu).click()
        self.driver.find_elements(*Login.createaccount)[1].click()
        accountForm = WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(Login.firstname))

        if accountForm:
            frameset = self.driver.find_element(*Login.frame)
            self.driver.switch_to.frame(frameset)
            self.driver.find_element(*Login.firstname).send_keys("Kundan")
            self.driver.find_element(*Login.lastName).send_keys("Kumar")
            self.driver.find_element(*Login.email).send_keys("test@gmail.com")
            self.driver.find_element(*Login.password).send_keys("test@7654")
            self.driver.find_element(*Login.confirmPassword).send_keys("test@7654")
            self.driver.find_element(*Login.text).click()
            self.driver.find_element(*Login.firstname).send_keys("Kundan")
            self.driver.switch_to.default_content()

    def headerbar(self):
        return self.driver.find_element(Login.headerMenu)

    def signin(self):
        self.driver.find_element(*Login.headerMenu).click()
        # self.driver.find_elements(*Login.createaccount)[1].click()
        self.driver.find_elements(*Login.signintab)[1].click()
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(Login.emailid))
        frameset = self.driver.find_element(*Login.frame)
        self.driver.switch_to.frame(frameset)
        self.driver.find_element(*Login.emailid).send_keys("test@gmail.com")
        self.driver.find_element(*Login.loginpassword).send_keys("AutomationTesting")
        self.driver.find_element(*Login.signintab).click()
        self.driver.switch_to.default_content()
