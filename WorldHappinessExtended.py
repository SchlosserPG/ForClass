from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Load your dataset (adjust the path or filename as needed)
df = pd.read_csv('data/world_happiness.csv')

# Clean and prepare the dataset
df = df.rename(columns={
    "country": "Country",
    "year": "Year",
    "Life Ladder": "Happiness Score"
})
df['Year'] = df['Year'].astype(int)

# Create app
app = Dash(__name__)
app.title = "World Happiness Dashboard"

# App layout
app.layout = html.Div(style={'padding': '20px', 'backgroundColor': "#FAF3DD"}, children=[
    html.H1("World Happiness Dashboard", style={'textAlign': 'center', 'color': '#013A63'}),
    html.P("Explore global happiness trends by year.", style={'textAlign': 'center'}),
    
    html.Div([
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': str(year), 'value': year} for year in sorted(df['Year'].unique())],
            value=df['Year'].max(),
            clearable=False,
            style={'width': '50%'}
        )
    ], style={'textAlign': 'center', 'marginBottom': '30px'}),
    
    dcc.Graph(id='happiness-map'),
    dcc.Graph(id='top-bottom-bar'),

    html.Div([
        html.A("World Happiness Report Data Source", 
               href="https://worldhappiness.report/", 
               target="_blank",
               style={'textAlign': 'center', 'display': 'block', 'marginTop': '20px'})
    ])
])

# Callback for updating map and bar chart
@app.callback(
    [Output('happiness-map', 'figure'),
     Output('top-bottom-bar', 'figure')],
    [Input('year-dropdown', 'value')]
)
def update_dashboard(selected_year):
    filtered_df = df[df['Year'] == selected_year]

    # Choropleth map
    map_fig = px.choropleth(
        filtered_df,
        locations="Country",
        locationmode="country names",
        color="Happiness Score",
        hover_name="Country",
        color_continuous_scale="viridis",
        title=f"Happiness Score by Country - {selected_year}"
    )
    #Removes left, right, and bottom margins (l=0, r=0, b=0) 
    # so the map fills more space.
    map_fig.update_layout(margin=dict(l=0, r=0, t=40, b=0))

    # Bar chart for top 5 and bottom 5
    top_bottom = pd.concat([
        filtered_df.nlargest(5, 'Happiness Score'),
        filtered_df.nsmallest(5, 'Happiness Score')
    ])
    bar_fig = px.bar(
        top_bottom.sort_values('Happiness Score'),
        x='Happiness Score',
        y='Country',
        orientation='h',
        color='Happiness Score',
        title=f"Top and Bottom Countries by Happiness Score - {selected_year}",
        color_continuous_scale='BrBG'
    )
    bar_fig.update_layout(yaxis={'categoryorder': 'total ascending'})

    return map_fig, bar_fig

# Run server
if __name__ == '__main__':
    app.run(debug=True)
