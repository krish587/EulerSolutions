import sys

def sum_multiples_numbers(number1,number2,max_range):
    sum = 0
    for i in range(0,max_range):
        if i%number1==0 or i%number2==0:
            sum = sum + i
    return sum


if __name__=="__main__":
    sum3_5 = sum_multiples_numbers(3,5,1000)
    
    print "multiples of 3 and 5 sum %s" %(sum3_5)
    
    
