class Solution(object):
    def fizzBuzz(self, n):

        result = []
        
        for i in range(1, n+1):

            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

        return print(result)

        #Usando String:
        
        # result = []
        
        # for i in range(1, n+1):
        #     r = ''
        #     if i % 3 == 0:
        #         r += 'Fizz'
        #     if i % 5 == 0:
        #         r += 'Buzz'
        #     if r == '':
        #         r = i
        #     result.append(str(r))
        # return print(result)

Solution().fizzBuzz(356)