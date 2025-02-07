def function(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    elif isinstance(a, int) and isinstance(b, str):
        return str(a) + b
    elif isinstance(a, str) and isinstance(b, int):
        return a + str(b)
    else:
        return "Error: Unsupported types"

result = function(5, '10')
print(result)
result = function(5,10)
print(result) 
result = function('5','10')
print(result) 