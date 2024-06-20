def all_odds(numbers):
    if len(numbers) == 0:
        return True
    else:
        return numbers[0] % 2 != 0 and all_odds(numbers[1:])
    
print(all_odds([3, 6, -7, 79]))

print(all_odds([]))