from typing import List

class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        play01 = 0
        play02 = 0
        
        bowl_perfect = False
        for i in player1:
            if i == 10:
                bowl_perfect = True
            if bowl_perfect == True:
                play01 += i * 2
            else:
                play01 += i
        for i in player2:
            if i == 10:
                bowl_perfect = True
            if bowl_perfect == True:
                play02 += i * 2
            else:
                play02 += i
    
        
        if play02 > play01:
            print("2")
        elif play01 > play02:
            print("1")
        else:
            print("0")

test_solution = Solution()    
    
test_solution.isWinner(player1=[4,10,7,9], player2=[6,5,2,3])
