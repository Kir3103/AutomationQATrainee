import BasePage from './BasePage.js'
import generatePassword from '../utils/generatePassword.js'
import Label from '../elements/Label.js'
import Dropdown from '../elements/Dropdown.js'
import TextField from '../elements/TextField.js'
import Button from '../elements/Button.js'
import testDataFile from '../utils/testData.js'


const locatorRegistrationPage = new Label('//*[@id="app"]//div[@class="login-form"]', 'Registration Page')
const locatorfillPass = new TextField('//*[@id="app"]//input[contains(@placeholder,"Password")]', 'Fill password')
const locatorfillEmail = new TextField('//*[@id="app"]//input[contains(@placeholder,"email")]', 'Fill email')
const locatorfillDomain = new TextField('//*[@id="app"]//input[contains(@placeholder,"Domain")]', 'Fill domain')
const locatorSelectDropdown = new Dropdown('//*[@id="app"]//div[contains(@class,"list")]', 'Select Dropdown')
const locatorDropdownCom = new Dropdown('//*[@id="app"]//div[contains(text(),".com")]', 'Select .com')
const locatorTermsClick = new Button('//*[@id="app"]//span[contains(@class,"icon-check")]', '"Terms" button')
const locatorNextClick = new Button('//*[@id="app"]//a[contains(@class,"secondary")]', '"Next" button')
const locatorHideForm = new Button('//*[@id="app"]//button[contains(@class,"send")]', 'Hide form')
const locatorIsHideForm = new Label('//*[@id="app"]//div[contains(@class,"is-hidden")]', 'Is hide form')
const locatorAcceptCookie = new Button('//*[@id="app"]//button[contains(@class,"transparent")]', 'Accept cookie')
const locatorIsAcceptCookie = new Label('//*[@id="app"]//div[@class="cookies"]', 'Is accept cookie')
const locatorTimer = new Label('//*[@id="app"]//div[contains(@class,"timer")]', 'Check timer')

class RegistrationPage extends BasePage {
    
    constructor () {
        super(locatorRegistrationPage, 'Registration Page')
    }
    async fillPass () {
        return (await locatorfillPass.sendKeys(generatePassword(testDataFile.registrationPageData.quantForPass)))
    }
    async fillEmail () {
        return (await locatorfillEmail.sendKeys(testDataFile.registrationPageData.email))
    }
    async fillDomain () {
        return (await locatorfillDomain.sendKeys(testDataFile.registrationPageData.domain))
    }
    async selectDropdown () {
        locatorSelectDropdown.jsClick()
        return (await locatorDropdownCom.jsClick())
    }
    async termsClick () {
        return (await locatorTermsClick.clickRegular())
    }
    async nextClick () {
        return (await locatorNextClick.clickRegular())
    }
    async hideForm () {
        locatorHideForm.waitForElement()
        return (await locatorHideForm.clickRegular())
    }
    async isHideForm () {
        return (await locatorIsHideForm.waitForElement())
    }
    async acceptCookie () {
        locatorAcceptCookie.waitForElement()
        return (await locatorAcceptCookie.clickRegular())
    }
    async isAcceptCookie () {
        return (await locatorIsAcceptCookie.findElement())
    }
    async getTextTimer () {
        const textTimer = await locatorTimer.getTextFromElem()
        if ( textTimer === testDataFile.registrationPageData.timer ) {
            return true
        } return false 
    }

}

export default new RegistrationPage()