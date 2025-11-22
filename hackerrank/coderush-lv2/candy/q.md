There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Input: ratings = [1,2,2]

Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
Input Format

first line should for length of rating. second line should for input array

n=3 ratings = [1,0,2]

Constraints

n == ratings.length
1 <= n <= 2 _ 10^4
0 <= ratings[i] <= 2 _ 10^4
Output Format

5

Sample Input 0

3
1 0 2
Sample Output 0

5
Sample Input 1

4
1 1 1 1
Sample Output 1

4
