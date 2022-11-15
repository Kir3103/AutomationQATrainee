import Logger from '../utils/logUtils.js';
import configData from './configData.js';

export default class BrowserUtils {

    static async refreshPage() {
        Logger.infoLog('Refresh page');
        return browser.refresh();
    };

    static async takeScreenshot(){
        Logger.infoLog('Save screenshot to directory');
        return browser.saveScreenshot(configData.pathScreenshot);
    };

    static async setCookie(cookieData, cookieName) {
        Logger.infoLog('Set cookie');
        return browser.setCookies({
            name: cookieName,
            value: cookieData
        });
    };
};