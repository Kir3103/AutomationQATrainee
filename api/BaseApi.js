import fetch from 'node-fetch'

class BaseApi {
    
    static async postRequest(url, methodUrl, headers, data){
        const response = await fetch(url + methodUrl, {
            method: "POST",
            headers: headers,
            body: data
        })
        return response
    }

    static async getRequest(url, methodUrl){
        const response = await fetch(url + methodUrl)
        return response
    }
}
export default BaseApi