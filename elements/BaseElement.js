import scriptDataFile from '../utils/scriptData.js'
import Logger from '../utils/logUtils.js'

export default class BaseElement {
    
    constructor(locator, name) {
        this.locator = locator
        this.name = name
    }
    
    async findElement () {
        Logger.infoLog('Find element' + this.name)
        return (await $(this.locator).isDisplayed())
    }

    async findElements () {
        Logger.infoLog('Find elements' + this.name)
        return (await $$(this.locator).isDisplayed())
    }

    async waitForElement () {
        Logger.infoLog('Find element with wait' + this.name)
        return (await $(this.locator).waitForDisplayed())
    }

    async clickRegular () {
        Logger.infoLog('Click on' + this.name)
        return (await $(this.locator).click())
    }

    async jsClick () {
        Logger.infoLog('Click on with js' + this.name)
        const element = await $(this.locator)
        return browser.execute(scriptDataFile.jsClick, element)
    }

    async getTextFromElem () {
        Logger.infoLog('Get text from element' + this.name)
        return await $(this.locator).getText()
    }
}
