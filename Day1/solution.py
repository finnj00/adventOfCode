
class Solution:

    def __init__(self):
        self.spelledNums = {}
        self.spelledNums['one'] = 1
        self.spelledNums['two'] = 2
        self.spelledNums['three'] = 3
        self.spelledNums['four'] = 4
        self.spelledNums['five'] = 5
        self.spelledNums['six'] = 6
        self.spelledNums['seven'] = 7
        self.spelledNums['eight'] = 8
        self.spelledNums['nine'] = 9

    def trebuchet(self, filename):
        
        f = open(filename, 'r')
        sum = 0
        for line in f:
            first = None
            last = None
            cur = ''
            for char in line:
                if char.isdigit():
                    if first is None:
                        first = char
                        last = char
                    else:
                        last = char            
            combined = first + last
            sum += int(combined)
        f.close()
        return sum
