import BasePage from './BasePage.js'
import Label from '../elements/Label.js'

const locatorPersonalPage = new Label('//*[@id="app"]//div[@class="personal-details"]', 'Personal Page')

class PersonalPage extends BasePage {
    
    constructor () {
        super(locatorPersonalPage, 'Personal Page')
    }

}
export default new PersonalPage()