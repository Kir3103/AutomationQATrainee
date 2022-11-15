import BasePage from './BasePage.js';
import Button from '../elements/Button.js';
import TextField from '../elements/TextField.js';
import Label from '../elements/Label.js';

const locatorAddProjectName = new TextField('//*[@id="projectName"]', 'Text field Project name');
const locatorSaveNewProject = new Button('//*[@id="addProjectForm"]//button[@type="submit"]', 'Submit button');
const locatorSuccessText = new Label('//*[@id="addProjectForm"]//div[contains(@class,"success")]', 'Project saved');

class AddProjectPage extends BasePage {
    
    constructor () {
        super();
    };

    async fillNewProject(text){
        return locatorAddProjectName.sendKeys(text);
    };

    async clickSubmitBtn(){
        return locatorSaveNewProject.clickRegular();
    };

    async getSuccessText(){
        return locatorSuccessText.getTextFromElem();
    };

};

export default new AddProjectPage();