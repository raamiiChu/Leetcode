// set

/**
 * @param {number[]} nums
 * @return {boolean}
 */

// Time complexity: O(n)
// Space complexity: O(n)

var containsDuplicate = function(nums) {
    // 創建 set
    let numSet = new Set(nums);

    // 比較 set 跟 array 是否等長 
    return numSet.size !== nums.length;
};



// sort

/**
 * @param {number[]} nums
 * @return {boolean}
 */

// Time Complexity: O(N logn)
// Space Complexity: O(1)

var containsDuplicate = function(nums) {
    // 排序
    nums.sort();

    // 索引值, 數字
    for (let [index, value] of nums.entries()){
        // 當前數字是否等於前項數字
        if (value === nums[index-1]){
            return true;
        }
    }
    return false;
};