"""
Runs the search agent in debug mode with predefined requests.
"""
from agents import Runner
from agent import create_search_agent

def debug_mode():
    """Run a series of predefined search queries for debugging."""
    print("=== Debug Web Search Mode ===\n")
    
    agent, _ = create_search_agent()
    print("Web search assistant created for debugging.\n")
    
    predefined_queries = [
        "What is the Reagentic framework?",
        "Who is the current CEO of OpenAI?",
        "What were the main announcements at the last Apple event?",
        "xyz123nonexistenttopic" # A query that should yield no results
    ]

    for i, query in enumerate(predefined_queries):
        print(f"--- Query {i+1}: '{query}' ---")
        print("Thinking...")
        
        result = Runner.run_sync(agent, query)
        
        print("\nAssistant:")
        print(result.final_output)
        print("-" * 50 + "\n")
    
    print("\n=== Debug Search Mode Complete ===")

if __name__ == "__main__":
    debug_mode() 