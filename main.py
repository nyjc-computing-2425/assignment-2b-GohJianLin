num = input('Enter a number (decimal only): ')
# type your code here
a = num.strip(" ")
b = num.find(".")
c = num[b+1:]
dp = len(c)
# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
