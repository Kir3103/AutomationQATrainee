import BaseApi from "./BaseApi.js";
import requestData from "../utils/requestData.js";

class Variant2Api extends BaseApi {

    static async getToken(data){
        return BaseApi.postRequest(requestData.urlApi, requestData.getToken, data);
    };

    static async getTests(data){
        return BaseApi.postRequest(requestData.urlApi, requestData.getProjectsJson, data);
    };

    static async postTest(data){
        return BaseApi.postRequest(requestData.urlApi, requestData.postNewTest, data);
    };

    static async postLog(data){
        return BaseApi.postRequest(requestData.urlApi, requestData.postLog, data);
    };

    static async postData(data){
        return BaseApi.postRequest(requestData.urlApi, requestData.postData, data);
    };
};
export default Variant2Api;