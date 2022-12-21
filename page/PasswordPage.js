import BasePage from './BasePage.js';
import Button from '../elements/Button.js';
import TextField from '../elements/TextField.js';
import testData from '../utils/testData.js';

const locatorPasswordField = new TextField('//*[contains(@type,"password")]', 'Password field');
const locatorSubmitButton = new Button('//*[contains(@type,"submit")]', 'Submit password button');

class PasswordPage extends BasePage {

    constructor () {
        super();
    };

    async fillPasswordField () {
        locatorPasswordField.waitForElement();
        return locatorPasswordField.sendKeys(testData.password);
    };

    async clickSubmitButton(){
        return locatorSubmitButton.jsClick();
    };
};

export default new PasswordPage();