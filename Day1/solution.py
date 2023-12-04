
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
    
    def trebuchet2(self, filename):
        f = open(filename, 'r')
        sum = 0
        for line in f:
            line = self.preprocess(line)
            first = None
            last = None
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
    
    def preprocess(self, line):
        memo = [0] * len(line)
        newLine = ''
        for spelledNum in self.spelledNums.keys():
            if len(line) < len(spelledNum):
                pass
            else:
                start = 0
                end = len(spelledNum)
                while end <= len(line):
                    if line[start:end] == spelledNum:
                        memo[start] = self.spelledNums[spelledNum]
                    start += 1
                    end += 1
        for i in range(len(line)):
            if memo[i] != 0:
                newLine += str(memo[i])
            else:
                newLine += line[i]  
        return newLine