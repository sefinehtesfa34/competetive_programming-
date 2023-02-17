/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    let answer = []
    const generator = (closed, opened, temp) => {
        if (closed > opened || closed > n || opened > n){
            return 
        }
        if (closed === opened && closed == n){
            answer.push(temp.slice().join(""))
            return 
        }
        
        temp.push(")")
        generator(closed + 1, opened, temp)
        temp.pop()
        temp.push("(")
        generator(closed, opened + 1, temp)
        temp.pop()
    }
    generator(0, 0, [])
    return answer
};