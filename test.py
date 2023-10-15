import unittest

def roman_numerals_to_int(roman_numeral):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 
    result = 0 
    prev_value = None 
    
    for i in roman_numeral.upper(): 
        if i in roman_dict: 
            curr_value = roman_dict[i] 
            if prev_value != None and prev_value < curr_value: 
                result += curr_value - 2 * prev_value 
            else:
                result += curr_value 

            prev_value = curr_value 
        else:
            return None 
        
    return result


class Test(unittest.TestCase):

   def test_1(self):
       res = roman_numerals_to_int("xiv")
       self.assertEqual(res, 14)

   def test_2(self):
       res = roman_numerals_to_int("MMXXIII")
       self.assertEqual(res, 2023)

   def test_3(self):
       res = roman_numerals_to_int("xivj")
       self.assertEqual(res, None)

if __name__ == '__main__': 
    unittest.main() 