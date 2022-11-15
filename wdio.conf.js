import configData from '../k.strunets/utils/configData.js';
import cleanLogFile from '../k.strunets/utils/cleanLogUtils.js';
import loginData from '../k.strunets/utils/loginData.js'

exports.config = {
    specs: [
        './test/specs/**/*.js'
    ],
    maxInstances: 10,
    capabilities: [
        {
        maxInstances: 1,
        browserName: 'chrome',
        'goog:chromeOptions':{
            args: ['--incognito', '--start-maximized', '--lang=en-GB', '--excludeSwitches']
        },
        acceptInsecureCerts: true
        },
    ],
    logLevel: 'info',
    bail: 0,
    baseUrl: 'http://localhost:8081/web',
    waitforTimeout: 50000,
    connectionRetryTimeout: 120000,
    connectionRetryCount: 5,
    services: ['chromedriver'],
    framework: 'mocha',
    reporters: ['spec'],
    mochaOpts: {
        ui: 'bdd',
        timeout: 60000,
        require: ['@babel/register'],
    },
    onPrepare: async function (config, capabilities) {
        return cleanLogFile(configData.pathLogInfo)
    },
    before: async function (capabilities, specs) {
        await browser.url(`http://${loginData.login}:${loginData.password}@localhost:8081/web`)
    },
    after: async function (result, capabilities, specs) {
        await browser.reloadSession
    },
};