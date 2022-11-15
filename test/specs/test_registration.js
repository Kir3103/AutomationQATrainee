import HomePage from '../../page/Homepage.js'
import RegistrationPage from '../../page/RegistrationPage.js'
import InterestsPage from '../../page/InterestsPage.js'
import PersonalPage from '../../page/PersonalPage.js'
import { assert } from 'chai'
import Logger from '../../utils/logUtils.js'

describe('Registration page', function () {
    
    it('Check if pages are opened and text fields are filled', async function () {
        Logger.infoLog('Navigate to home page')
        assert.isTrue(await HomePage.isPageOpen(), 'Homepage is not opened')
        
        Logger.infoLog('Navigate to Registration page')
        await HomePage.clickHereButton()
        assert.isTrue(await RegistrationPage.isPageOpen(), 'Registration page is not opened')

        Logger.infoLog('Input random valid password, email, accept the terms of use and click "next" button')
        await RegistrationPage.fillPass()
        await RegistrationPage.fillEmail()
        await RegistrationPage.fillDomain()
        await RegistrationPage.selectDropdown()
        await RegistrationPage.termsClick()
        await RegistrationPage.nextClick()
        assert.isTrue(await InterestsPage.isPageOpen(), 'Checkbox with interests is not opened')
    })

    it.skip('Select only 3 interests and upload image', async function () {
        Logger.infoLog('Choose 2 random interest, upload image, click "Next" button')
        await InterestsPage.unselectAll()
        await InterestsPage.selectInterests()
        await InterestsPage.uploadImage()
        await InterestsPage.clickNextBtn()
        assert.isTrue(await PersonalPage.isPageOpen(), 'Personal page is not opened')
    }) 
})
