import requests
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_stock_headlines(stock_symbol):
  """Fetches top headlines for a given stock using the NewsAPI."""

  api_key = "c52e1788bde5439382b60c6d0e3dd9d9"  # Replace with your NewsAPI key
  url = f"https://newsapi.org/v2/everything?q={stock_symbol}&apiKey={api_key}"

  response = requests.get(url)
  data = response.json()

  headlines = [article["title"] for article in data["articles"]]
  return headlines


# Example usage:
while True:
    stock_symbol = input('enter a ticker: ')
    headlines = get_stock_headlines(stock_symbol)

    for headline in headlines:
        print(headline)

    # Download necessary NLTK data
    nltk.download('vader_lexicon')

    # Create a SentimentIntensityAnalyzer object
    sia = SentimentIntensityAnalyzer()

    # Initialize sentiment scores
    total_positive = 0
    total_negative = 0
    total_neutral = 0
    total_compound = 0

    # Analyze sentiment for each headline and accumulate scores
    for headline in headlines:
        sentiment = sia.polarity_scores(headline)
        total_positive += sentiment['pos']
        total_negative += sentiment['neg']
        total_neutral += sentiment['neu']
        total_compound += sentiment['compound']

    # Calculate   average sentiment scores
    average_positive = total_positive / len(headlines)
    average_negative = total_negative / len(headlines)
    average_neutral = total_neutral / len(headlines)
    average_compound = total_compound / len(headlines)

    # Print overall sentiment
    print("Overall Sentiment:")
    print("Positive:", average_positive)
    print("Negative:", average_negative)
    print("Neutral:", average_neutral)
    print("Compound:", average_compound)