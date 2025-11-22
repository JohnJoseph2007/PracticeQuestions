Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000(use double datatype)
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]

Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Input Format

first line contains size of the first array
n1=2
second line contains 1st array nums1.
nums1 = [1,3].
third line contains size of the second array.
n2=1
fourth line contains 2nd array nums2.
nums2=[2]
Constraints

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
Output Format

2.00000

Sample Input 0

2
1 3
1
2
Sample Output 0

2.00000
Sample Input 1

4
1 3 8 9
5
2 4 6 7 10
Sample Output 1

6.00000
