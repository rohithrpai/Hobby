###############################################################################
#                           Keith Number Generator                            #
#                              - Rohith Pai                                   #
#                                                                             #
###############################################################################
# Based on the user of the N th number the code will perform iteration and    #
# separate the Keith number between 1 and N.                                  #
###############################################################################
import pandas as pd
import numpy as np
import time

t = time.time()
#-------------------Keith's number Generator function--------------------------#
def keith_num (num):
    length = len(num)
    if(length==1):
        return (None, None)
    original_num = int(num)
    number = [int(k) for k in [j for j in num]]
    iteration = 0
    summation  = 0
    while (summation<original_num):
        iteration += 1
        summation = sum(number)
        for j in range(0,length):
            if(j != length-1):
                number[j] = number[j+1]
            elif(j == length-1):
                number[j] = summation
    if(summation>original_num):
        return (None, None)
    else:
        return (original_num,iteration)

#------------------------------Main Function-----------------------------------#
def main():
    print('The code will search and list all the Keith numbers between 1-N')
    print('_______________________________________________________________')

    num_range = int(input('Enter the Value of N:'))
    keith_nums = []

    for j in range(1,num_range+1):
        keith_nums.append(keith_num(str(j)))
    keith_nums = pd.DataFrame(keith_nums,columns=['KeithNumbers','Summation_steps'])
    keith_nums.dropna(how ='all',inplace = True)
    keith_nums.to_csv('KeithNumber.csv',index = False)
    elapsedtime = time.time() -t

    print('\n')
    print("Done recording!")
    print('Elapsed time: %.2f secs.'%elapsedtime)

if __name__ == '__main__':
    main()
