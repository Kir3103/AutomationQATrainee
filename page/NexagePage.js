import BasePage from './BasePage.js';
import Label from '../elements/Label.js';
import StringUtils from '../utils/StringUtils.js';
import Button from '../elements/Button.js';

const locatorTableTests = new Label('//*[@class="table"]//td[4]', 'Table with tests');
const locatorNexagePage = new Label('//*[@id="pie"]', 'Nexage page unique elem');
const locatorNameProject = new Label('//ol[@class="breadcrumb"]//*[contains(text(),"Nexage")]', 'Name project');
const locatorHomeBtn = new Button('//*[contains(@href,"projects")]', 'Home button');

class NexagePage extends BasePage {
    
    constructor () {
        super(locatorNexagePage, 'Nexage page');
    };

    async compareProjectsDate(){
        await locatorNameProject.getTextFromElementCompareWait('Nexage');
        const array = await locatorTableTests.getTextFromElements();

        const arrayForConvert = await StringUtils.convertForDataParse(array);
        const secArray = await StringUtils.getSecond(arrayForConvert);
        return secArray;
    };

    async clickHomeButton(){
        return locatorHomeBtn.clickRegular();
    };
};

export default new NexagePage();