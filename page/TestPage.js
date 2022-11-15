import BasePage from './BasePage.js';
import Label from '../elements/Label.js';
import StringUtils from '../utils/StringUtils.js';
import Button from '../elements/Button.js';

const locatorTableStartTime = new Label('//*[@class="table"]//td[4]', 'Table with start time in tests');
const locatorTableTestMethod = new Label('//*[@class="table"]//td[2]', 'Table with test method in tests');
const locatorNameProject = new Label('//ol[@class="breadcrumb"]//*[contains(text(),"Nexage")]', 'Name project');
const locatorHomeBtn = new Button('//*[contains(@href,"projects")]', 'Home button');

class TestPage extends BasePage {
    
    constructor () {
        super();
    };

    async compareProjectsDate(){
        await locatorNameProject.getTextFromElementCompareWait('Nexage');
        const array = await locatorTableStartTime.getTextFromElements();

        const arrayForConvert = await StringUtils.convertForDataParse(array);
        const secArray = await StringUtils.getSecond(arrayForConvert);
        return secArray;
    };

    async clickHomeButton(){
        return locatorHomeBtn.clickRegular();
    };

    async isTestVisible(textFromElem){
        return locatorTableTestMethod.getTextFromElementCompareWait(textFromElem);
    };
};

export default new TestPage();