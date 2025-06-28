"""
A simplified Search Subsystem for the Reagentic framework.
"""
import time
from typing import List
from duckduckgo_search import DDGS

from reagentic.subsystems.subsystem_base import SubsystemBase

class SearchSubsystem(SubsystemBase):
    """
    A simplified search subsystem that provides a single web search capability.
    """
    
    def __init__(self, rate_limit_delay: float = 1.0, max_results: int = 5):
        """
        Initialize the search subsystem.
        
        Args:
            rate_limit_delay: Delay between searches to respect rate limits.
            max_results: Maximum number of results to return per search.
        """
        super().__init__()
        self.rate_limit_delay = rate_limit_delay
        self.max_results = max_results
        self.last_search_time = 0
        
        try:
            self.ddgs = DDGS()
        except Exception as e:
            print(f"Warning: Could not initialize DuckDuckGo search: {e}")
            self.ddgs = None
    
    def _rate_limit(self):
        """Implement rate limiting to respect search APIs."""
        current_time = time.time()
        time_since_last = current_time - self.last_search_time
        if time_since_last < self.rate_limit_delay:
            time.sleep(self.rate_limit_delay - time_since_last)
        self.last_search_time = time.time()
    
    def _safe_search(self, search_func, *args, **kwargs) -> List:
        """Safely execute a search function with error handling."""
        try:
            self._rate_limit()
            # The DDGS functions return generators, so we convert to a list
            results = list(search_func(*args, **kwargs))
            return results[:self.max_results]
        except Exception as e:
            print(f"Search error: {e}")
            return []
    
    @SubsystemBase.subsystem_tool("web")
    def web_search_t(self, query: str) -> str:
        """
        Perform a general web search using DuckDuckGo. 
        Use this tool to find information on the internet.

        Args:
            query: The search query.
            
        Returns:
            A formatted string of search results, or an error message.
        """
        if not self.ddgs:
            return "Error: Search service not available"
        
        results = self._safe_search(self.ddgs.text, query)
        
        if not results:
            return f"No results found for: {query}"
        
        formatted_results = []
        for i, result in enumerate(results, 1):
            formatted_results.append(
                f"{i}. {result.get('title', 'No title')}\n"
                f"   URL: {result.get('href', 'No link')}\n"
                f"   Snippet: {result.get('body', 'No description')[:250]}...\n"
            )
        
        return f"Web search results for '{query}':\n\n" + "\n".join(formatted_results) 