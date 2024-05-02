import dash
from dash import dcc, html, Input, Output
import plotly.figure_factory as ff
import pandas as pd
import numpy as np
from covarience_functions import calculate_covariance_matrices

# load & clean data
df = pd.read_csv('Datasets\combined\merged_data_renters.csv')
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

# get cov. matrix
covariance_matrices = calculate_covariance_matrices(df)


# initilize  dash app
app = dash.Dash(__name__)

# define the layout of the app
app.layout = html.Div([
    dcc.Dropdown(
        id='county-dropdown',
        options=[{'label': county, 'value': county} for county in covariance_matrices.keys()],
        value=list(covariance_matrices.keys())[0]  # default value
    ),
    dcc.Graph(id='covariance-heatmap')
])

# define callback to update heatmap based on selected county
@app.callback(
    Output('covariance-heatmap', 'figure'),
    [Input('county-dropdown', 'value')]
)
def update_heatmap(selected_county):
    if covariance_matrices[selected_county] is not None:
        # creating the heatmap figure from the covariance matrix
        fig = ff.create_annotated_heatmap(
            z=covariance_matrices[selected_county].to_numpy(),
            x=covariance_matrices[selected_county].columns.tolist(),
            y=covariance_matrices[selected_county].index.tolist(),
            annotation_text=covariance_matrices[selected_county].round(2).to_numpy(),
            showscale=True
        )
        fig.update_layout(title_text=f'Covariance Matrix for {selected_county}')
        return fig
    else:
        return dash.no_update

# runn app
if __name__ == '__main__':
    app.run_server(debug=True)