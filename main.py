from dash import html,Dash, dcc, Output, Input
import pandas
import plotly.express as px

def loadData():
    data = pandas.read_csv("output.csv")
    data["Date"] = pandas.to_datetime(data["Date"])
    return data


def buildGraph(data):
    salesOnDate = data.groupby("Date", as_index=False)["Sales"].sum()

    graph = px.line(
        salesOnDate,
        x="Date",
        y="Sales",
    )
    
    return html.Div(
        [dcc.Graph(id="sales-chart",figure=graph)],
        style={
            "backgroundColor": "#6CAEC6",
            "padding": "20px",
            "borderRadius": "12px",
            "marginBottom": "20px"
        }
    )

def buildHeader():
    return html.Header([
        html.H1("Soul Foods Pink Morsel Sales",
        style={
            "textAlign": "center",
            "color": "#BA4560",
            "marginBottom": "10px"
        })
    ])

def buildRadioButtons():
    return html.Div([
        html.Label("Choose a region:",
            style={
                "color": "#BA4560",
                "fontWeight": "bold",
                "display": "block",
                "marginBottom": "10px"
            }
        ),
        dcc.RadioItems(
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"}
            ],
            value="all",
            id="region-filter",
            inline=True,
            style={
                "marginBottom": "20px",
                "color": "#BA4560"
            }
        )
    ],
    style={
        "backgroundColor": "#6CAEC6",
        "padding": "20px",
        "borderRadius": "12px",
        "marginBottom": "20px"
    })

def main():
    data=loadData()
    app=Dash(__name__)
    app.layout = html.Div([
        buildHeader(),
        buildGraph(data),
        buildRadioButtons()  
    ])

    @app.callback(
        Output("sales-chart", "figure"),
        Input("region-filter", "value")
    )
    def updateGraph(selectedRegion):
        filteredData = data

        if selectedRegion != "all":
            filteredData = data[data["Region"] == selectedRegion]

        salesOnDate = filteredData.groupby("Date", as_index=False)["Sales"].sum()

        figure = px.line(
            salesOnDate,
            x="Date",
            y="Sales",
            labels={
                "Date": "Date",
                "Sales": "Sales"
            },
            title="Pink Morsel Sales Over Time"
        )

        figure.update_layout(
            plot_bgcolor="#FEDACD",
            paper_bgcolor="white",
            font={"color": "#BA4560"},
            title={"x": 0.5}
        )

        figure.update_traces(line={"color": "#6CAEC6"})

        return figure
    app.run(debug=True)

if __name__ == "__main__":
    main()




