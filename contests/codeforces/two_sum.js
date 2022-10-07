/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    hashmap = {}
    for (let i = 0; i < nums.length; i ++){
        if (nums[i] in hashmap){
            return [i, hashmap[nums[i]]];
        }
        hashmap[target - nums[i]] = i;
    }
    
};