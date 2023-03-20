import requests
import pandas as pd

url = "https://www.bleepingcomputer.com/news/microsoft/microsoft-march-2023-patch-tuesday-fixes-2-zero-days-83-flaws/"

# Set a user agent to mimic a web browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# Send a GET request with headers
response = requests.get(url, headers=headers)

# Read the table from the HTML response
tables = pd.read_html(response.content, match="Tag")

# Select the table with the desired columns
df = tables[0][["Tag", "CVE ID", "CVE Title", "Severity"]]
df_critical = df[df['Severity'] == 'Critical']

df.to_excel('microsoft tuesday.xlsx', index= False)
df_critical.to_excel('report critical.xlsx', index= False)
