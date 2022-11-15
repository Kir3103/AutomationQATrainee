import fs from 'fs';

export default function cleanLogFile(filePath){
    fs.access(filePath, (err) =>{
        if(!err) {
            return fs.unlinkSync(filePath)
        };
    });
    
};