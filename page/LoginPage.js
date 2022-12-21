import BasePage from './BasePage.js';
import Button from '../elements/Button.js';
import Label from '../elements/Label.js';
import TextField from '../elements/TextField.js';
import testData from '../utils/testData.js';

const locatorHomePage = new Label('//*[@id="index_login"]', 'Home Page');
const locatorLoginField = new TextField('//*[@id="index_email"]', 'Fill login');
const locatorSignInButton = new Button('//*[contains(@class,"FlatButton") and contains(@type,"submit")]', 'Button "Sign in"');

class HomePage extends BasePage {
    
    constructor () {
        super(locatorHomePage, 'VK page');
    };

    async fillLoginField () {
        return locatorLoginField.sendKeys(testData.login);
    };

    async clickSignInButton(){
        return locatorSignInButton.clickRegular();
    };
};

export default new HomePage();