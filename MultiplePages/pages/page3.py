from dash import html, dcc, Input, Output, callback, register_page
import pandas as pd
import plotly.express as px
from pathlib import Path

register_page(__name__, path="/page3", name="Electricity")

DataPath = Path(__file__).resolve().parent.parent / "data" / "electricity_prices.csv"
raw = pd.read_csv(DataPath)

# Keep just residential and compute ANNUAL mean price per state
df = (
    raw.loc[raw["sectorName"].eq("residential"), ["year", "state", "price"]]
       .groupby(["year", "state"], as_index=False)["price"].mean()
)

# Pulling out slider bounds into variables
YEAR_MIN = int(df["year"].min())
YEAR_MAX = int(df["year"].max())

# Lock in color scale across all years (in cents/kWh)
V_MIN = float(df["price"].min())
V_MAX = float(df["price"].max())

layout = html.Div(
    style={"backgroundColor": "#293831", "padding": "20px"},
    children=[
        html.H1("Electricity Prices by US State (Residential, cents/kWh)",
                style={"color": "#CDD6D3", "textAlign": "center"}),

        dcc.Slider(
            id="year-slider",
            min=YEAR_MIN, max=YEAR_MAX, value=YEAR_MIN,
            marks={str(y): str(y) for y in range(YEAR_MIN, YEAR_MAX + 1)},
            step=None,
            tooltip={"placement": "bottom", "always_visible": True},
        ),
        html.Br(),
        dcc.Graph(id="choropleth-map"),
    ]
)

@callback(
    Output("choropleth-map", "figure"), 
    Input("year-slider", "value")
)

def update_map(selected_year):
    d = df[df["year"] == selected_year]

    fig = px.choropleth(
        d,
        locations="state",               # 2-letter USPS codes
        locationmode="USA-states",
        color="price",
        scope="usa",
        color_continuous_scale="Reds",
        ##setting range color by the variables made above
        range_color=(V_MIN, V_MAX),      # consistent across years
        labels={"price": "Price (cents/kWh)"},
        title=f"Residential Electricity Prices - {selected_year}",
    )

    ##added a better hovertemplate at 1 decimal
    fig.update_traces(
        hovertemplate="<b>%{location}</b><br>Price: %{z:.1f} cents/kWh<extra></extra>"
    )

    fig.update_layout(
        geo=dict(bgcolor="#B9975B"), ##Background color around map
        paper_bgcolor = "#32453C", 
        font_color = "white",
        margin=dict(l=10, r=10, t=50, b = 10)         
    )
    return fig

