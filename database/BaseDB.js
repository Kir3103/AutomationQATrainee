import { createPool } from "mysql2";

class BaseDB{

    static connectionToDB(hostDb, userDb, nameDb, passwordDb){

        const pool = createPool({
            host: hostDb,
            user: userDb,
            database: nameDb,
            password: passwordDb,
            connectionLimit: 10
        });
        return pool.promise();
    }

    static async queryToDB(queryData, dataBase){
        return dataBase.execute(queryData)
        .then( ([rows]) => {
            dataBase.end();
            return rows;
        })
    }
}

export default BaseDB;