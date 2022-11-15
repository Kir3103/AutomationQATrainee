import BasePage from './BasePage.js'
import Button from '../elements/Button.js'
import Label from '../elements/Label.js'


const locatorHomePage = new Label('//*[@id="app"]//button[@type="button"]', 'Home Page')
const btnHere = new Button('//*[@id="app"]//a[contains(text(),"HERE")]', 'Button "HERE"')

class HomePage extends BasePage {
    
    constructor () {
        super(locatorHomePage, 'Home Page')
    }

    async clickHereButton () {
        return (await btnHere.clickRegular())
    }
}

export default new HomePage()