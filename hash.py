
class Find_mod:
    def __init__(self):
        self.size = int(input())
        self.strings = list(input())
        self.mod_num = 1234567891
        self.sum = 0
    
    def hash(self,num,index):
        if index == self.size:
            print(self.sum)
            return

        if num > self.mod_num:
            self.sum += (num * (ord(self.strings[index]) - 96)) % self.mod_num

        else:
            self.sum += num * (ord(self.strings[index]) - 96)

        num = num * 31
        index += 1
        self.hash(num,index)
    
if __name__ == "__main__":
    h = Find_mod()
    h.hash(1,0)