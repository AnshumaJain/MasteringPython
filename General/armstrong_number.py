"""""
LeetCode Problem #1134: Armstrong Number

The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.
Given a positive integer N, return true if and only if it is an Armstrong number.

Example 1:
Input: 153
Output: true
Explanation: 
153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.
"""""


class Solution:
    @staticmethod
    def is_armstrong(n: int) -> bool:
        num = str(n)
        ln = len(num)

        arm_num = 0
        for i in num:
            # raise and add each digit to the power of length
            arm_num += int(i) ** ln

        return arm_num == n


if __name__ == "__main__":
    sol = Solution()
    print(sol.is_armstrong(153))
