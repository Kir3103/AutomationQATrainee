import Logger from '../utils/logUtils.js';
import scriptData from '../utils/scriptData.js'
import configData from '../utils/configData.js';


export default class BaseElement {
    
    constructor(locator, name) {
        this.locator = locator;
        this.name = name;
    };
    
    async findElement () {
        Logger.infoLog('Find element ' + this.name);
        return await $(this.locator).isDisplayed();
    };

    async findElements () {
        Logger.infoLog('Find elements ' + this.name);
        return await $$(this.locator).isDisplayed();
    };

    async waitForElement () {
        Logger.infoLog('Find element with wait ' + this.name);
        return await $(this.locator).waitForDisplayed({ timeout: configData.timeout });
    };

    async clickRegular () {
        Logger.infoLog('Click on ' + this.name);
        return await $(this.locator).click();
    };

    async jsClick () {
        Logger.infoLog('Click on with js ' + this.name);
        const element = await $(this.locator);
        return browser.execute(scriptData.jsClick, element);
    };

    async clickOnElementWithText(text){
        Logger.infoLog('Click on element with need text ' + this.name);
        const elements = await $$(this.locator);
        for(let elem = 0; elem < elements.length; elem++){
            if(await elements[elem].getText() === text){
                return await elements[elem].click();
            };
        };
    };

    async scrollToElement(){
        Logger.infoLog('Scroll to ' + this.name);
        const element = await $(this.locator);
        return browser.execute(scriptData.scrollToElement, element);
    };

    async jsGetText(){
        Logger.infoLog('Get text from element with js ' + this.name);
        const element = await $(this.locator);
        return browser.execute(scriptData.text, element);
    };

    async getTextFromElem () {
        Logger.infoLog('Get text from element ' + this.name);
        return await $(this.locator).getText();
    };

    async getTextFromElements(){
        Logger.infoLog('Get text from elements ' + this.name);
        const elements = await $$(this.locator);
        let textArray = [];
        for(let elem = 0; elem < elements.length; elem++){
            textArray.push(await elements[elem].getText());
        };
        return textArray;
    };

    async getAttributeFromElem(value) {
        Logger.infoLog('Get attribute from element ' + this.name);
        return await $(this.locator).getAttribute(value);
    };

    async getTextFromElementCompareWait(text=null){
        Logger.infoLog('Get text from element with wait ' + this.name);
        return await browser.waitUntil(
            async () => (await $(this.locator).getText()) === text, {timeout: configData.timeout});
    };

    async elementIsExisting(){
        Logger.infoLog('Check element exist in DOM ' + this.name);
        return await $(this.locator).isExisting();
    };

    async getLength(){
        Logger.infoLog('Get length of the list elements ' + this.name);
        return this.findElements().length;
    };
};