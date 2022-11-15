import Logger from '../utils/logUtils.js'

export default function generatePassword(passwordLength) {
  
  let resultPassword = 'K9tи'
  let length = passwordLength - resultPassword.length
  const valueForPass = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'  
  for (var i = 0, n = valueForPass.length; i < length; ++i) {
    resultPassword += valueForPass.charAt(Math.floor(Math.random() * n))
}
  Logger.infoLog('Generate random password')
  return resultPassword
}