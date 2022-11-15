import BaseElement from "./BaseElement.js";
import Logger from '../utils/logUtils.js';

export default class TextField extends BaseElement{
    async sendKeys (value) {
        Logger.infoLog('Send value to element ' + this.name);
        $(this.locator).clearValue();
        return (await $(this.locator).setValue(value));
    };
};