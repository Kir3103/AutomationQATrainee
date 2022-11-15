import BaseElement from "./BaseElement.js"
import Logger from '../utils/logUtils.js'

export default class Upload extends BaseElement{
    async uploadFile (path) {
        Logger.infoLog('Upload file to element' + this.name)
        const input = $(this.locator)
        return (await input.setValue(path))
    }
}