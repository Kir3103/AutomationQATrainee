import Logger from '../utils/logUtils.js';

export default class BasePage {
    
    constructor(uniqueElem, nameLog) {
        this.uniqueElem = uniqueElem;
        this.nameLog = nameLog;
    };
    
    async isPageOpen () {
        Logger.infoLog(this.nameLog + ' is opened');
        if (this.uniqueElem.getLength() === 0) {
            return false;
        }else {
            return true;
        };
    };
};