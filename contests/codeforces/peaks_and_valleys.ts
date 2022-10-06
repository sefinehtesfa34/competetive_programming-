const peaksAndValleys = (nums: [number]) => {
    let left, right
    let result!:[number]
    while (left <= right){
        result.push(nums[right])
        result.push(nums[left])
        right--
        left ++
    }
};
