from dash import html, register_page, dcc, callback, Output, Input
import requests

register_page(__name__, path="/page2", name="Page 2")

layout = html.Div([
    html.H2("Page 2", className="page-title"),
    html.P("Click to fetch a random cat fact from a public API", className="page-subtitle"),
    html.Button("Get Cat Fact", id="btn-cat", n_clicks=0),
    dcc.Loading(html.Div(id="cat-fact")) 
], className="page2-wrap")


@callback(
    Output("cat-fact", "children"),
    Input("btn-cat", "n_clicks")
)

def get_cat_fact(n):
    try:
        r = requests.get("https://catfact.ninja/fact", timeout=5)
        r.raise_for_status()
        fact = r.json().get("fact", "no fact found")
        return html.Div(fact)
    except requests.RequestException as e:
        return html.Div(f"Error contacting API: {e}")
        