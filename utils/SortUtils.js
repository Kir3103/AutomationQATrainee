import Logger from '../utils/logUtils.js';

export default class SortUtils{

    static async descendingDate(dataArray){
        Logger.infoLog('Sort date by descending');
        for(let i = 0; i < dataArray.length; i++){
            if(dataArray[i] > dataArray[i + 1]){
                return true;
            }else {
                return false;
            };
        };
    };
};