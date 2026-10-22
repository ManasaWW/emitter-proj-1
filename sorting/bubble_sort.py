from typing import List, Any
from utils.logger import get_logger

logger = get_logger(__name__)

def bubble_sort(arr: List[Any]) -> List[Any]:
    """
    Sorts a list using the bubble sort algorithm.
    :param arr: List of comparable elements
    :return: Sorted list
    """
    logger.info(f"Starting bubble sort for array of length {len(arr) if isinstance(arr, list) else 'UNKNOWN'}")
    
    try:
        if not isinstance(arr, list):
            raise TypeError("Input must be a list.")
            
        # Create a copy to avoid mutating the original list
        sorted_arr = arr.copy()
        n = len(sorted_arr)
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                # Type checking to ensure elements are comparable
                if type(sorted_arr[j]) != type(sorted_arr[j+1]):
                    logger.warning(f"Comparing different types: {type(sorted_arr[j])} and {type(sorted_arr[j+1])}")
                    
                if sorted_arr[j] > sorted_arr[j + 1]:
                    sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                    swapped = True
            if not swapped:
                break
                
        logger.debug("Successfully completed bubble sort.")
        return sorted_arr
        
    except TypeError as te:
        logger.error(f"Type error during bubble sort (likely non-comparable elements): {str(te)}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during bubble sort: {str(e)}")
        raise
