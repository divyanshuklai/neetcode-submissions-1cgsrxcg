class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks)%4==0:
            target = sum(matchsticks)//4
            
            matchsticks.sort(reverse=True)
            if matchsticks[0] > target:
                return False

            memo = set()
            def backtrack(side, length, sticks, used):
                if side == 0:
                    return True
                if length == 0 :
                    return backtrack(side-1, target, sticks, used)
                if length < 0:
                    return False
                if (side, length, used) in memo:
                    return False
                
                        
                for i in range(0, len(sticks)):
                    if 1 << i & used == 0 :
                        used |= 1 << i
                        stick = sticks[i]
                        if backtrack(side, length-stick, sticks, used):
                            return True
                        used &= ~(1 << i)

                memo.add((side, length, used))
                return False

            return backtrack(4, target, matchsticks, 0)
        return False
    
    