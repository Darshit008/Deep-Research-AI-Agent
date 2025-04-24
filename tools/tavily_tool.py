import requests
import json

class TavilySearch:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.tavily.com/search"

    def search(self, query):
        # Construct the request payload
        payload = {
            "query": query,
            "topic": "general",  # You can adjust this to "news" if needed
            "search_depth": "basic",  # or "advanced" if you need more detailed results
            "chunks_per_source": 3,
            "max_results": 5,
            "time_range": None,
            "days": 7,  # Set as per your requirements (1 to 7 days)
            "include_answer": True,
            "include_raw_content": False,
            "include_images": False,
            "include_image_descriptions": False,
            "include_domains": [],
            "exclude_domains": []
        }

        # Set up the authorization header with the API key
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Make the POST request
        response = requests.post(self.base_url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()  # Parse and return the JSON response
        else:
            print("Error:", response.status_code)
            return None

# Example usage
if __name__ == "__main__":
    api_key = "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"  # Use your correct Tavily API key
    tavily = TavilySearch(api_key)
    
    query = "latest AI trends 2025"
    result = tavily.search(query)
    
    if result:
        print("Search Results:")
        print(json.dumps(result, indent=4))  # Pretty-print the JSON result
