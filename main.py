from dash import html,Dash, dcc
import pandas
import plotly.express as px

def buildGraph():
    data = pandas.read_csv("output.csv")
    data["Date"] = pandas.to_datetime(data["Date"])

    salesOnDate = data.groupby("Date", as_index=False)["Sales"].sum()

    graph = px.line(
        salesOnDate,
        x="Date",
        y="Sales",
    )
    return graph

def buildHeader():
    return html.Header([
        html.H1("Soul Foods Pink Morsel Sales")
    ])

def main():
    app=Dash(__name__)
    app.layout = html.Div([
        buildHeader(),
        dcc.Graph(figure=buildGraph())
    ])
    app.run()

if __name__ == "__main__":
    main()




