import Logger from '../utils/logUtils.js';

export default class HandlesUtils {

    static async getCurrentHandle(){
        Logger.infoLog('Get current handle');
        return await browser.getWindowHandle();
    };

    static async getAllHandles(){
        Logger.infoLog('Get all handles');
        return await browser.getWindowHandles();
    };

    static async closeCurrentWindow(){
        Logger.infoLog('Close current window');
        return await browser.closeWindow();
    };

    static async switchWindow(handle){
        Logger.infoLog('Go to new window');
        return await browser.switchToWindow(handle);
    };

    static async getCurrentUrl(){
        Logger.infoLog('Get current url');
        return await browser.getUrl();
    };
};