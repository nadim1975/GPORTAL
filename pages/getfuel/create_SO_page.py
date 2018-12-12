import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class CreateSalesOrderPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _icao_field = "mat-input-0"
    _airport_name = "//div[@id='mat-autocomplete-0']//small[contains(text(),'{0}')]"
    _select_location = "ticker-div0"
    _select_location2 =_"//dt[@class='dt-font_title']"
    _select_FBO = "//article[1]//button[@class='mat-button mat-flat-button mat-primary']//span[contains(text(),'Setup')]"
    _registry_list = "//div[@class='mat-select-value']"
    _select_tail = "//span[contains(text(),'{0}')]"
    _next_destination = "mat-input-2"
    _gallons = "mat-input-4"
    _flight_num = "mat-input-5"
    _arrival_calendar = "mat-input-6"
    _arrival_date = "//div[contains(text(),'{0}')]"
    _arrival_hour = "mat-input-7"
    _arrival_minutes = "mat-input-8"
    _departure_calendar ="mat-input-9"
    _departure_date = "//div[contains(text(),'{0}')]"
    _departure_hour = "mat-input-10"
    _departure_minutes = "mat-input-11"
    _request_fuel = "//span[contains(text(),'Request')]"
    _close_order = "//span[contains(text(),'Close')]"
    _quote_number = "//span[@class='quote-id']"
    _so_number = "//a[@class='portal__link ng-star-inserted']"

    ############################
    ### Element Interactions ###
    ############################

    #Houston William P Hobby
    def enterICAO(self, icao,airportName):
        icaoElement = self.waitForElement(self._icao_field)
        self.sendKeys(icao, element=icaoElement)
        self.elementClick(locator=self._airport_name.format(airportName),locatorType="xpath")

    def selectLocation(self):
        locationElement = self.waitForElement(locator=self._select_location,locatorType='id',timeout=60,pollFrequency=1)
        self.elementClick(element=locationElement)

    #selecting first FBO
    def selectFBO(self):
        self.elementClick(self._select_FBO,'xpath')

    #5H-ZBZ
    def selectTail(self,tailNumber):
        registryElement = self.waitForElement(locator=self._registry_list,locatorType='xpath',timeout=10)
        self.elementClick(element=registryElement)
        self.elementClick(self._select_tail.format(tailNumber),'xpath')

    def enterNextDestination(self,nextDestination):
        self.sendKeys(nextDestination,self._next_destination)

    def enterGallons(self,quantity):
        self.sendKeys(quantity,self._gallons)

    def enterFlightNumber(self,flightNumber):
        self.sendKeys(flightNumber,self._flight_num)

    def selectArrivalDate(self,arrivalDay,arrivalHour,arrivalMin):
        self.elementClick(self._arrival_calendar)
        self.elementClick(self._arrival_date.format(arrivalDay),'xpath')
        self.sendKeys(arrivalHour,self._arrival_hour)
        self.sendKeys(arrivalMin,self._arrival_minutes)

    def selectDepartureDate(self,departureDay,departureHour,departureMin):
        self.elementClick(self._departure_calendar)
        self.elementClick(self._departure_date.format(departureDay), 'xpath')
        self.sendKeys(departureHour, self._departure_hour)
        self.sendKeys(departureMin, self._departure_minutes)

    def clickRequestFuel(self):
        self.elementClick(self._request_fuel,'xpath')

    def getQuoteNumber(self):
        quoteElement = self.waitForElement(locator=self._quote_number, locatorType='xpath', timeout=40)
        return self.getElementAttributeValue('text',element=quoteElement)

    def getSoNumber(self):
        soElement = self.waitForElement(locator=self._so_number, locatorType='xpath', timeout=40)
        return self.getElementAttributeValue('text', element=soElement)

    def verifySOcreated(self):
        soElement = self.waitForElement(locator=self._so_number, locatorType='xpath', timeout=40)
        return self.isElementDisplayed(element=soElement)


    def enterTripInformation(self,icao,airportName,tailNumber,nextDestination,quantity,flightNumber,
                             arrivalDay,arrivalHour,arrivalMin,departureDay,departureHour,departureMin):
        self.enterICAO(icao,airportName)
        self.selectLocation()
        self.selectFBO()
        self.selectTail(tailNumber)
        self.enterNextDestination(nextDestination)
        self.enterGallons(quantity)
        self.enterFlightNumber(flightNumber)
        self.selectArrivalDate(arrivalDay,arrivalHour,arrivalMin)
        self.selectDepartureDate(departureDay,departureHour,departureMin)


    # def verifyEnrollFailed(self):
    #     result = self.isEnabled(locator=self._submit_enroll2, locatorType="xpath",
    #                             info="Enroll Button")
    #     return not result