import BaseDB from "./BaseDB.js"
import queryData from '../utils/queryData.js'
import connectionData from '../utils/connectionData.js'


class UnionReporting extends BaseDB{

    static async connectionToUnionReportBD(){
        return BaseDB.connectionToDB(connectionData.hostDb, connectionData.userDb, 
            connectionData.nameDb, connectionData.passwordDb)
    }

    static async getMinWorkingTime(){
        const connection = await UnionReporting.connectionToUnionReportBD()
        return BaseDB.queryToDB(queryData.queryDb.minWorkingTime, connection)
    }

    static async getTestsCount(){
        const connection = await UnionReporting.connectionToUnionReportBD()
        return BaseDB.queryToDB(queryData.queryDb.testsCount, connection)
    }

    static async getTestsDate(){
        const connection = await UnionReporting.connectionToUnionReportBD()
        return BaseDB.queryToDB(queryData.queryDb.testsDate, connection)
    }

    static async getBrowserCount(){
        const connection = await UnionReporting.connectionToUnionReportBD()
        return BaseDB.queryToDB(queryData.queryDb.browserCount, connection)
    }
}

export default UnionReporting