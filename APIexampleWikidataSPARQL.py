import requests
import pandas as pd

# 10 most populous countries from Wikidata (latest stored population value)
query = """
SELECT ?countryLabel ?population WHERE {
  ?country wdt:P31 wd:Q6256 .              # instance of country
  ?country wdt:P1082 ?population .         # population
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
ORDER BY DESC(?population)
LIMIT 10
"""

endpoint = "https://query.wikidata.org/sparql"
headers = {"User-Agent": "MSBA-class-example/1.0 (youremail@school.edu)"}

resp = requests.get(endpoint, params={"query": query, "format": "json"}, headers=headers)
resp.raise_for_status()
data = resp.json()["results"]["bindings"]

df_api = pd.DataFrame(
    [{"Country": r["countryLabel"]["value"], 
      "Population": int(r["population"]["value"])} for r in data]
)

print(df_api)
