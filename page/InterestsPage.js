import BasePage from './BasePage.js'
import Button from '../elements/Button.js'
import Label from '../elements/Label.js'
import Upload from '../elements/Upload.js'
import testDataFile from '../utils/testData.js'


const locatorCheckboxInterests = new Label('//*[@id="app"]//div[contains(@class, "form")]', 'Checkbox Interests')
const locatorUnselectAll = new Button('//*[@id="app"]//label[contains(@for,"unselect")]', 'Unselect ALL')
const locatorPoloInterests = new Button('//*[@id="app"]//label[contains(@for,"polo")]', 'Polo Interests')
const locatorTiresInterests = new Button('//*[@id="app"]//label[contains(@for,"tires")]', 'Tires Interests')
const locatorCottonInterests = new Button('//*[@id="app"]//label[contains(@for,"cotton")]', 'Cotton Interests')
const locatorUpload = new Upload('//*[@id="app"]//a[contains(@class,"upload")]', 'Upload form')
const locatorNextBtn = new Button('//*[@id="app"]//button[contains(text(),"Next")]', 'Next button')

class InterestsPage extends BasePage {
    
    constructor () {
        super(locatorCheckboxInterests, 'Checkbox Interests')
    }

    async unselectAll () {
        return (await locatorUnselectAll.clickRegular())
    }

    async selectInterests () {
        locatorPoloInterests.clickRegular()
        locatorTiresInterests.clickRegular()
        return (await locatorCottonInterests.clickRegular())
    }

    async uploadImage () {
        // it doesn't work
        const path = require('path')
        const filePath = path.join(__dirname, '..', 'resources', testDataFile.interestsPageData)
        const remoteFilePath = browser.uploadFile(filePath)
        return (await locatorUpload.uploadFile(remoteFilePath))
    }

    async clickNextBtn () {
        return (await locatorNextBtn.clickRegular())
    }

}

export default new InterestsPage()