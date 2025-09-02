import datetime as dt
import requests
from dash import Dash, html, dcc, Input, Output, exceptions

API_KEY = "DEMO_KEY"          # Replace with your own if you have one
APOD_URL = "https://api.nasa.gov/planetary/apod"
MIN_DATE = dt.date(1995, 6, 16)
TODAY = dt.date.today()

app = Dash(__name__)
app.title = "NASA APOD"

app.layout = html.Div(
    style={"margin": "0 auto", "padding":20},
    children=[
        html.H1("NASA Astronomy Picture of the Day"),
        dcc.DatePickerSingle(
            id="apod-date",
            min_date_allowed=MIN_DATE,
            max_date_allowed=TODAY,
            date=TODAY,
            display_format="YYYY-MM-DD",
            clearable=False,
        ),
        dcc.Loading(html.Div(id="media", style={"marginTop": 16, 
                                                "textAlign": "center"})),
        html.Div(id="caption"),
    ],
)

@app.callback(
    [Output("media", "children"), Output("caption", "children")],
    Input("apod-date", "date"),
)
def show_apod(date_str):
    if not date_str:
        raise exceptions.PreventUpdate

    try:
        date_obj = dt.date.fromisoformat(date_str[:10])
    except Exception:
        return "Invalid date.", ""

    params = {"api_key": API_KEY, "date": date_obj.isoformat()}
    try:
        r = requests.get(APOD_URL, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
    except requests.RequestException as e:
        return f"API error: {e}", ""

    media_type = data.get("media_type", "")
    url = data.get("url", "")
    title = data.get("title", "APOD")
    explanation = data.get("explanation", "")

    if media_type == "image":
        media = html.Img(src=url, style={"maxWidth": "100%", "borderRadius": 8}, alt=title)
    elif media_type == "video":
        media = html.Iframe(src=url, style={"width": "100%", "height": 500, "border": 0})
    else:
        media = html.Div("Unsupported media type.")

    header = html.H3(f"{title} — {date_obj.isoformat()}", style={"marginBottom": 8})
    return html.Div([header, media]), explanation

if __name__ == "__main__":
    app.run(debug=True)
