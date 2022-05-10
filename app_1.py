
# from dash import Dash, dash_table, dcc, html, Input, Output
# import pandas as pd

# # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
# df = pd.read_parquet('tokens.parquet')
# df = df[[
#     'symbol',
#     'name',
#     'contract',
#     'decimal',
#     'blockchain',
#     'total_supply',
#     'verified'
# ]]

# app = Dash(__name__)


# app.layout = dash_table.DataTable(df.to_dict('records'), 
#                                   [{"name": i, "id": i} for i in df.columns],
#                                     page_size = 15,
#                                     style_cell = {
#                                                  'textAlign': 'left'
#                                               },
#                                     style_header = {
#                                                  'backgroundColor': '#C0C0C0',
#                                                  'fontWeight': 'bold',
#                                                 },
#                                     editable=False,
#                                     filter_action="native",
#                                     sort_action="native",
#                                     sort_mode="multi",
#                                     column_selectable="single",
#                                     row_selectable="multi",
#                                     row_deletable=False,
#                                     selected_columns=[],
#                                     selected_rows=[],
#                                     page_action="native",
#                                     page_current= 0,
#                                  )

# if __name__ == '__main__':
#     app.run_server(debug=True)

# ----------

# from dash import Dash, dcc, html, Input, Output
# import pandas as pd

# df = pd.read_parquet('tokens.parquet')
# app = Dash(__name__)
# app.layout = html.Div([
#     dcc.Dropdown(
#     df['blockchain'].drop_duplicates().sort_values().to_list(),
#     placeholder="Select a blockchain",
#     value = None,
#     id = 'demo-dropdown'
# ),
#     html.Div(id='dd-output-container')
# ])


# @app.callback(
#     Output('dd-output-container', 'children'),
#     Input('demo-dropdown', 'value')
# )
# def update_output(value):
#     return f'You have selected {value}'


# if __name__ == '__main__':
#     app.run_server(debug=True)


# ---------------------


from dash import Dash, dash_table, dcc, html, Input, Output
import pandas as pd

df = pd.read_parquet('tokens.parquet')
app = Dash(__name__)


app.layout = html.Div([
    dcc.Dropdown(
    df['blockchain'].drop_duplicates().sort_values().to_list(),
    placeholder="Select a blockchain",
    value = None,
    id = 'demo-dropdown'
),
    
    html.Div(id='dd-output-container'),
    
    html.Div(
    dash_table.DataTable(df.to_dict('records'), 
                                  [{"name": i, "id": i} for i in df.columns],
                                    page_size = 15,
                                    style_cell = {
                                                 'textAlign': 'left'
                                              },
                                    style_header = {
                                                 'backgroundColor': '#C0C0C0',
                                                 'fontWeight': 'bold',
                                                },
                                    editable=False,
                                    filter_action="native",
                                    sort_action="native",
                                    sort_mode="multi",
                                    column_selectable="single",
                                    row_selectable="multi",
                                    row_deletable=False,
                                    selected_columns=[],
                                    selected_rows=[],
                                    page_action="native",
                                    page_current= 0,
                                 )
    )
])


@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    return f'You have selected {value}'


if __name__ == '__main__':
        app.run_server(debug=True, port=8050)


# ------------------------------
