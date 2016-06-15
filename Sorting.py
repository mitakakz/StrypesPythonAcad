from copy import deepcopy
import time

class SlowSorts :

    @staticmethod
    def bubble_sort( list ):
        sorted_list = deepcopy(list)
        do_sort = True
        while do_sort == True:
            do_sort = False
            for i in range(1,len(sorted_list)):
                if sorted_list[i-1] > sorted_list[i]:
                    sorted_list[i-1],sorted_list[i] = sorted_list[i],sorted_list[i-1]
                    do_sort = True
        return sorted_list

    @staticmethod
    def selection_sort(items):
        list = deepcopy(items)

        new_list = []
        for el in range(0, len(list)):
            tmp = list[0]
            for i in range(1,len(list)):
                if tmp > list[i]:
                    tmp = list[i]
            new_list.append(tmp)
            list.remove(tmp)
        return new_list

class FastSort :

    @staticmethod
    def bin_search( list, elem ):
        left = 0
        right = len(list)

        def middle_calc():
            return  (left + right) // 2

        middle = middle_calc()

        while left<right:
            print ("L:{}, R:{}, M:{}".format(left,right,middle))
            if list[middle] > elem:
                right = middle-1
                middle = middle_calc()

            elif list[middle] <elem:
                left = middle+1
                middle = middle_calc()

            elif list[middle] == elem:
                return True

        return False

    @staticmethod
    def quick_sort(list):

        if len(list) <= 1:
            return list
        pivot = list[0]
        smaller = [x for x in list if x < pivot]
        greater =[x for x in list if x > pivot]
        pivots = [x for x in list if x == pivot]
        return FastSort.quick_sort(smaller) + pivots + FastSort.quick_sort(greater)

    @staticmethod
    def Counting_sort(list, upper_limits=None):

        result = []
        if upper_limits == None:
            upper_limits = max(list)
        counts = [0 for x in range(0,upper_limits+1)]
        index = 0

        for elem in list:
            counts[elem] += 1
        for sort_n in counts:
            for s_elem in range(0,sort_n):
                result.append(index)
            index += 1
        print(result)



'''
l = [5,0,-8,42,100]
start_time = time.time()
print(SlowSorts.bubble_sort(l))
print ("Bubble_sort finished for : ", time.time()-start_time)
print (l)
start_time = time.time()
print(SlowSorts.selection_sort(l))
print ("Selection_sort finished for : ", time.time()-start_time)
print (l)

print(FastSort.bin_search([1,2,3,4,5,6,7,8,9,10],11))
#print(FastSort.bin_search([1,2,3,4,5],8))
'''
#print (FastSort.quick_sort([1,3,5,87,42,43,6,-23]))
FastSort.Counting_sort([1,3,5,87,42,43,6])