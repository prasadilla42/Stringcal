import re
from typing import List

from src.exception import NegativeErrorException


class Handlers:
    """
    A common utility handler
    """
    def handle_input_string(self,text:str)->List[int]:
        """Parse the string for integer numbers and append that in to a list
           - Raise an exception if the number is negative
           - Not to add number in to the list if the number is more than 1000        
        Args:
            s (str): lines of text entered by the user

        Returns:
            List[int]: list of positive numbers entered by the user
        """
        numbers = self._extract_numbers_from_string(text)        
        non_negative_numbers=[]
        for num in numbers:
            if num <0:                
                raise NegativeErrorException("entered number is negative, poisitive numbers only allowed")
            elif num >= 1000:
                continue
            else:
                non_negative_numbers.append(num)  
        return non_negative_numbers 
            
    
    def _extract_numbers_from_string(self,s:str)->List[int]:
        """
        Find all integers numbers from the text including negative numbers 
        and add them to list
        """    
        pattern = r'-?\d+'
        numbers = re.findall(pattern, s)
        return [int(num) for num in numbers]
