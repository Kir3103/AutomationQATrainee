import BaseApi from "./BaseApi.js"
import testData from "../utils/testData.js"
import headerData from "../utils/headerData.js"

class JsonPlaceholderApi extends BaseApi {

    static async getAllPosts(){
        return await BaseApi.getRequest(testData.url, testData.request.posts)
    }

    static async get99Posts(){
        return await BaseApi.getRequest(testData.url, testData.request.posts99)
    }

    static async get150Posts(){
        return await BaseApi.getRequest(testData.url, testData.request.posts150)
    }

    static async postRandomText(dataRandom){
        const data = JSON.stringify(dataRandom)
        return await BaseApi.postRequest(testData.url, testData.request.posts, headerData.headerJson, data)
    }

    static async getUsers(){
        return await BaseApi.getRequest(testData.url, testData.request.users)
    }

    static async get5Users(){
        return await BaseApi.getRequest(testData.url, testData.request.users5)
    }

}
export default JsonPlaceholderApi