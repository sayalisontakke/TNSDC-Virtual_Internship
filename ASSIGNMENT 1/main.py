class Solution(object):
  def romanToInt(self):
    """
    :rtype: int
    """
    lookup = {
      'M': 1000, 
      'CM': 900, 
      'D': 500, 
      'CD': 400, 
      'C': 100, 
      'XC': 90, 
      'L': 50, 
      'XL': 40, 
      'X': 10, 
      'IX': 9, 
      'V': 5, 
      'IV': 4, 
      'I': 1
    }
    roman = input("Enter a Roman numeral: ").upper()
    num = 0

    for i in range(len(roman)):
      if i > 0 and lookup[roman[i]] > lookup[roman[i-1]]:
        num += lookup[roman[i]] - 2 * lookup[roman[i-1]]
      else:
        num += lookup[roman[i]]
    return num

# Example usage:
solution = Solution()
result = solution.romanToInt()
print(result)

Output : class Solution(object):
  def romanToInt(self):
    """
    :rtype: int
    """
    lookup = {
      'M': 1000, 
      'CM': 900, 
      'D': 500, 
      'CD': 400, 
      'C': 100, 
      'XC': 90, 
      'L': 50, 
      'XL': 40, 
      'X': 10, 
      'IX': 9, 
      'V': 5, 
      'IV': 4, 
      'I': 1
    }
    roman = input("Enter a Roman numeral: ").upper()
    num = 0

    for i in range(len(roman)):
      if i > 0 and lookup[roman[i]] > lookup[roman[i-1]]:
        num += lookup[roman[i]] - 2 * lookup[roman[i-1]]
      else:
        num += lookup[roman[i]]
    return num

# Example usage:
solution = Solution()
result = solution.romanToInt()
print(result)
