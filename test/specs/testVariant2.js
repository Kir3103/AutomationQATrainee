import { assert } from 'chai';
import Logger from '../../utils/logUtils.js';
import ApiUtils from '../../utils/ApiUtils.js';
import HomePage from '../../page/HomePage.js';
import testData from '../../utils/testData.js';
import TestPage from '../../page/TestPage.js';
import StringUtils from '../../utils/StringUtils.js';
import SortUtils from '../../utils/SortUtils.js';
import HandlesUtils from '../../utils/HandlesUtils.js';
import AddProjectPage from '../../page/AddProjectPage.js';
import BrowserUtils from '../../utils/BrowserUtils.js';
import generateMessage from '../../utils/generateMessage.js';
import requestData from '../../utils/requestData.js';
import configData from '../../utils/configData.js';


describe('Test Variant 2 (UI + API)', function (){

    it('Authorization, get list with all tests, add new project and new test', async function(){
        
        Logger.infoLog('Get the token according to the option number');
        const token = await ApiUtils.postToken();
        assert.exists(token, 'Token is not received');

        Logger.infoLog('Complete the necessary authorization. Pass the generated token');
        await HomePage.isPageOpen();
        await BrowserUtils.setCookie(token, "token");
        await HomePage.refreshHomePage();
        const testVersion = await HomePage.getVersionTest();
        assert.equal(testVersion, testData.version, 'Version is different');

        Logger.infoLog('Go to the Nexage page and get first 20 test. Check sorted data');
        const projectId = await HomePage.getProjectId(configData.sliceNumbProjectId);
        await HomePage.clickNexageBtn();
        const startTimeArrayPage = await TestPage.compareProjectsDate();
        assert.isTrue(await SortUtils.descendingDate(startTimeArrayPage), 'Test date is not sorted');

        Logger.infoLog('Query the API to get a list of tests. Check sorted data');
        const allTestsApi = await ApiUtils.postAllTests(projectId);
        const startTimeArrayApi = await StringUtils.getStartTimeArray(allTestsApi);
        const startTimeArrayAfterConvertApi = await StringUtils.convertForDataParse(startTimeArrayApi);
        const startTimeArraySecApi = await StringUtils.getSecond(startTimeArrayAfterConvertApi);
        const startTimeArraySecApiSort = await StringUtils.arraySortAndSlice(startTimeArraySecApi, 
            configData.startNumbSort, configData.endNumbSort);
        assert.deepEqual(startTimeArrayPage, startTimeArraySecApiSort, 'Projects from API and Page are different');

        Logger.infoLog('Go back to the Homepage, click +Add button and go to the new tab');
        await TestPage.clickHomeButton();
        const homepageHandle = await HandlesUtils.getCurrentHandle();
        await HomePage.clickAddBtn();
        const allHandles = await HandlesUtils.getAllHandles();
        for(const handle of allHandles){
            if(handle !== homepageHandle){
                await HandlesUtils.switchWindow(handle);
            };
        };
        Logger.infoLog('Add new project, compare urls before/after and go to the Homepage');
        const urlAddProject = HandlesUtils.getCurrentUrl();
        const projectName = generateMessage();
        await AddProjectPage.fillNewProject(projectName);
        await AddProjectPage.clickSubmitBtn();
        const textFromSuccessMsg = await AddProjectPage.getSuccessText();
        assert.deepEqual(textFromSuccessMsg, `Project ${projectName} saved`, 'Message is not visible or different');
        await HandlesUtils.closeCurrentWindow();
        await HandlesUtils.switchWindow(homepageHandle);
        await BrowserUtils.refreshPage();
        const urlHomePage = HandlesUtils.getCurrentUrl();
        assert.notEqual(urlAddProject, urlHomePage, 'Add project page is not closed');
        const listWithAllProjects = await HomePage.getListProjects();
        assert.include(listWithAllProjects, projectName, 'New project is not displayed');
        
        Logger.infoLog('Go to the created project. Add a test with screenshot and log using API');
        await HomePage.clickOnNewProject(projectName);
        Logger.infoLog('Generate SID, test name and test method');
        const sid = generateMessage();
        const testName = generateMessage();
        const testMethod = generateMessage();
        await BrowserUtils.takeScreenshot();
        const idTest = await ApiUtils.postNewTest(sid, projectName, testName, testMethod);
        await ApiUtils.postNewLog(idTest, configData.pathLogInfo);
        const screenshotConvert64 = await StringUtils.decodeString64(configData.pathScreenshot);
        await ApiUtils.postScreenshot(idTest, screenshotConvert64, requestData.contentTypeImage);
        assert.isTrue(await TestPage.isTestVisible(testMethod), 'New test is not visible');
    });
});