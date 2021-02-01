class Solution:
    def isValid(self, s: str) -> bool:
        left = '([{'
        xs = []
        for x in s:
            if x in left:
                xs.append(x)
            else:
                if xs:   
                    target = xs.pop() + x
                    if not target in '()[]{}':
                        return False
                else:
                    return False
        
        return not xs
