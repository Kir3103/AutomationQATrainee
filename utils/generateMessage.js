import Logger from '../utils/logUtils.js';

export default function generateMessage() {

    let resultMessage = '';
    const length = 10;
    const valueForMessage = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    for (var i = 0, n = valueForMessage.length; i < length; ++i) {
        resultMessage += valueForMessage.charAt(Math.floor(Math.random() * n));
    };
    Logger.infoLog('Generate random message');
    return resultMessage;
};