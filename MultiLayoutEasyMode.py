from dash import Dash, html
import dash_bootstrap_components as dbc

##initiate the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Multi Layout App"

box_style = {
    "border": "2px solid black",
    "borderRadius": "5px", 
    "margin": "5px",
    "padding":"20px", 
    "backgroundColor": "#e0f7fa"    
}

##set app.layout
app.layout = dbc.Container([
    ##Row 1 full width
    dbc.Row(dbc.Col(html.Div("Top Row (Full Width)", style=box_style))),
    dbc.Row([
        dbc.Col(html.Div("Left Column", style=box_style)),
        dbc.Col(html.Div("Right Column", style=box_style))
    ]),
    dbc.Row(dbc.Col(html.Div("Footer (Full Width)", style=box_style)))
    
], fluid=True)

##run the app
if __name__ == "__main__":
    app.run(debug=True)
