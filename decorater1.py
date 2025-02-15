
def dedug(func):
    def wrapper(*args,**kwargs):
        args_value=", ".join(str(arg) for arg in args)
        getData=", ".join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling:{func.__name__} and key is {args_value} and value is {getData}")
        return func(*args, **kwargs)  # Correct way to call function
    return wrapper  # Return corrected wrapper function
    
@dedug        
    
def name(**kwargs):
    for kay,value in kwargs.items():
      print(  f"This is a key {kay} and value is {value}")
@dedug        
def testt():
     print("Hello")
     
     
testt()        
name(name="Abdullah",age=18)
    