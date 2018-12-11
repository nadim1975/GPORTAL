import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _search_box = "search-courses"
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _search_button = 'search-course-button'
    _all_courses = "course-listing-title"
    _enroll_button = "enroll-button-top"
    _cc_num = 'cardnumber'
    _cc_exp = 'exp-date'
    _cc_cvv = 'cvc'
    _card_country = "//select[@id='country_code_credit_card-cc']//option[text()='{0}']"
    _card_postalcode = 'postal'
    _agreement_checkbox = 'agreed_to_terms_checkbox'
    _submit_enroll = 'confirm-purchase'
    _card_decline = "//div[contains(text(),'The card was declined')]"
    _enroll_error_message = "//div[@id='new_card']//div[contains(text(),'The card number is not a valid credit card number.')]"
    _submit_enroll2 = "//button[@id='confirm-purchase']/parent::div"

    ############################
    ### Element Interactions ###
    ############################

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box)
        self.elementClick(self._search_button)

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button)

    def enterCardNum(self, num):
        self.switchToFrame(name="__privateStripeFrame4")
        self.sendKeys(num,self._cc_num,'name')
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        self.switchToFrame(name="__privateStripeFrame5")
        self.sendKeys(exp, locator=self._cc_exp,locatorType='name')
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        self.switchToFrame(name="__privateStripeFrame6")
        self.sendKeys(cvv, locator=self._cc_cvv,locatorType='name')
        self.switchToDefaultContent()

    def selectCountry(self,country):
        self.elementClick(self._card_country.format(country),'xpath')

    def enterPostalCode(self,zipcode):
        self.switchToFrame(name="__privateStripeFrame7")
        self.sendKeys(zipcode,self._card_postalcode,'name')
        self.switchToDefaultContent()

    def clickAgreeToTermsCheckbox(self):
        self.elementClick(locator=self._agreement_checkbox)


    def clickEnrollSubmitButton(self):
        self.elementClick(self._submit_enroll)
        #self.elementClick(self._submit_enroll2,'xpath')

    def enterCreditCardInformation(self, num, exp, cvv,country,zipcode):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.selectCountry(country)
        self.enterPostalCode(zipcode)

    def enrollCourse(self, num="", exp="", cvv="",country="United States",zipcode="33025"):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv,country,zipcode)
        self.clickAgreeToTermsCheckbox()
        #self.clickEnrollSubmitButton()

    def verifyCardDecline(self):
        self.isElementPresent(self._card_decline,'xpath')

    def verifyEnrollFailed(self):
        result = self.isEnabled(locator=self._submit_enroll2, locatorType="xpath",
                                info="Enroll Button")
        return not result
