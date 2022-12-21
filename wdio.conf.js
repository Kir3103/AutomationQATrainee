import configData from './utils/configData.js';
import cleanLogFile from './utils/cleanLogUtils.js';

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
            args: ['--incognito', '--start-maximized', '--lang=en-GB']
        },
        acceptInsecureCerts: true
        },
        // {
        // browserName: 'firefox',
        // 'moz:firefoxOptions':{
        //     args: ['--incognito', '--start-maximized']
        // },
        // acceptInsecureCerts: true
        // }
    ],
    logLevel: 'info',
    bail: 0,
    baseUrl: 'https://vk.com',
    waitforTimeout: 30000,
    connectionRetryTimeout: 120000,
    connectionRetryCount: 5,
    services: ['chromedriver'],
    // services: ['geckodriver'],
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
        await browser.url('/')
    },
    after: async function (result, capabilities, specs) {
        await browser.reloadSession
    },
};