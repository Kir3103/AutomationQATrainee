import BasePage from './BasePage.js';
import Button from '../elements/Button.js';
import Label from '../elements/Label.js';
import BrowserUtils from '../utils/BrowserUtils.js';

const locatorHomePage = new Label('//*[contains(text(),"projects")]', 'HomePage');
const locatorVersion = new Label('//span[contains(text(),"Version")]', 'Version test');
const locatorNexageBtn = new Button('//*[contains(text(),"Nexage")]', 'Nexage button');
const locatorAddBtn = new Button('//*[contains(@class,"btn-xs")]', '+Add button');
const locatorProjectList = new Label('//*[contains(@class,"item")]', 'List with all projects');

class HomePage extends BasePage {
    
    constructor () {
        super(locatorHomePage, 'Homepage projects');
    };

    async getVersionTest () {
        return locatorVersion.getTextFromElem();
    };

    async refreshHomePage(){
        return BrowserUtils.refreshPage();
    };

    async clickNexageBtn(){
        return locatorNexageBtn.clickRegular();
    };

    async clickAddBtn(){
        return locatorAddBtn.clickRegular();
    };

    async getListProjects(){
        return locatorProjectList.getTextFromElements();
    };

    async clickOnNewProject(textProject){
        return locatorProjectList.clickOnElementWithText(textProject);
    };

    async getProjectId(numb){
        const projectIdData = await locatorNexageBtn.getAttributeFromElem('href');
        return await projectIdData.slice(numb);
    };
};

export default new HomePage();