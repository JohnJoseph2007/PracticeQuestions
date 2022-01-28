# Monk and Rotation
# Link: https://www.hackerearth.com/practice/codemonk/
# Monk loves to perform different operations on arrays, and so being the principal of Hackerearth School, he assigned a task to his new student Mishki. Mishki will be provided with an integer array A of size N and an integer K , where she needs to rotate the array in the right direction by K steps and then print the resultant array. As she is new to the school, please help her to complete the task.

# Video approach to solve this question: https://youtube.com/watch?v=mX38pWM--0M&list=PL1YS4hYJip07A-YteNUR8qTeA_wHQarDX&index=42

# Input:
# The first line will consists of one integer T denoting the number of test cases.
# For each test case:
# 1) The first line consists of two integers N and K, N being the number of elements in the array and K denotes the number of steps of rotation.
# 2) The next line consists of N space separated integers , denoting the elements of the array A.

# Output:
# Print the required array.

# Sample Input:
# 1 (T)
# 5 2 (N, K)
# 1 2 3 4 5 (List)
# Sample Output:
# 4 5 1 2 3 (Shifted Array)

# Explanation
# Here T is 1, which means one test case.
# N = 5, denoting the number of elements in the array and K = 2, denoting the number of steps of rotations.
# The initial array is: 1, 2, 3, 4, 5
# In first rotation, 5 will come in the first position and all other elements will move to one position ahead from their current position. Now, the resultant array will be: 5, 1, 2, 3, 4
# In second rotation, 4 will come in the first position and all other elements will move to one position ahead from their current position. Now, the resultant array will be: 4, 5, 1, 2, 3

## CODE HERE :

t=int(input())
for i in range(t):
    n, k = map(int, input().split())
    listinput = list(map(int, input().split()))
    x = k%n
    print(*(listinput[n-x:] + listinput[:n-x]))
    #listinput[n-x:] prints everything after index n-x
    #listinput[:n-x] prints everything before index n-x
    # print(*()) removes all metacharacters and converts 2d array into normal space-separated string

# Status: Finished
