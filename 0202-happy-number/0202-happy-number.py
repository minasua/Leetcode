class Solution:
    def isHappy(self, n: int) -> bool:
        catch = []
        next = [int(x) for x in str(n)]
        while True:
            sumn = sum(list(map(lambda x:x**2, next)))
            if sumn != 1:
                if sumn in catch:
                    return False
                catch.append(sumn)
                next = [int(x) for x in str(sumn)]
            else:
                return True