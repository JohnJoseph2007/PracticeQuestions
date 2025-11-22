Given n non-negative integers representing an elevation map where the width of each bar is 1

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Input: height = [4,2,0,3,2,5]

Output: 9
Input Format

first line contains size of the input array.
n=6
second line contains input array.
height = [0,1,0,2,1,0,1,3,2,1,2,1]
Constraints

n == height.length
1 <= n <= 2 \* 10^4
0 <= height[i] <= 10^5
Output Format

6

Sample Input 0

12
0 1 0 2 1 0 1 3 2 1 2 1
Sample Output 0

6
Sample Input 1

6
4 2 0 3 2 5
Sample Output 1

9
