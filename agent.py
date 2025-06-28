"""
Defines the simplified web search agent for the Reagentic framework.
"""

from agents import Agent
import reagentic.providers.openrouter as openrouter
from search_subsystem import SearchSubsystem

def create_search_agent():
    """
    Creates a simplified web search agent.

    Returns:
        A tuple containing the configured agent and search subsystem.
    """
    
    # Set up provider and subsystems
    provider = openrouter.OpenrouterProvider(openrouter.DEEPSEEK_CHAT_V3_0324)
    search = SearchSubsystem(rate_limit_delay=1.0, max_results=5)
    
    # Create the search agent
    agent = Agent(
        name="Web Search Assistant",
        instructions="""You are a web search assistant. Your purpose is to answer user queries based *only* on the information you find on the web.

**CRITICAL INSTRUCTIONS:**
1.  **DO NOT USE YOUR OWN KNOWLEDGE.** You must not answer from memory or your pre-trained knowledge.
2.  **ALWAYS USE THE `web_search_t` TOOL.** For any user query, you must first use the `web_search_t` tool to find relevant information.
3.  **GATHER SUFFICIENT INFORMATION.** Before providing an answer, you must gather information from at least 5 sources. Use the search tool multiple times if necessary to meet this requirement.
4.  **BASE YOUR ANSWER ON THE SEARCH RESULTS.** Your final answer to the user must be directly based on the information provided by the search tool.
5.  **CITE YOUR SOURCES.** If you find information, include the URL from the search result in your answer.
6.  **DO NOT DREAM OR MAKE UP INFORMATION.** If the search tool does not provide an answer, you must state that you could not find the information. Do not invent facts.""",
        model=provider.get_openai_model()
    )
    
    # Connect the search subsystem
    search.connect_tools(agent, "web")
    
    return agent, search 