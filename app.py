import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load the data
data = pd.read_csv("data/co2_per_capita.csv")

# Dash app initialization with external Bootstrap stylesheet and custom assets
app = dash.Dash(
    __name__,
    external_stylesheets=[
        "https://cdn.jsdelivr.net/npm/bootswatch@5.3.0/dist/minty/bootstrap.min.css",
    ],
    assets_folder='assets',  # Custom assets folder
    suppress_callback_exceptions=True,
)

server = app.server

app.title = "CO2 Emissions Per Capita Analysis"
# This is my block for the App layout
# this is for defining the HTML layout using Dash HTML components

# Load the data

# Navigation bar with the dashboard title
navbar = html.Nav(
    className="navbar navbar-expand-lg navbar-light bg-primary",
    children=[
        html.Div(
            className="container-fluid d-flex justify-content-center",
            children=[
                html.A(
                    "CO2 Emissions Per Capita Dashboard",
                    className="navbar-brand",
                    style={"font-size": "2em"},  # Larger font
                ),
            ],
        ),
    ],
)

# Radio button group with centered mode text
radio_group_with_mode = html.Div(
    className="d-flex justify-content-center",  # Centered alignment
    children=[
        html.Div(
            id="current-mode",  # To be updated with the selected mode
            children=["Your current mode is: Worldview"],  # Default mode
            style={"font-size": "1.5em", "text-align": "center"},  # Centered text
        ),
        dcc.RadioItems(
            id="mode-selector",
            options=[
                {"label": "Worldview", "value": "worldview"},
                {"label": "Single Country View", "value": "single_country"},
                {"label": "Multiple Country View", "value": "multiple_country"},
                {"label": "Year View", "value": "year_view"},
            ],
            value="worldview",  # Default selected value
            inputClassName="btn-check",  # Bootstrap class for radio inputs
            labelClassName="btn btn-outline-primary",  # Label class for styling
            labelStyle={"margin-right": "10px"},  # Horizontal layout spacing
            inline=True,  # Horizontal layout
        ),
    ],
)

mode_descriptions = {
    "worldview": "In the Worldview mode, you can explore CO2 emissions per capita across all countries over a chosen time range. These graphs show trends over time and the distribution of emissions across the globe.",
    "single_country": "In the Single Country View mode, you can analyze CO2 emissions for a specific country over a selected period. This mode allows you to understand how emissions have changed within a particular country over time",
    "multiple_country": "In the Multiple Country View mode, you can compare CO2 emissions per capita across multiple countries. This mode provides insights into how emissions differ between countries during a specific period.",
    "year_view": "In the Year View mode, you can analyze CO2 emissions per capita for a specific year across various countries. This mode helps you visually identify the trend in a year."
}

