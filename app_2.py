"""
A simple app demonstrating how to manually construct a navbar with a customised
layout using the Navbar component and the supporting Nav, NavItem, NavLink,
NavbarBrand, and NavbarToggler components.

Requires dash-bootstrap-components 0.3.0 or later
"""
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html, dcc, dash_table
import pandas as pd

# PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
# GITHUB_LOGO = "https://github.com/Inabat13/cryptodash/blob/main/assets/GitHub-Mark-Light-64px.png"

PLOTLY_LOGO = "assets/PS_logo_Vert_s.png"
GITHUB_LOGO = "assets/GitHub-Mark-Light-64px.png"
df = pd.read_parquet('tokens.parquet')
df = df[[
    'symbol',
    'name',
    'contract',
    'decimal',
    'blockchain',
    'total_supply',
    'verified'
]]



app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
# try running the app with one of the Bootswatch themes e.g.
# app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL])
# app = dash.Dash(external_stylesheets=[dbc.themes.SKETCHY])

# make a reuseable navitem for the different examples
nav_item = dbc.NavItem(dbc.NavLink("View on GitHub", href="https://github.com/Inabat13/cryptodash"))


# make a reuseable dropdown for the different examples
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Entry 1"),
        dbc.DropdownMenuItem("Entry 2"),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Entry 3"),
    ],
    nav=True,
    in_navbar=True,
    label="Menu",
)

# # this is the default navbar style created by the NavbarSimple component
# default = dbc.NavbarSimple(
#     children=[nav_item, dropdown],
#     brand="Default",
#     brand_href="#",
#     sticky="top",
#     className="mb-5",
# )

# # here's how you can recreate the same thing using Navbar
# # (see also required callback at the end of the file)
# custom_default = dbc.Navbar(
#     dbc.Container(
#         [
#             dbc.NavbarBrand("Custom default", href="#"),
#             dbc.NavbarToggler(id="navbar-toggler1"),
#             dbc.Collapse(
#                 dbc.Nav(
#                     [nav_item, dropdown], className="ms-auto", navbar=True
#                 ),
#                 id="navbar-collapse1",
#                 navbar=True,
#             ),
#         ]
#     ),
#     className="mb-5",
# )


# this example that adds a logo to the navbar brand
logo = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("FB-PS crypto dash", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://www.fatbrain.ai/",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    [
                        
                     html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=GITHUB_LOGO, height="30px")),
                    ],
                    align="center",
                    className="g-0",
                ),
            ),         
                    nav_item, dropdown],
                    className="ms-auto",
                    navbar=True,
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ],
    ),
    color="dark",
    dark=True,
    className="mb-5",
)

# # this example has a search bar and button instead of navitems / dropdowns
# search_navbar = dbc.Navbar(
#     dbc.Container(
#         [
#             dbc.NavbarBrand("Search", href="#"),
#             dbc.NavbarToggler(id="navbar-toggler3"),
#             dbc.Collapse(
#                 dbc.Row(
#                     [
#                         dbc.Col(
#                             dbc.Input(type="search", placeholder="Search")
#                         ),
#                         dbc.Col(
#                             dbc.Button(
#                                 "Search", color="primary", className="ms-2"
#                             ),
#                             # set width of button column to auto to allow
#                             # search box to take up remaining space.
#                             width="auto",
#                         ),
#                     ],
#                     # add a top margin to make things look nice when the navbar
#                     # isn't expanded (mt-3) remove the margin on medium or
#                     # larger screens (mt-md-0) when the navbar is expanded.
#                     # keep button and search box on same row (flex-nowrap).
#                     # align everything on the right with left margin (ms-auto).
#                     className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
#                     align="center",
#                 ),
#                 id="navbar-collapse3",
#                 navbar=True,
#             ),
#         ]
#     ),
#     className="mb-5",
# )


data_table = html.Div([
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
                                    page_size = 5,
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
#                                     column_selectable="single",
#                                     row_selectable="multi",
                                    row_deletable=False,
                                    selected_columns=[],
                                    selected_rows=[],
                                    page_action="native",
                                    page_current= 0,
                                 )
    ),
])



# # custom navbar based on https://getbootstrap.com/docs/4.1/examples/dashboard/
# dashboard = dbc.Navbar(
#     dbc.Container(
#         [
#             dbc.Col(dbc.NavbarBrand("Dashboard", href="#"), sm=3, md=2),
#             dbc.Col(dbc.Input(type="search", placeholder="Search here")),
#             dbc.Col(
#                 dbc.Nav(
#                     dbc.Container(dbc.NavItem(dbc.NavLink("Sign out"))),
#                     navbar=True,
#                 ),
#                 width="auto",
#             ),
#         ],
#     ),
#     color="dark",
#     dark=True,
# )

app.layout = html.Div(
    [
#      default, 
#      custom_default, 
     logo, 
#      search_navbar,
     data_table
#      dashboard
    ]
)


# we use a callback to toggle the collapse on small screens
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# the same function (toggle_navbar_collapse) is used in all three callbacks
for i in [1, 2, 3]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)
    

if __name__ == "__main__":
    app.run_server(debug=True, port=8888)