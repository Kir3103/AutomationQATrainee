import UnionReporting from '../database/UnionReporting.js'

describe('Get data from Union Reporting DB', function (){

    it('Get min working time, tests count, tests date and browser count', async function(){
        console.table(await UnionReporting.getMinWorkingTime())
        console.table(await UnionReporting.getTestsCount())
        console.table(await UnionReporting.getTestsDate())
        console.table(await UnionReporting.getBrowserCount())
    })
})