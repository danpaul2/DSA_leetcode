from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0
 
        for price in prices:
            if price<minPrice:
                minPrice = price
            elif price-minPrice > maxProfit:
                maxProfit = price-minPrice
        return maxProfit

if __name__ == '__main__':
    sol = Solution()

    sample_list1 = [7,6,4,3,1]
    sample_list2 = [7,1,5,3,6,4]

    print("Profit for sample_list1:",sol.maxProfit(sample_list1))
    print("Profit for sample_list1:",sol.maxProfit(sample_list2))


    

    

    
                


            

        

        