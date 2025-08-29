##import my dash library
from dash import Dash, html

##create my dash app
app = Dash(__name__)
app.title = "My First Dash App"

###Define the layout
app.layout = html.Div([
    html.H1("Hello Dash", style={"color": "#3B2658",
                                 "fontSize":"20px",
                                 "backgroundColor":"#E898AA"}),
    html.P("This is a simple dashboard", style={"border":"1px solid black",
                                                "padding":"20px", 
                                                "margin":"50px"}),
    html.Br(),
    html.A("Click here", href="https://example.com") 
])

##run the app
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)


