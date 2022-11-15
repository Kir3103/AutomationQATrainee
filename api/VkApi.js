import BaseApi from "./BaseApi.js";
import apiData from "../utils/apiData.js";

class VkApi extends BaseApi {

    static async postWall(data){
        return await BaseApi.postRequest(apiData.apiUrl, apiData.post, data);
    };

    static async postUrlUploadImage(data){
        return await BaseApi.postRequest(apiData.apiUrl, apiData.getWallUploadServer, data);
    };

    static async postUploadImage(urlResponse, data){
        return await BaseApi.postRequestMultipartData(urlResponse, data);
    };

    static async postImage(data){
        return await BaseApi.postRequest(apiData.apiUrl, apiData.saveWallPhoto, data);
    };

    static async postEdit(data){
        return await BaseApi.postRequest(apiData.apiUrl, apiData.wallEdit, data);
    };

    static async postAddComment(data){
        return await BaseApi.postRequest(apiData.apiUrl, apiData.wallcreateComment, data);
    };

    static async postLikeList(data){
        return await BaseApi.postRequest(apiData.apiUrl, apiData.likesgetList, data);
    };

    static async postDelete(data){
        return await BaseApi.postRequest(apiData.apiUrl, apiData.walldelete, data);
    };

};
export default VkApi;