import fetch from 'node-fetch';

class BaseApi {

    static async postRequest(url, methodUrl, data){
        const response = await fetch(url + methodUrl, {
            method: "POST",
            body: data
        });
        return response;
    };

    static async getRequest(url, methodUrl){
        const response = await fetch(url + methodUrl);
        return response;
    };

    static async postRequestMultipartData(urlResponse, data){
        const response = await fetch(urlResponse, {
            method: "POST",
            body: data,
        });
        return response;
    };
};
export default BaseApi;