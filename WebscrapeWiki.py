import pandas as pd
import requests

# Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

# Fetch the page with requests (adds headers automatically)
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
response.raise_for_status()  # will throw an error if request fails

# Parse all tables from the HTML
tables = pd.read_html(response.text)

# Heuristic: pick the table with Location + Population
candidate = None
for t in tables:
    cols = [c.lower() for c in t.columns.astype(str)]
    if any("location" in c for c in cols) and any("population" in c for c in cols):
        candidate = t
        break

if candidate is None:
    raise ValueError("Could not find a suitable table on the page.")

# Normalize column names
col_map = {}
for c in candidate.columns:
    cl = str(c).lower()
    if "location" in cl:
        col_map[c] = "Location"
    elif "population" in cl:
        col_map[c] = "Population"

df_scrape = candidate.rename(columns=col_map)[["Location", "Population"]].copy()

# Clean Population
df_scrape["Population"] = (
    df_scrape["Population"]
    .astype(str)
    .str.replace(r"\[.*?\]", "", regex=True)   # remove footnotes
    .str.replace(",", "", regex=False)         # remove commas
    .str.extract(r"(\d+)", expand=False)       # extract digits
    .astype("Int64")
)

# Top 10 countries
df_scrape = (
    df_scrape.dropna(subset=["Population"])
             .sort_values("Population", ascending=False)
             .head(10)
             .reset_index(drop=True)
)

print(df_scrape)
