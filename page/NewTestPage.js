import BasePage from './BasePage.js';
import Label from '../elements/Label.js';

const locatorTableTests = new Label('//*[@class="table"]//td[2]', 'Table with tests');

class NewTestPage extends BasePage {
    
    constructor () {
        super();
    };

    async isTestVisible(textFromElem){
        return locatorTableTests.getTextFromElementCompareWait(textFromElem);
    };
};

export default new NewTestPage();