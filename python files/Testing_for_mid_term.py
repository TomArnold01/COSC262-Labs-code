def almost_all(numbers):
     
     total = sum(numbers)
     result = [total-x for x in numbers]
         
     return result

print(almost_all([1,2,3]))