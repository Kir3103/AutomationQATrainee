class ApiUtils{

    async getUserById(dataArray, userId){
        for (let i = 0; i < (dataArray.length - 1); i++) {
            if(dataArray[i].id === userId){
                return dataArray[i]
            }
        }
    }
}
export default new ApiUtils()