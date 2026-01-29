# Dataset Scraping and Confirmation Testing

A Python-based tool for scraping and analyzing podcast transcript data from Supabase backend services.

## 📋 Overview

This project provides utilities to fetch, store, and analyze podcast transcripts from a remote API endpoint. It includes functionality for making authenticated API requests and parsing the resulting JSON data to extract episode information.

## 🚀 Features

- **API Integration**: Connects to Supabase Functions to fetch transcript data
- **Authentication**: Handles API key-based authentication with proper headers
- **Data Persistence**: Saves fetched data to JSON files for offline analysis
- **Data Analysis**: Parses and analyzes the structure of transcript datasets
- **Pagination Support**: Capable of handling paginated API responses
- **Large File Handling**: Efficiently processes large JSON responses using streaming

## 📁 Project Structure

```
Dataset-Scraping-And-Confirmation-Testing/
├── test.py                              # Main script for fetching and analyzing transcripts
├── fetch_transcripts_response.json      # Cached API response data (~26MB)
├── .gitattributes                       # Git configuration
└── README.md                            # This file
```

## 🛠️ Requirements

- Python 3.7+
- `requests` library (for API calls)

## 📦 Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd Dataset-Scraping-And-Confirmation-Testing
```

2. Install required dependencies:
```bash
pip install requests
```

## 💻 Usage

### Fetching Transcripts

The script includes functionality to fetch transcripts from the API (currently commented out):

```python
import requests

URL = "https://bcvtinztsqcolilikksy.supabase.co/functions/v1/fetch-transcripts"
APIKEY = "your-api-key-here"

headers = {
    "accept": "*/*",
    "content-type": "application/json",
    "apikey": APIKEY,
    "authorization": f"Bearer {APIKEY}",
}

payload = {"page": 1}
r = requests.post(URL, headers=headers, json=payload, stream=True, timeout=120)
```

### Analyzing Data

Run the script to analyze the cached transcript data:

```bash
python test.py
```

The script will output:
- Data type (list or dict)
- Number of episodes in the response
- Total available episodes
- Number of unique slugs

### Sample Output

```
<class 'dict'>
episodes in this response: 150
totalAvailable: 500
slugs: 150
```

## 📊 Data Structure

The fetched JSON data contains:
- **episodes**: Array of episode objects with transcript information
- **totalAvailable**: Total number of episodes available in the database
- **slugs**: Array of unique episode identifiers

## 🔐 Security Notes

- **API Keys**: The current implementation includes API keys in the code. For production use, store credentials in environment variables or a secure configuration file.
- **Authentication**: Uses Bearer token authentication with Supabase API keys
- **CORS Headers**: Includes proper origin and referer headers for API compatibility

## 🔧 Configuration

### API Endpoint
```
https://bcvtinztsqcolilikksy.supabase.co/functions/v1/fetch-transcripts
```

### Headers Required
- `apikey`: Your Supabase anonymous key
- `authorization`: Bearer token (same as apikey)
- `content-type`: application/json
- `origin`: https://lennyshub.lovable.app
- `referer`: https://lennyshub.lovable.app/

### Request Payload
```json
{
  "page": 1
}
```

## 📝 Development Notes

- The script uses streaming to handle large responses efficiently
- Timeout is set to 120 seconds for API requests
- Response is saved in chunks of 1MB to manage memory usage
- Error handling includes status code checking and partial error message display

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is provided as-is for educational and research purposes.

## ⚠️ Disclaimer

This tool is designed for legitimate data collection and analysis purposes. Ensure you have proper authorization to access and scrape data from the target API. Respect rate limits and terms of service of the API provider.

## 🐛 Troubleshooting

### Common Issues

**Issue**: `requests.exceptions.Timeout`
- **Solution**: Increase the timeout value or check your internet connection

**Issue**: `401 Unauthorized`
- **Solution**: Verify your API key is valid and not expired

**Issue**: `JSONDecodeError`
- **Solution**: Check if the response is valid JSON; the API might be returning an error message

## 📧 Contact

For questions or support, please open an issue in the repository.

---

**Last Updated**: January 2026
