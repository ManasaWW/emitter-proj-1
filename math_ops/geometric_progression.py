from typing import List, Union
from utils.logger import get_logger

logger = get_logger(__name__)

def generate_geometric_progression(a: Union[int, float], r: Union[int, float], n: int) -> List[Union[int, float]]:
    """
    Generates a geometric progression.
    :param a: Initial term
    :param r: Common ratio
    :param n: Number of terms
    :return: List containing the geometric progression
    """
    logger.info(f"Generating geometric progression with a={a}, r={r}, n={n}")
    
    try:
        if not isinstance(n, int) or n <= 0:
            raise ValueError("Number of terms (n) must be a positive integer.")
        if not isinstance(a, (int, float)) or not isinstance(r, (int, float)):
            raise TypeError("Initial term (a) and common ratio (r) must be numbers.")
            
        progression = [a * (r ** i) for i in range(n)]
        logger.debug(f"Successfully generated progression: {progression}")
        return progression
        
    except Exception as e:
        logger.error(f"Error generating geometric progression: {str(e)}")
        raise
