import Label from '../elements/Label.js';
import BasePage from './BasePage.js';
import Button from '../elements/Button.js';
import Image from '../elements/Image.js';

const locatorIdUser = new Label('//*[@class="author"]', 'User ID from last comment');
const locatorTextFromPost = new Label('//*[contains(@class,"wall_post_text")]', 'Text from last post');
const locatorCommentUserId = new Label('//*[@class="reply_author"]//a[@class="author"]', 'User Id from comment');
const locatorLikePost = new Button('//*[contains(@class,"ReactionsContainer")]', 'Button "Like"');
const locatorIdImageLastPost = new Image('//*[contains(@class,"page_post_sized")]//child::a[contains(@href,"")]', 'Image');

class MyProfilePage extends BasePage {

    constructor () {
        super();
    };

    async getUserIdFromLastPost(){
        const userIdPost = await locatorIdUser.getAttributeFromElem('href');
        return userIdPost.slice(3);
    };

    async isTextFromLastPostVisible(text){
        return locatorTextFromPost.getTextFromElementCompareWait(text);
    };

    async getUserIdFromComment(){
        const userIdComment = await locatorCommentUserId.getAttributeFromElem('href');
        return userIdComment.slice(3);
    };

    async clickLikeButton(){
        return locatorLikePost.clickRegular();
    };

    async isPostMiss(){
        return locatorTextFromPost.jsGetText();
    };

    async getImageIdFromLastPost(){
        const imageId = await locatorIdImageLastPost.getAttributeFromElem('href');
        return imageId.slice(1);
    };
};

export default new MyProfilePage();