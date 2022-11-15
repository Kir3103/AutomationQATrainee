import Variant2Api from '../api/Variant2Api.js';
import { URLSearchParams } from 'url';
import requestData from './requestData.js';
import Logger from '../utils/logUtils.js';
import fs from 'fs';

class ApiUtils{

    async postToken() {
        Logger.infoLog(`Set search parametres ${requestData.variant}`);
        const dataApi = new URLSearchParams(requestData.variant).toString();
        const responseServer = await Variant2Api.getToken('?' + dataApi);
        Logger.infoLog('Return token from server in text');
        return await responseServer.text();
    };

    async postAllTests(projectId){
        Logger.infoLog(`Set search parametres projectId`);
        const dataApi = new URLSearchParams(projectId);
        const responseServer = await Variant2Api.getTests('?' + dataApi);
        const allTests = await responseServer.json();
        Logger.infoLog('Return response with all tests from server in JSON');
        return allTests;
    };

    async postNewTest(sid, nameProject, nameTest, nameMethod){
        Logger.infoLog('Set search parametres for post new test');
        const dataApi = new URLSearchParams();
        dataApi.set('SID', sid);
        dataApi.set('projectName', nameProject);
        dataApi.set('testName', nameTest);
        dataApi.set('methodName', nameMethod);
        dataApi.set('env', requestData.hostname);
        dataApi.toString();
        const responseServer = await Variant2Api.postTest('?' + dataApi);
        Logger.infoLog('Return id test from server in text');
        return responseServer.text();
    };

    async postNewLog(testId, content){
        Logger.infoLog('Set search parametres for post log');
        const dataApi = new URLSearchParams();
        dataApi.set('testId', testId);
        dataApi.set('content', fs.readFileSync(content));
        dataApi.toString();
        const responseServer = await Variant2Api.postLog('?' + dataApi);
        Logger.infoLog('Add log to test');
        return responseServer;
    };

    async postScreenshot(testId, content, contentType){
        Logger.infoLog('Set search parametres for post attachment');
        const dataApi = new URLSearchParams();
        dataApi.set('testId', testId);
        dataApi.set('content', content);
        dataApi.set('contentType', contentType);
        dataApi.toString();
        const responseServer = await Variant2Api.postData('?' + dataApi);
        Logger.infoLog('Add file to test');
        return responseServer;
    };
};

export default new ApiUtils();