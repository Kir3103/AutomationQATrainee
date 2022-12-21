import winston from 'winston';
const { timestamp, combine, printf, align, json } = winston.format;

export default new class Logger {

    constructor(){
        this.logger = winston.createLogger({
            format: combine(timestamp({ 
                format: 'YYYY-MM-DD HH:mm:ss'
            }),
                align(),
                json(),
                printf((info) => `[${info.timestamp}] ${info.level}: ${info.message}`)),
            transports: [
                new winston.transports.File({
                    filename: 'resources/logFile.log'
                })
            ]
        });
    };

    infoLog(message){
        return this.logger.info(message);
    };

    errorLog(message){
        return this.logger.error(message);
    };
};