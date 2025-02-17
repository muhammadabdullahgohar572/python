
# def Passs(**Known):
 
#     for key,value in Known.items():
#        print (f'This is a Key {key} and This is a Data {value}');

# Passs(name="Abdullah",age=18,city="pakistan")     


# def GenrateNumber(limit):
#     for i in range(2,limit+1,2):
#         yield i

# for num in GenrateNumber(10):
#   print(num)      
  
  
def fac(n):
    if n == 0 or n == 1:  # Base case to stop recursion
        return 1
    return n * fac(n - 1)

print(fac(2))  # Output: 2
print(fac(5))  # Output: 120
