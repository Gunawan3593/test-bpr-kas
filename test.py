# Answer Number 1

def sum2Nums(nums, target):
    find = {}
    for i, num in enumerate(nums):
        if target - num in find:
            return [find[target - num], i]
        find[num] = i
    return []
    
nums = [2, 7, 11, 15, 3]
target = 26

result = sum2Nums(nums, target)
print(result)

# Answer Number 2

def romanToInt(s: str) -> int:
    romanNumerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    for i in range(len(s)):
        currentNumeral = s[i]
        currentValue = romanNumerals[currentNumeral]
        if i == len(s) - 1 or romanNumerals[s[i+1]] <= currentValue:
            result += currentValue
        else:
            result -= currentValue
    
    return result

input = "MDCCLXXVI"
result = romanToInt(input)
print(result)
