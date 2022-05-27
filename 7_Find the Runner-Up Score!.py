# Question 7 - Find the Runner-Up Score!:
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given scores. Store them in a list and find the score of the runner-up.
#
#
# Input Format
#
# The first line contains n. The second line contains an array A[] of integers each separated by a space.
#
# Constraints
# 2 <=n <= 10
# -100 <= A[i] <= 100
#
# Output Format
#
# Print the runner-up score.
#
#
# Sample Input 0
#
# 5
# 2 3 6 6 5
#
# Sample Output 0
#
# 5
#
# Explanation 0
#
# Given list is . The maximum score is , second maximum is . Hence, we print as the runner-up score


arr = [5, 2, 3, 6, 6, 5]
new_list = set(arr)
new_list.remove(max(new_list))
print(max(new_list))
