
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class CreateSalesOrderPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _icao_field = "#quick-fuel-quote .fuel-quote-form__airport-code-input"  #"mat-input-0"
    _airport_name = "//div[@class='cdk-overlay-pane']//small[contains(text(),'{0}')]"   #"//div[@class='cdk-overlay-pane']//span[contains(text(),'{0}')]"
    _select_location = "ticker-item-1" #"ticker-div0"
    _select_FBO_setup = "#fbo-1-setup-button" # for FBO2 use #fbo-2-setup-button and so forth.
    _select_FBO_details = "#fbo-1-details-button"  # for FBO2 use #fbo-2-details-button and so forth.

    _registry_list = "#fuel-quote-setup-registry-select" #"//div[@class='mat-select-value']"
    _select_tail = "//div[@class='cdk-overlay-pane']//span[contains(text(),'{0}')]" #"//span[@class='mat-option-text'][contains(text(),'{0}')]" #"//span[contains(text(),'{0}')]"
    _next_destination = "fuel-quote-setup-nextdestination" #"mat-input-2"
    _gallons = "fuel-quote-setup-gallons" #"mat-input-4"
    _flight_num = "fuel-quote-setup-flightnumber" #"mat-input-5"
    _aircraft_ground = "#fuel-quote-setup-aircraftonground-input"
    _arrival_calendar = "fuel-quote-setup-arrivaldate" #"mat-input-6"
    _arrival_date = ".mat-calendar-table [aria-label='January 16, 2019'] div" #"[id='cdk-overlay-3'] [aria-label='December 5, 2018'] div"
    _arrival_hour = "fuel-quote-setup-arrivalhour" #"mat-input-7"
    _arrival_minutes = "fuel-quote-setup-arrivalminute" #"mat-input-8"
    _departure_calendar = "fuel-quote-setup-departuredate" #"mat-input-9"
    _departure_date = ".mat-calendar-table [aria-label='January 17, 2019'] div" #"[id='cdk-overlay-4'] [aria-label='December 12, 2018'] div"
    _departure_hour = "fuel-quote-setup-departurehour" #"mat-input-10"
    _departure_minutes =  "fuel-quote-setup-departureminute" #"mat-input-11"
    _additional_notes = "fuel-quote-setup-freehandnotes"  #ID
    _email = "fuel-quote-setup-email" #ID
    _fax = "fuel-quote-setup-fax" #Fax
    _request_fuel = "//span[contains(text(),'Request')]"
    _close_order = "//span[contains(text(),'Close')]"
    _quote_number = "//span[@class='quote-id']"
    _so_number = "//a[@class='portal__link ng-star-inserted']"

    ############################
    ### Element Interactions ###
    ############################

    #Houston William P Hobby
    def enterICAO(self, icao,airportName):
        icaoElement = self.waitForElement(self._icao_field,'css')
        self.sendKeys(icao, element=icaoElement)
        self.elementClick(locator=self._airport_name.format(airportName),locatorType="xpath")

    def selectLocation(self):
        locationElement = self.waitForElement(locator=self._select_location,locatorType='id',timeout=60,pollFrequency=1)
        self.elementClick(element=locationElement)

    #selecting FBO Setup button
    def selectFBOSetup(self):
        self.webScroll()
        self.elementClick(self._select_FBO_setup,'css')

    # selecting FBO Details button
    def selectFBODetails(self):
        self.webScroll()
        self.elementClick(self._select_FBO_details, 'css')

    #5H-ZBZ
    def selectTail(self,tailNumber):
        registryElement = self.waitForElement(locator=self._registry_list,locatorType='css',timeout=10)
        self.elementClick(element=registryElement)
        self.elementClick(self._select_tail.format(tailNumber),'xpath')

    def enterNextDestination(self,nextDestination):
        self.sendKeys(nextDestination,self._next_destination)

    def enterGallons(self,quantity):
        self.sendKeys(quantity,self._gallons)

    def enterFlightNumber(self,flightNumber):
        self.sendKeys(flightNumber,self._flight_num)

    def selectArrivalDate(self,arrivalDate,arrivalHour,arrivalMin):
        self.elementClick(self._arrival_calendar)
        time.sleep(1)
        self.elementClick(self._arrival_date, 'css')
        self.sendKeys(arrivalHour,self._arrival_hour)
        self.sendKeys(arrivalMin,self._arrival_minutes)

    def selectDepartureDate(self,departureDate,departureHour,departureMin):
        self.elementClick(self._departure_calendar)
        # departureDateElement = self.waitForElement(self._departure_date.format(departureDate),'css_selector')
        # self.elementClick(element=departureDateElement)
        time.sleep(1)
        self.elementClick(self._departure_date,'css')
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

    def clickCloseRequest(self):
        closeElement = self.waitForElement(locator=self._close_order,locatorType='xpath',timeout=10)
        self.elementClick(element=closeElement)


    def enterTripInformation(self,tailNumber,nextDestination,quantity,flightNumber,
                             arrivalDate,arrivalHour,arrivalMin,departureDate,departureHour,departureMin):
        print('############################## Begin Fueling Process ##############################')

        self.selectTail(tailNumber)
        self.enterNextDestination(nextDestination)
        self.enterGallons(quantity)
        self.enterFlightNumber(flightNumber)
        self.selectArrivalDate(arrivalDate,arrivalHour,arrivalMin)
        self.selectDepartureDate(departureDate,departureHour,departureMin)


    # def verifyEnrollFailed(self):
    #     result = self.isEnabled(locator=self._submit_enroll2, locatorType="xpath",
    #                             info="Enroll Button")
    #     return not result
