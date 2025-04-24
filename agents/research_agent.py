# research_agent.py
from dotenv import load_dotenv
from tools.tavily_tool import TavilySearch
import os

load_dotenv()

def fetch_data(query):
    tavily = TavilySearch(os.getenv("TAVILY_API_KEY"))
    result = tavily.search(query)
    if result and 'results' in result:
        return result['results']
    return []
