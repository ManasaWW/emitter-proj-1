from typing import List
import re
from utils.logger import get_logger

logger = get_logger(__name__)

def search_keyword(paragraph: str, keyword: str, case_sensitive: bool = False) -> List[int]:
    """
    Searches for a keyword in a paragraph and returns its starting indices.
    :param paragraph: The text to search in
    :param keyword: The word to search for
    :param case_sensitive: Whether the search should be case sensitive
    :return: List of starting indices where the keyword is found
    """
    logger.info(f"Searching for keyword '{keyword}' (case_sensitive={case_sensitive})")
    
    try:
        if not isinstance(paragraph, str) or not isinstance(keyword, str):
            raise TypeError("Both paragraph and keyword must be strings.")
        if not keyword:
            raise ValueError("Keyword cannot be empty.")
            
        flags = 0 if case_sensitive else re.IGNORECASE
        
        # Use regex to find whole words only, or adjust pattern as needed.
        # Here we just find all occurrences of the substring.
        pattern = re.escape(keyword)
        matches = [m.start() for m in re.finditer(pattern, paragraph, flags)]
        
        logger.debug(f"Found {len(matches)} occurrences of '{keyword}'.")
        return matches
        
    except Exception as e:
        logger.error(f"Error searching for keyword: {str(e)}")
        raise
