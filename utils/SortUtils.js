class SortUtils{

    async ascendingId(dataArray){
        for (let i = 0; i < (dataArray.length - 1); i++){
            if(dataArray[i].id < dataArray[i + 1].id){
                return true
            }else{
                return false
            }
        }
    }
}
export default new SortUtils()