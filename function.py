
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
    return n*fac(n-1)
  
  
print(fac(2))
  
  
  