from pytrends.request import TrendReq
import pandas as pd
import os
from datetime import datetime

# Step 1: Output folder
output_dir = "data/processed"
os.makedirs(output_dir, exist_ok=True)

# Step 2: Use broad, high-volume keywords
keywords = ["weather", "cricket", "stock market", "India news", "technology"]

# Step 3: Start pytrends
pytrends = TrendReq(hl='en-US', tz=330)
pytrends.build_payload(keywords, cat=0, timeframe='now 7-d', geo='IN')

# Step 4: Get interest over time
data = pytrends.interest_over_time()

# Step 5: Check and clean
if data.empty:
    print("⚠️ No data fetched. Try different keywords or check your internet.")
else:
    if 'isPartial' in data.columns:
        data = data.drop(columns=['isPartial'])

    # Step 6: Save CSV
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M')
    filename = f"{output_dir}/trends_{timestamp}.csv"
    data.to_csv(filename)
    print(f"✅ Trends data saved to: {filename}")
    print(data.head())
