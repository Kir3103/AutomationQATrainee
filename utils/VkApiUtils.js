import FormData from 'form-data';
import VkApi from '../api/VkApi.js';
import apiData from './apiData.js';
import Logger from './logUtils.js';
import fs from 'fs';
import testData from './testData.js';


class VkApiUtils{

    async postOnWall(text) {

        let dataApi = new FormData();
        dataApi.append('access_token', apiData.token);
        dataApi.append('message', text);
        dataApi.append('v', apiData.v);
        Logger.infoLog('Post new post on Wall');
        const responseServer = await VkApi.postWall(dataApi);
        const responseJson = await responseServer.json();
        return responseJson.response.post_id.toString();
    };

    async getUrlUploadImage(){
        let dataApi = new FormData();
        dataApi.append('access_token', apiData.token);
        dataApi.append('v', apiData.v);
        Logger.infoLog('Get url to upload image on wall');
        const responseServer = await VkApi.postUrlUploadImage(dataApi);
        const responseJson = await responseServer.json();
        return responseJson.response.upload_url;
    };

    async uploadImage(){
        const urlImageFromVk = await this.getUrlUploadImage();
        let dataApiImage = new FormData();
        dataApiImage.append('photo', fs.createReadStream(apiData.imageUpload)); // when use __dir, get error:device_event_log_impl.cc(214)
        Logger.infoLog('Upload image to server');
        const responseServer = await VkApi.postUploadImage(urlImageFromVk, dataApiImage);
        const responseJson = await responseServer.json();
        return responseJson;
    };
    
    async postImageWall(){
        const imageToWall = await this.uploadImage();
        let dataApi = new FormData();
        dataApi.append('access_token', apiData.token);
        dataApi.append('v', apiData.v);
        dataApi.append('user_id', testData.userId);
        dataApi.append('server', imageToWall.server);
        dataApi.append('hash', imageToWall.hash);
        dataApi.append('photo', imageToWall.photo);
        Logger.infoLog('Post image on wall');
        const responseServer = await VkApi.postImage(dataApi);
        const responseJson = await responseServer.json();
        return 'photo' + testData.userId + "_" + responseJson.response[0].id;
    };

    async editPost(idPost, editText, image) {
        let dataApi = new FormData();
        dataApi.append('access_token', apiData.token);
        dataApi.append('message', editText);
        dataApi.append('v', apiData.v);
        dataApi.append('post_id', idPost);
        dataApi.append('attachments', image);
        Logger.infoLog('Edit post on wall with new comment and image');
        return await VkApi.postEdit(dataApi);
    };

    async addComment(idPost, text){
        let dataApi = new FormData();
        dataApi.append('access_token', apiData.token);
        dataApi.append('v', apiData.v);
        dataApi.append('post_id', idPost);
        dataApi.append('message', text);
        Logger.infoLog('Add comment to post');
        return await VkApi.postAddComment(dataApi);
    };

    async getLikeList(idPost){
        let dataApi = new FormData();
        dataApi.append('access_token', apiData.token);
        dataApi.append('v', apiData.v);
        dataApi.append('type', 'post');
        dataApi.append('item_id', idPost);
        Logger.infoLog('Check user id from like with api');
        const responseServer = await VkApi.postLikeList(dataApi);
        const responseJson = await responseServer.json();
        return responseJson.response.items.toString();
    };

    async deletePost(idPost){
        let dataApi = new FormData();
        dataApi.append('access_token', apiData.token);
        dataApi.append('v', apiData.v);
        dataApi.append('post_id', idPost);
        Logger.infoLog('Post to delete post with api');
        return await VkApi.postDelete(dataApi);
    };

};
export default new VkApiUtils();