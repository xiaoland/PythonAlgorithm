# coding=utf-8
# author: Lan_zhijiang
# description: 康托运算及其逆运算

from base.basic_algorithm import BasicAlgorithm

class CartonCompute():
    
    def __init__(self):
    
        self.basicAlgorithm = BasicAlgorithm()

    def carton_opreation(self, array, length):

        """
        康托展开
        :param array: 序列
        :param length: 序列长度
        :return int
        """
        if len(array) != length:
            raise Exception("The real length of array is not same as the length you gave!")

        appear = []
        ans = 0
        for i in range(0, length):
            nac = 0
            for j in range(1, array[i]):
                if j not in appear:
                    nac+=1
            appear.append(array[i])
            ans = ans + nac*self.basicAlgorithm.get_factorial(length-i)
        
        return ans+1

    def inverse_opreation_of_carton(self, index, length):

        """
        康拓展开逆运算
        :param index: 序号
        :param length: 序列长度
        :return list
        """
        if index < self.basicAlgorithm.get_factorial(length):
            raise Exception("Your index can't small than the length you gave's factorial!")

        index -= 1
        appear = []
        ans = []
        for i in range(0, length):
            now_factorial = self.basicAlgorithm.get_factorial(length-i)
            nac = index / now_factorial
            index -= nac*now_factorial
            
            for j in range(1, length+1):
                if j not in appear:
                    write_in = j
                    if nac == 0:
                        break
                    nac-=1
            appear.append(write_in)
            ans.append(write_in)
        
        a = ans[0]
        ans.remove(ans[0])
        ans.reverse()
        ans.insert(0, a)
        return ans
            


# print(CartonCompute().carton_opreation([6, 5, 4, 3, 2, 1], 6)) # RESULT: Successful
# print(CartonCompute().inverse_opreation_of_carton(24, 6)) # RESULT: Successful