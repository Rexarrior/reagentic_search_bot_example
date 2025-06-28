"""
Runs the simplified search agent in interactive mode.
"""
from agents import Runner
from agent import create_search_agent

def interactive_mode():
    """Run the search agent in an interactive loop."""
    print("=== Interactive Web Search Mode ===\n")
    
    agent, _ = create_search_agent()
    print("Web search assistant is ready.")
    print("Type your query, or 'exit' to quit.\n")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting interactive mode. Goodbye!")
                break

            if not user_input.strip():
                continue
            
            print("\nThinking...")
            result = Runner.run_sync(agent, user_input)
            
            print("\nAssistant:")
            print(result.final_output)
            print("-" * 50)

        except KeyboardInterrupt:
            print("\nExiting interactive mode. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    interactive_mode() 