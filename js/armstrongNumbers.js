exports.findArmstrongNumbers = function(arr) {

    answer = []

    for (let i = 0; i < arr.length; i++) {
      
        let times = Math.ceil(Math.log10(i))

        if(arr[i] < 2) {
            answer.push(i)
        } else {
            let sums = 0
            
            let temp = i
            for (let j = 0; j < times; j++) {
                let remainder = temp % 10
                sums += remainder ** times
                temp = Math.floor(temp / 10)
            }
            if (sums === i) {
                answer.push(i)
            }
        }  
    }
    return answer
}