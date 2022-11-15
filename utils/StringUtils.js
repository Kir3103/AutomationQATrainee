import Logger from '../utils/logUtils.js';

export default class StringUtils {

    static async convertForDataParse(dataArray){
        const newArray = [];
        for(let elem = 0; elem < dataArray.length; elem++){
            newArray.push(await dataArray[elem].replace(/-/g, '.').slice(0, 19));
        };
        Logger.infoLog('Return array with need data for getSecond()');
        return newArray;
    };

    static async getSecond(dataArray){
        const allSecond = [];
        for(let sec = 0; sec < dataArray.length; sec++){
            allSecond.push(Date.parse(dataArray[sec])/1000);
        };
        Logger.infoLog('Return array with unicode second');
        return allSecond;
    };

    static async getStartTimeArray(array){
        const arrayStartTime = [];
        for(let numb = 0; numb < array.length; numb++){
            arrayStartTime.push(array[numb].startTime);
        };
        Logger.infoLog('Return array with data startTime from response API');
        return arrayStartTime;
    };

    static async arraySortAndSlice(array, startNumb, endNumb){
        Logger.infoLog('Return array after sort and slice');
        return array.sort().reverse().slice(startNumb, endNumb)
    };

    static async decodeString64(pathToDecode){
        Logger.infoLog('Return decoded Base64 string');
        const path = require('path');
        const pathToScreenshot = path.join(__dirname, '..', pathToDecode);
        return btoa(pathToScreenshot);
    };
};