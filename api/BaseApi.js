import fetch from "node-fetch";
import Logger from '../utils/logUtils.js';

class BaseApi {
    
    static async postRequest(url, methodUrl, data){
        Logger.infoLog(`Send POST request with ${methodUrl} and ${data}`);
        const response = await fetch(url + methodUrl + data, {
            method: 'POST',
        });
        return response;
    };

    static async getRequest(url, methodUrl){
        Logger.infoLog(`Send GET request with ${methodUrl}`);
        const response = await fetch(url + methodUrl);
        return response;
    };
};
export default BaseApi;