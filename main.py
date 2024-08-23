import requests
from bs4 import BeautifulSoup
import urllib.parse

def google_search(query, num_results=10):
    # Encode the query for use in the URL
    encoded_query = urllib.parse.quote(query)
    
    # Construct the Google search URL
    url = f"https://www.google.com/search?q={encoded_query}&num={num_results}"
    
    # Send a GET request to Google
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find and extract search results
    search_results = []
    for result in soup.find_all('div', class_='yuRUbf'):
        title = result.find('h3', class_='LC20lb').text if result.find('h3', class_='LC20lb') else "N/A"
        link = result.find('a')['href'] if result.find('a') else "N/A"
        search_results.append((title, link))
    
    return search_results

def main():
    query = input("Enter your search query: ")
    num_results = int(input("Enter the number of results to display: "))
    
    results = google_search(query, num_results)
    
    print(f"\nTop {num_results} results for '{query}':\n")
    for i, (title, link) in enumerate(results, 1):
        print(f"{i}. {title}")
        print(f"   {link}\n")

if __name__ == "__main__":
    main()