# Chrome Extension Analyzer

## Overview

Chrome Extension Analyzer is a Python-based tool designed to gather and analyze data about Chrome extensions. It combines web scraping techniques to collect information from both the Chrome Web Store and Google search results, providing insights into extension popularity, user reviews, and more.

## Features

- Search for Chrome extensions using keywords
- Scrape extension data from the Chrome Web Store
- Collect additional information from Google search results
- Extract user counts and reviews for each extension
- Export results to CSV files for further analysis

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- Chrome WebDriver (for Selenium)
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/chrome-extension-analyzer.git
   cd chrome-extension-analyzer
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Download and install the Chrome WebDriver that matches your Chrome browser version.

## Usage

1. Prepare your input file:
   - Create a CSV file named `ideakeywords.csv` with a column named 'ideas' containing your search queries.

2. Run the main script:
   ```
   python main.py
   ```

3. The script will process each query in the CSV file and generate separate CSV files for each query, containing the combined results from the Chrome Web Store and Google searches.

## Output

For each query, the script generates a CSV file named `{query}.csv` containing the following information:
- Link to the Chrome extension
- Number of users
- User reviews (including reviewer name, rating, date, and review text)

## Note

This script uses web scraping techniques and may be affected by changes to the Chrome Web Store or Google search results pages. Always ensure you comply with the terms of service of the websites you're scraping.

## Contributing

Contributions to the Chrome Extension Analyzer are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
