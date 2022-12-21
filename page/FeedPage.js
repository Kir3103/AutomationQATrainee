import BasePage from './BasePage.js';
import Button from '../elements/Button.js';

const locatorMyProfileButton = new Button('//*[@id="l_pr"]//span[contains(@class,"inl_bl")]', 'My profile button');

class FeedPage extends BasePage {
    
    constructor () {
        super();
    };

    async clickMyProfileButton(){
        return locatorMyProfileButton.clickRegular();
    };
};

export default new FeedPage();