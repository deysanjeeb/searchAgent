import requests
from bs4 import BeautifulSoup
import urllib.parse
import pandas as pd


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
    user_data = []
    extension = []
    for result in soup.find_all('div', class_='yuRUbf'):
        title = result.find('h3', class_='LC20lb').text if result.find('h3', class_='LC20lb') else "N/A"
        link = result.find('a')['href'] if result.find('a') else "N/A"
        
        if "chromewebstore" in link:
            print(f"Found chromewebstore link: {link}")
            clean_url = link.split('?')[0]
            print(clean_url)
            reviewlink = clean_url + "/reviews"
            print(reviewlink)
            response = requests.get(link, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the div containing the user count
            user_div = soup.find('div', class_='F9iKBc')

            if user_div:
                # Extract the text containing the user count
                user_text = user_div.contents[-1].strip()
                
                # Extract just the number
                user_count = ''.join(filter(str.isdigit, user_text))
                
                print(f"Number of users: {user_count}")
                user_data.append((link, user_count))

            reviews = requests.get(reviewlink, headers=headers)
            soup = BeautifulSoup(reviews.content, 'html.parser')

            # Find all review sections
            review_sections = soup.find_all('section', class_='T7rvce')

            reviews = []

            for section in review_sections:
                review = {}
                
                # Extract reviewer name
                name_span = section.find('span', class_='LfYwpe')
                if name_span:
                    review['name'] = name_span.text.strip()
                
                # Extract rating
                rating_div = section.find('div', class_='B1UG8d')
                if rating_div:
                    review['rating'] = rating_div['aria-label']
                
                # Extract date
                date_span = section.find('span', class_='ydlbEf')
                if date_span:
                    review['date'] = date_span.text.strip()
                
                # Extract review text
                review_p = section.find('p', class_='fzDEpf')
                if review_p:
                    review['text'] = review_p.text.strip()
                
                reviews.append(review)
            extension.append((link,user_count,reviews))
    
    df = pd.DataFrame(extension, columns=['Link', 'Number of Users', 'Reviews'])
    return df


def webstore_search(query, num_results=10):
    # Encode the query for use in the URL
    encoded_query = urllib.parse.quote(query)
    
    # Construct the Google search URL
    url = f"https://chromewebstore.google.com/search/{encoded_query}"
    
    # Send a GET request to Google
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find and extract search results
    search_results = []
    user_data = []
    extension = []
    for result in soup.find_all('div', class_='Cb7Kte'):
        title = result.find('h2', class_='IcZnBc').text if result.find('h2', class_='IcZnBc') else "N/A"
        alink = result.find('a')['href'] if result.find('a') else "N/A"
        print(alink)
        link = 'https://chromewebstore.google.com/' + alink[1:]
        print(link)
        if "detail" in link:
            print(f"Found chromewebstore link: {link}")
            clean_url = link.split('?')[0]
            print(clean_url)
            reviewlink = clean_url + "/reviews"
            print(reviewlink)
            response = requests.get(link, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the div containing the user count
            user_div = soup.find('div', class_='F9iKBc')

            if user_div:
                # Extract the text containing the user count
                user_text = user_div.contents[-1].strip()
                
                # Extract just the number
                user_count = ''.join(filter(str.isdigit, user_text))
                
                print(f"Number of users: {user_count}")
                user_data.append((link, user_count))

            reviews = requests.get(reviewlink, headers=headers)
            soup = BeautifulSoup(reviews.content, 'html.parser')

            # Find all review sections
            review_sections = soup.find_all('section', class_='T7rvce')

            reviews = []

            for section in review_sections:
                review = {}
                
                # Extract reviewer name
                name_span = section.find('span', class_='LfYwpe')
                if name_span:
                    review['name'] = name_span.text.strip()
                
                # Extract rating
                rating_div = section.find('div', class_='B1UG8d')
                if rating_div:
                    review['rating'] = rating_div['aria-label']
                
                # Extract date
                date_span = section.find('span', class_='ydlbEf')
                if date_span:
                    review['date'] = date_span.text.strip()
                
                # Extract review text
                review_p = section.find('p', class_='fzDEpf')
                if review_p:
                    review['text'] = review_p.text.strip()
                
                reviews.append(review)
            extension.append((link,user_count,reviews))
    
    df = pd.DataFrame(extension, columns=['Link', 'Number of Users', 'Reviews'])
    return df
                
def main():
    csv_file = 'ideakeywords.csv'
    df = pd.read_csv(csv_file)
    data_list = df.values.tolist()
    print(data_list)
    # query = input("Enter your search query: ")
    # num_results = int(input("Enter the number of results to display: "))
    for query in df['ideas']:
        print(query)
        gsearch = query + 'chrome extension'
        
        results = webstore_search(query)
        print(results)
        results = google_search(gsearch)
        print(results)

if __name__ == "__main__":
    main()