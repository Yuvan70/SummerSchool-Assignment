
#assignment 1 2nd question cs20b070

class IndicesFind :
    def __init__(self,array,target) :
         self.arr = array
         self.target = target
         self.solution = {}

         ans = 0
         for i in range (len(self.arr)):
            for j in range (len(self.arr)):
              if (self.arr[i] + self.arr[j] == self.target):
                ans+=1
                self.solution[ans] = [i, j]

    def PrintSolution (self):
         print(self.solution)

array = [10,20,10,40,50,60,70]
target = 50

numbers = IndicesFind(array,target)
numbers.PrintSolution()