# MultiLayoutWeather.py
import requests
import pandas as pd #for data frame and manipulation
from datetime import datetime #for date and time manipulation
from dash import Dash, html, dcc, Input, Output 
import dash_bootstrap_components as dbc #for bootstrap components
import plotly.express as px #for data visualization


# ---------- Public API helper (Open-Meteo) ----------
#selecting the cities and their coordinates
# This is a dictionary mapping city names to their latitude and longitude.
CITY_COORDS = {
    "Williamsburg": (37.2707, -76.7075),
    "Richmond": (37.5407, -77.4360),
    "Virginia Beach": (36.8529, -75.9780),
    "Roanoke": (37.27097, -79.94143),
    "Charlottesville": (38.0293, -78.4767)
}

def fetch_hourly_temp(lat: float, lon: float) -> pd.DataFrame:
    """Fetch next-48-hours hourly temperature."""
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&hourly=temperature_2m&forecast_days=2&timezone=auto"
    )
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    data = r.json()["hourly"]
    df = pd.DataFrame({"time": data["time"], "temp_C": data["temperature_2m"]})
    df["time"] = pd.to_datetime(df["time"])
    return df

# ---------- Dash App ----------
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Open-Meteo Dashboard"

# Top bar
navbar = html.Div(
    [
        html.H3("Open-Meteo Dashboard", className="text-white"),
        html.Span("Public API - Multi-column layout", className="text-white"),
    ],
    className="navbar navbar-dark bg-dark mb-4 px-3"
)


# Controls (left column) — pure html + Bootstrap classes
controls = html.Div(
    [
        html.Div("Controls", className="card-header"),

        html.Div(
            [
                html.Label("City", className="form-label"),
                dcc.Dropdown(
                    id="city-dd",
                    options=[{"label": k, "value": k} for k in CITY_COORDS.keys()],
                    value="Williamsburg",
                    clearable=False,
                ),

                html.Div(className="my-3"),  # spacing

                html.Button("Refresh", id="refresh", n_clicks=0,
                            className="btn btn-primary w-100"),

                html.Hr(className="my-3"),

                html.Small(
                    "Data source: open-meteo.com (no API key required).",
                    className="text-muted",
                ),
            ],
            className="card-body",
        ),
    ],
    className="card mb-3",
)

# Controls (left column)
controls = dbc.Card([
        dbc.CardHeader("Controls"),
        dbc.CardBody(
            [
                dbc.Label("City"),
                dcc.Dropdown(
                    id="city-dd",
                    options=[{"label": k, "value": k} for k in CITY_COORDS.keys()],
                    value="Williamsburg",
                    clearable=False,
                ),
                html.Br(),
                dbc.Button("Refresh", id="refresh", n_clicks=0, className="w-100"),
                html.Hr(),
                html.Small(
                    "Data source: open-meteo.com (no API key required).",
                    className="text-muted",
                ),
            ]
        ),
    ],className="mb-3",)

# KPI cards (top row center/right)
def kpi_card(title, id_):
    return dbc.Card(
        dbc.CardBody(
            [
                html.H6(title, className="text-muted mb-1"),
                html.H3(id=id_, className="mb-0"),
            ]
        ),
        className="h-100",
    )

kpi_row = dbc.Row(
    [
        dbc.Col(kpi_card("Current Temp (°C)", "kpi-now"), md=4),
        dbc.Col(kpi_card("Min (°C/48h)", "kpi-min"), md=4),
        dbc.Col(kpi_card("Max (°C/48h)", "kpi-max"), md=4),
    ],
    className="g-3 mb-3",
)

# Chart (middle column)
chart_card = dbc.Card(
    [
        dbc.CardHeader("Hourly Temperature (next 48h)"),
        dbc.CardBody(dcc.Graph(id="temp-chart", config={"displayModeBar": False})),
    ]
)

# Stats table (right column)
table_card = dbc.Card(
    [
        dbc.CardHeader("Summary Stats"),
        dbc.CardBody(html.Div(id="stats-table")),
    ]
)

# ---------- Layout: Multi-column grid ----------
app.layout = dbc.Container(
    [
        navbar,
        dbc.Row(
            [
                # Left: controls (md=3)
                dbc.Col(controls, md=3),
                # Middle: KPIs + chart (md=6)
                dbc.Col([kpi_row, chart_card], md=6),
                # Right: stats table (md=3)
                dbc.Col(table_card, md=3),
            ],
            className="g-3",
        ),
        html.Footer(
            html.Small(
                "Built with Dash + dash-bootstrap-components • Layout uses Row/Col grid",
                className="text-muted",
            ),
            className="mt-4",
        ),
    ],
    fluid=True,
)

# ---------- Callbacks ----------
@app.callback(
    [
        Output("temp-chart", "figure"),
        Output("kpi-now", "children"),
        Output("kpi-min", "children"),
        Output("kpi-max", "children"),
        Output("stats-table", "children"),
    ],
    [Input("city-dd", "value"), Input("refresh", "n_clicks")],
)
def update(city, _):
    lat, lon = CITY_COORDS[city]
    df = fetch_hourly_temp(lat, lon)

    # KPIs
    now = df.iloc[0]["temp_C"]
    tmin = df["temp_C"].min()
    tmax = df["temp_C"].max()

    # Chart
    fig = px.line(df, x="time", y="temp_C", markers=True, title=None)
    fig.update_layout(margin=dict(l=10, r=10, t=10, b=10), yaxis_title="°C", xaxis_title="Time")

    # Stats table
    summary = (
        df.assign(Date=df["time"].dt.date)
        .groupby("Date")["temp_C"]
        .agg(["min", "max", "mean"])
        .round(1)
        .rename(columns={"min": "Min °C", "max": "Max °C", "mean": "Avg °C"})
        .reset_index()
    )
    table = dbc.Table.from_dataframe(summary, striped=True, bordered=False, hover=True)

    fmt = lambda x: f"{x:.1f}"
    return fig, fmt(now), fmt(tmin), fmt(tmax), table


if __name__ == "__main__":
    app.run(debug=True)
