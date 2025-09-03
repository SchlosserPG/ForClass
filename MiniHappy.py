from dash import Dash, html

##initialize the app
app = Dash(__name__)

##Set up the layout
app.layout = html.Div([ 
    html.H1("World Happiness Dashboard"),
    html.P("This dashboard will visualize world hapiness score"),
    html.Br(),
    html.A("World Happiness Report", href="https://worldhappiness.report/",
           target="_blank", style={"color":"#6065a3", "textDecoration":"underline"}),
                       
])

##run the app
if __name__ == '__main__':
    app.run(debug=True)
    