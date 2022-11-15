import HomePage from '../../page/Homepage.js'
import RegistrationPage from '../../page/RegistrationPage.js'
import { assert } from 'chai'
import Logger from '../../utils/logUtils.js'

describe('Timer, Hide form, Cookie', function () {

    it('Check if page is opened, timer at zero, hide form is closed and cookie accept', async function () {
        Logger.infoLog('Navigate to home page')
        assert.isTrue(await HomePage.isPageOpen(), 'Homepage is not opened')

        Logger.infoLog('Navigate to Registration page')
        await HomePage.clickHereButton()
        Logger.infoLog('Check timer on page')
        assert.isTrue(await RegistrationPage.getTextTimer(), 'Text from webelement "Timer" and test data are different')

        Logger.infoLog('Hide help form')
        await RegistrationPage.hideForm()
        assert.isTrue(await RegistrationPage.isHideForm(), 'Hide form is not closed')

        Logger.infoLog('Accept cookies')
        await RegistrationPage.acceptCookie()
        assert.isFalse(await RegistrationPage.isAcceptCookie(), 'Cookie form is not closed')
    })
})