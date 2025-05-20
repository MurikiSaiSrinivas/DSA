class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coinsCount = [float('inf')] * (amount+1)
        coinsCount[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >=0:
                    coinsCount[i] = min(coinsCount[i], coinsCount[i - coin]+1)
        return coinsCount[amount] if coinsCount[amount] != float('inf') else -1
                