app.layout = html.Div([
    navbar,  # Include the navbar at the top
    
    # Section for dashboard title and card-styled description
    html.Div(
        className="d-flex justify-content-between align-items-center",
        style={"padding": "20px"},  # Padding for visual appeal
        children=[
            # Dashboard title and card-styled description occupying 50% of the width
            html.Div(
                className="d-flex flex-column justify-content-center align-items-center",
                style={"width": "50%"},  # 50% of the section's width
                children=[
        
                    # Dashboard description in a card
                    html.Div(
                        className="card border-primary mb-3",
                        style={"width": "100%"},  # Take full width of its parent div
                        children=[
                            html.Div("     ", className="card-header"),
                            html.Div(
                                className="card-body",
                                children=[
                                    html.H4("Welcome to the CO2 Emissions Per Capita Dashboard!", className="card-title"),
                                    html.P(
                                        "Welcome to the CO2 Emissions Per Capita Dashboard. This platform helps you explore carbon dioxide emissions from different countries over time, providing insights into trends, distributions, and comparisons on a global scale. Through interactive graphs, you can visualize how CO2 emissions per capita have changed across various regions, offering a unique perspective on our planet's environmental challenges. But this dashboard is more than just a collection of data—it's a call to action. As you explore the information, consider the broader impact of carbon emissions on climate change and what it means for future generations. This is your chance to understand the urgency of reducing emissions and inspire others to take action. Whether through individual choices or political advocacy, every effort counts in the fight against climate change. Use this dashboard as a catalyst for change, both in your life and in your community, to help build a more sustainable world.",
                                        className="card-text",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            
            # Section for mode display, mode description, and radio buttons
            html.Div(
                className="d-flex flex-column justify-content-center align-items-center",
                style={"width": "50%"},  # Remaining 50% of the section's width
                children=[
                    html.H2(  # Update to H2 for current mode text
                        id="current-mode",
                        children=["Your current mode is: Worldview"],
                        style={"font-family": "Arial, sans-serif"},  # Consistent font
                    ),
                    html.Div(
                        id="mode-description",
                        style={"font-size": "1em", "text-align": "center", "margin-top": "10px", "margin-bottom": "20px"},  # Extra space below description
                        children=[mode_descriptions["worldview"]],
                    ),
                    dcc.RadioItems(
                        id="mode-selector",
                        options=[
                            {"label": "Worldview", "value": "worldview"},
                            {"label": "Single Country View", "value": "single_country"},
                            {"label": "Multiple Country View", "value": "multiple_country"},
                            {"label": "Year View", "value": "year_view"},
                        ],
                        value="worldview",  # Default selected value
                        inputClassName="btn-check",
                        labelClassName="btn btn-outline-primary",
                        labelStyle={"margin-right": "10px"},
                        inline=True,
                    ),
                ],
            ),
        ],
    ),
    
    # Content to be updated based on mode selection
    html.Div(
        id="mode-display",
        style={"padding": "20px"},
    ),
])

# Callbacks and other functionality remain the same


# Callbacks and other functionality remain the same


# Callback to update the current mode display
@app.callback(
    Output("current-mode", "children"),
    [Input("mode-selector", "value")]
)
def update_current_mode(mode):
    mode_dict = {
        "worldview": "Worldview",
        "single_country": "Single Country View",
        "multiple_country": "Multiple Country View",
        "year_view": "Year View",
    }
    return [f"Your current mode is: {mode_dict[mode]}"]

@app.callback(
    [
        Output("mode-description", "children"), 
        Output("mode-display", "children")
    ],  # Update the description and content
    [
        Input("mode-selector", "value")
    ]
)
def update_mode_content(mode):
    # Define the mode description based on the selected mode
    mode_description = mode_descriptions.get(mode, "Unknown mode")
    
    # Initialize the content variable
    content = None

    # Worldview mode
    if mode == "worldview":
        content = html.Div(
            children=[
                # RangeSlider for selecting years
                dcc.RangeSlider(
                    id="worldview-year-slider",
                    min=data["year"].min(),
                    max=data["year"].max(),
                    value=[data["year"].min(), data["year"].max()],
                    marks={str(year): str(year) for year in range(data["year"].min(), data["year"].max() + 1, 10)},
                    step=1,
                ),

                # Container for the line graph and its text card
                html.Div(
                    children=[
                        # Line graph (66% width)
                        html.Div(
                            dcc.Graph(id="worldview-line-graph"),
                            style={"width": "75%", "padding-right": "10px"},  # 66% width with padding-right
                        ),
                        
                        # Text card for line graph description (33% width)
                        html.Div(
                            html.Div(
                                className="card border-primary mb-3",
                                children=[
                                    html.Div(" ", className="card-header"),
                                    html.Div(
                                        className="card-body",
                                        children=[
                                            html.H4("Line Graph Description", className="card-title"),
                                            html.P(
                                                "The line graph in the Worldview mode shows the trend of CO2 emissions per capita across time. You can use the year range slider to adjust the time frame and observe how emissions have changed globally.",
                                                className="card-text",
                                            ),
                                        ],
                                    ),
                                ],
                                style={"max-width": "20rem"},  # Consistent card size
                            ),
                            style={"width": "25%", "padding-left": "10px"},  # 33% width with padding-left
                        ),
                    ],
                    style={"display": "flex", "justify-content": "space-between", "align-items": "center"},  # Flex layout
                ),

                # Container for the histogram and its text card
                html.Div(
                    children=[
                        # Text card for histogram description (25% width)
                        html.Div(
                            html.Div(
                                className="card border-primary mb-3",
                                children=[
                                    html.Div(" ", className="card-header"),
                                    html.Div(
                                        className="card-body",
                                        children=[
                                            html.H4("Histogram Description", className="card-title"),
                                            html.P(
                                                "The histogram displays the distribution of CO2 emissions per capita across all countries. It provides a visual representation of how emissions are spread over time and identifies high and low-emission countries.",
                                                className="card-text",
                                            ),
                                        ],
                                    ),
                                ],
                                style={"max-width": "20rem"},  # Consistent card size
                            ),
                            style={"width": "25%", "padding-right": "10px"},  # 25% width with padding-right
                        ),
                        
                        # Histogram (75% width)
                        html.Div(
                            dcc.Graph(id="worldview-histogram"),
                            style={"width": "75%", "padding-left": "10px"},  # 75% width with padding-left
                        ),
                    ],
                    style={"display": "flex", "justify-content": "space-between", "align-items": "center"},  # Flex layout
                ),
            ],
            style={"padding": "20px"},  # Outer padding for spacing
        )




            # Single Country mode

    elif mode == "single_country":
        content = html.Div(
            children=[
                # Dropdown and year range slider
                html.Div(
                    children=[
                        html.Div(
                            dcc.Dropdown(
                                id="country-dropdown",
                                options=[{"label": country, "value": country} for country in data["country"].unique()],
                                value="USA",  # Default value
                            ),
                            style={"width": "50%", "padding-right": "10px"},  # 50% width with padding-right
                        ),
                        html.Div(
                            dcc.RangeSlider(
                                id="year-slider",
                                min=data["year"].min(),
                                max=data["year"].max(),
                                value=[data["year"].min(), data["year"].max()],
                                marks={str(year): str(year) for year in range(data["year"].min(), data["year"].max() + 1, 10)},
                                step=1,
                            ),
                            style={"width": "50%", "padding-left": "10px"},  # 50% width with padding-left
                        ),
                    ],
                    style={"display": "flex", "justify-content": "space-between", "align-items": "center"},
                ),

                # Container for the graphs and text description cards
                html.Div(
                    children=[
                        # Line graph and its text card
                        html.Div(
                            children=[
                                dcc.Graph(id="line-graph"),  # Line graph for single country
                                html.Div(
                                    className="card border-primary mb-3",
                                    children=[
                                        html.Div(" ", className="card-header"),
                                        html.Div(
                                            className="card-body",
                                            children=[
                                                html.H4("Line Graph Description", className="card-title"),
                                                html.P(
                                                    "The line graph in the Single Country mode demonstrates CO2 emissions per capita for a specific country over time. You can select a country from the dropdown and adjust the year range slider to observe changes in emissions",
                                                    className="card-text",
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            style={"width": "45%", "padding-bottom": "10px"},  # 50% width with padding-bottom
                        ),

                        # Box plot and its text card
                        html.Div(
                            children=[
                                dcc.Graph(id="box-plot"),  # Box plot for single country
                                html.Div(
                                    className="card border-primary mb-3",
                                    children=[
                                        html.Div(" ", className="card-header"),
                                        html.Div(
                                            className="card-body",
                                            children=[
                                                html.H4("Box Plot Description", className="card-title"),
                                                html.P(
                                                    "The box plot in the Single Country mode illustrates the distribution of CO2 emissions per capita within a chosen country. It helps identify trends and outliers in the emissions data.",
                                                    className="card-text",
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            style={"width": "45%", "padding-bottom": "10px"},  # 50% width with padding-bottom
                        ),
                    ],
                    style={"display": "flex", "justify-content": "space-between", "align-items": "center"},  # Flex layout for 50/50 space
                ),
            ],
            style={"padding": "20px"},  # Outer padding for spacing
        )








            # Multiple Country mode
    elif mode == "multiple_country":
        content = html.Div(
            children=[
                # Dropdown and year range slider for multiple countries
                html.Div(
                    children=[
                        html.Div(
                            dcc.Dropdown(
                                id="multiple-country-dropdown",
                                multi=True,
                                options=[{"label": country, "value": country} for country in data["country"].unique()],
                                value=["USA", "China"],  # Default selected values
                            ),
                            style={"width": "50%"},  # 50% width for the dropdown
                        ),
                        html.Div(
                            dcc.RangeSlider(
                                id="multiple-year-slider",
                                min=data["year"].min(),
                                max=data["year"].max(),
                                value=[data["year"].min(), data["year"].max()],
                                marks={str(year): str(year) for year in range(data["year"].min(), data["year"].max() + 1, 10)},
                                step=1,
                            ),
                            style={"width": "50%"},  # 50% width for the range slider
                        ),
                    ],
                    style={"display": "flex", "justify-content": "space-between", "align-items": "center"},
                ),

                # Container for the graphs and text description cards
                html.Div(
                    children=[
                        # Line graph for multiple countries and its text card
                        html.Div(
                            children=[
                                dcc.Graph(id="multi-country-line-graph"),  # Line graph for multiple countries
                                html.Div(
                                    className="card border-primary mb-3",
                                    children=[
                                        html.Div(" ", className="card-header"),
                                        html.Div(
                                            className="card-body",
                                            children=[
                                                html.H4("Line Graph Description", className="card-title"),
                                                html.P(
                                                    "The line graph in the Multiple Country mode displays CO2 emissions per capita trends for selected countries over a given time range. You can use the dropdown to select multiple countries for comparison",
                                                    className="card-text",
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            style={"width": "45%", "padding-bottom": "10px"},  # 50% width for the text card
                        ),

                        # Violin graph for multiple countries and its text card
                        html.Div(
                            children=[
                                dcc.Graph(id="multi-country-violin-graph"),  # Violin graph for multiple countries
                                html.Div(
                                    className="card border-primary mb-3",
                                    children=[
                                        html.Div(" ", className="card-header"),
                                        html.Div(
                                            className="card-body",
                                            children=[
                                                html.H4("Violin Graph Description", className="card-title"),
                                                html.P(
                                                    "The violin plot shows the distribution of CO2 emissions per capita across multiple countries. It offers a visual comparison of emissions data, allowing you to identify variations among countries.",
                                                    className="card-text",
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            style={"width": "45%", "padding-bottom": "10px"},  # 50% width for the text card
                        ),
                    ],
                    style={"display": "flex", "justify-content": "space-between", "align-items": "center"},  # Flex layout for 50/50 space
                ),
            ],
            style={"padding": "20px"},  # Outer padding for spacing
        )





    # Year View mode
    elif mode == "year_view":
        content = html.Div(
            children=[
                # Slider to select the year
                dcc.Slider(
                    id="single-year-slider",
                    min=data["year"].min(),
                    max=data["year"].max(),
                    value=data["year"].max(),
                    marks={str(year): str(year) for year in range(data["year"].min(), data["year"].max() + 1, 10)},
                    step=1,
                ),

                # Container for the bar graph and the description text card
                html.Div(
                    children=[
                        # Bar graph taking 75% of the width
                        html.Div(
                            dcc.Graph(id="year-bar-graph"),
                            style={"width": "75%", "padding-right": "10px"},  # 75% width with padding-right
                        ),

                        # Description text card for the graph
                        html.Div(
                            html.Div(
                                className="card border-primary mb-3",
                                children=[
                                    html.Div(" ", className="card-header"),
                                    html.Div(
                                        className="card-body",
                                        children=[
                                            html.H4("Bar Graph Description", className="card-title"),
                                            html.P(
                                                "The bar graph in the Year View mode represents CO2 emissions per capita for a specific year across different countries. This graph helps you see which countries had the highest and lowest emissions in that year.",
                                                className="card-text",
                                            ),
                                        ],
                                    ),
                                ],
                                style={"max-width": "20rem"},  # Ensure consistent card size
                            ),
                            style={"width": "25%", "padding-left": "10px"},  # 25% width with padding-left
                        ),
                    ],
                    style={"display": "flex", "justify-content": "space-between", "align-items": "center"},  # Flex layout
                ),
            ],
            style={"padding": "20px"},  # Outer padding for spacing
        )

    # Return the mode description and content
    return mode_description, content

# Callback for updating graphs in the Worldview mode
@app.callback(
    [Output("worldview-line-graph", "figure"),
     Output("worldview-histogram", "figure")],
    [Input("worldview-year-slider", "value")]
)
def update_worldview_graphs(year_range):
    filtered_data = data[
        (data["year"] >= year_range[0]) &
        (data["year"] <= year_range[1])
    ]
    
    line_fig = px.line(
        filtered_data,
        x="year",
        y="co2_per_capita",
        color="country",
        title="Global CO2 Emissions Per Capita Over Time",
    )
    line_fig.update_layout(
        xaxis_title="Year",  # Renamed
        yaxis_title="CO2 Per Capita",  # Renamed
    )

    histogram_fig = px.histogram(
        filtered_data,
        x="co2_per_capita",
        nbins=50,
        title="Distribution of Global CO2 Emissions Per Capita",
    )
    histogram_fig.update_layout(
        xaxis_title="CO2 Per Capita",  # Renamed
        yaxis_title="Count",  # Renamed
    )

    return line_fig, histogram_fig



# Callback to update graphs for the Single Country View
@app.callback(
    [Output("line-graph", "figure"),
     Output("box-plot", "figure")],
    [Input("country-dropdown", "value"),
     Input("year-slider", "value")]
)
def update_single_country_graphs(selected_country, year_range):
    #    # I am first filtering the data based on the selected country and year range
    filtered_data = data[(data['country'] == selected_country) &
                         (data['year'] >= year_range[0]) &
                         (data['year'] <= year_range[1])]
    
    # Then I am obviously creating the line graph with the filtered data
    line_fig = px.line(
        filtered_data, 
        x="year", 
        y="co2_per_capita", 
        title=f"CO2 Emissions Per Capita in {selected_country}"
    )
    # I will now be updating the layout of the line graph
    line_fig.update_layout(
        xaxis_title="Year",
        yaxis_title="CO2 Emissions Per Capita",
        margin={'l': 40, 'b': 40, 't': 40, 'r': 20},  # This is just some extra code to adjust margins to avoid cutoff
        height=400  # Just makiing sure the height matches box plot
    )

    # I will not create the box plot with my filtered data
    box_fig = px.box(
        filtered_data, 
        y="co2_per_capita", 
        title=f"Distribution of CO2 Emissions Per Capita in {selected_country}"
    )
    # Now i am updating update the layout of the box plot
    box_fig.update_layout(
        yaxis_title="CO2 Emissions Per Capita",
        margin={'l': 40, 'b': 40, 't': 40, 'r': 20},  # This is just some extra code to adjust margins to avoid cutoff
        height=400  # Just makiing sure the height matches box plot
    )

    # Now, finally I am returniong both figures
    return line_fig, box_fig

# Fix for Multiple Country View with proper data structure

@app.callback(
    [Output("multi-country-line-graph", "figure"),
     Output("multi-country-violin-graph", "figure")],
    [Input("multiple-country-dropdown", "value"),
     Input("multiple-year-slider", "value")]
)
def update_multi_country_graphs(selected_countries, year_range):
    filtered_data = data[
        (data["country"].isin(selected_countries)) &
        (data["year"] >= year_range[0]) &
        (data["year"] <= year_range[1])
    ]
    
    line_fig = px.line(
        filtered_data,
        x="year",
        y="co2_per_capita",
        color="country",
        title="CO2 Emissions Per Capita Over Time for Selected Countries",
    )
    line_fig.update_layout(
        xaxis_title="Year",  # Renamed
        yaxis_title="CO2 Per Capita",  # Renamed
    )

    violin_fig = px.violin(
        filtered_data,
        y="co2_per_capita",
        color="country",
        box=True,
        title="Distribution of CO2 Emissions Per Capita for Selected Countries",
    )
    violin_fig.update_layout(
        yaxis_title="CO2 Per Capita",  # Renamed
    )

    return line_fig, violin_fig


@app.callback(
    Output("year-bar-graph", "figure"),
    [Input("single-year-slider", "value")]
)
def update_year_graph(selected_year):
    filtered_data = data[
        (data["year"] == selected_year)
    ]
    
    bar_fig = px.bar(
        filtered_data,
        x="country",
        y="co2_per_capita",
        title=f"CO2 Emissions Per Capita in {selected_year}",
    )
    bar_fig.update_layout(
        xaxis_title="Country",  # Renamed
        yaxis_title="CO2 Per Capita",  # Renamed
    )

    return bar_fig



# Start the server
if __name__== '__main__':
    app.run_server(debug=True)
