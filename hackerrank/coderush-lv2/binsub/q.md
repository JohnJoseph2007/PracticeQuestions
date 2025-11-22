Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal. A subarray is a contiguous part of the array.

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below: [1,0,1,0,1] [1,0,1,0,1] [1,0,1,0,1] [1,0,1,0,1]
Input Format

The first line should be for an integer N (size of the array).
The second line should be for the array.
The third line should be for the goal.
n=5
nums = [1,0,1,0,1]
goal = 2
Constraints

1 <= nums.length <= 3 \* 10^4
nums[i] is either 0 or 1.
0 <= goal <= nums.length
Output Format

4

Sample Input 0

5
1 0 1 0 1
2
Sample Output 0

4
Sample Input 1

4
0 0 0 0
0
Sample Output 1

10
