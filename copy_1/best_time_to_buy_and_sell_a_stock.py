from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l+=1
                r+=1
            else:
                temp_profit = prices[r] - prices[l]
                max_profit = max(max_profit, temp_profit)
                # trunk-ignore(ruff/E741)
                l = r
                r+=1
        return max_profit


def test_max_profit():
    s = Solution()
    # trunk-ignore(bandit/B101)
    assert s.maxProfit([7,1,5,3,6,4]) == 5
    assert s.maxProfit([7,6,4,3,1]) == 0
    assert s.maxProfit([1,2,3,4,5]) == 4
    assert s.maxProfit([2,4,1]) == 2


def main():
    test_max_profit()

if __name__ == '__main__':
    main()
