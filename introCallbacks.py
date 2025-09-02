# callback_example.py
from dash import Dash, html, dcc, Input, Output, callback

app = Dash(__name__)
app.title = "Callback Example"

app.layout = html.Div(
    style={"maxWidth": 900, "margin": "40px auto", "fontFamily": "Georgia, serif"},
    children=[
        html.H1("Callback Example"),
        html.Ul([
            html.Li(["Input box’s ", html.Code("value"), " property updates output text"])
        ]),
        dcc.Input(
            id="text-in",
            type="text",
            placeholder="type here…",
            style={"width": "100%", "fontSize": "48px", "padding": "8px"},
        ),
        html.Div(id="text-out", style={"fontSize": "64px", "marginTop": "20px"}),
    ],
)

@callback(Output(component_id="text-out", component_property="children"),
          Input(component_id="text-in", component_property="value"))
def show_text(value):
    return f"Text: {value or ''}"

if __name__ == "__main__":
    app.run(debug=True)

