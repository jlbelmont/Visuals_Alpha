import pandas as pd
import numpy as np
from typing import List, Optional
from bokeh.models import ColumnDataSource, Button, Div, HoverTool, RangeTool
from bokeh.plotting import figure, output_notebook, output_file, show
from bokeh.layouts import column, row
from bokeh.io import curdoc
from bokeh.palettes import Category10, Category20

# Function to prepare wedge data for donut plots
def prepare_wedge_data(data: pd.DataFrame, column_name: str, colors: List[str]) -> pd.DataFrame:
    """
    Prepares wedge data for creating donut plots.

    Parameters:
        data (pd.DataFrame): DataFrame containing the data.
        column_name (str): Column name for which wedge data is prepared.
        colors (List[str]): List of colors for each category.

    Returns:
        pd.DataFrame: DataFrame containing start angles, end angles, colors, categories, and sizes.
    """
    counts = data[column_name].value_counts()
    categories = sorted(counts.index)
    sizes = counts.loc[categories].values

    angles = np.linspace(0, 2 * np.pi, len(categories) + 1)
    start_angles = angles[:-1]
    end_angles = angles[1:]

    return pd.DataFrame({
        'start_angle': start_angles,
        'end_angle': end_angles,
        'color': colors,
        column_name: categories,
        'value': sizes
    })

# Placeholder function
def frame() -> None:
    """Placeholder function for frame."""
    pass

# Placeholder function
def video() -> None:
    """Placeholder function for video."""
    pass

# Placeholder function
def scatter() -> None:
    """Placeholder function for scatter."""
    pass

# Placeholder function
def scatter_minimap() -> None:
    """Placeholder function for scatter minimap."""
    pass

# Function to arrange graphs
def arrange(graphs: List) -> None:
    """
    Arrange a list of graphs.

    Parameters:
        graphs (List): List of graph figures to arrange.

    Returns:
        None
    """
    pass  # Implementation needed

# Placeholder function
def display() -> None:
    """Placeholder function for display."""
    pass

# Placeholder function
def html_dash() -> None:
    """Placeholder function for HTML dashboard."""
    pass

# Placeholder function
def latex_dash() -> None:
    """Placeholder function for LaTeX dashboard."""
    pass

# Placeholder function
def extra() -> None:
    """Placeholder function for extra features."""
    pass

# Function to initialize output for Bokeh
def initialize_output(notebook: bool = False, file_name: str = "data_visualization_dashboard.html") -> None:
    """
    Initializes the output for Bokeh visualizations.

    Parameters:
        notebook (bool): If True, outputs to a Jupyter notebook. Defaults to False.
        file_name (str): Filename for HTML output. Defaults to "data_visualization_dashboard.html".

    Returns:
        None
    """
    if notebook:
        output_notebook()
    else:
        output_file(file_name)

# Function to create a ColumnDataSource
def create_column_data_source(data: pd.DataFrame) -> ColumnDataSource:
    """
    Creates a Bokeh ColumnDataSource from a DataFrame.

    Parameters:
        data (pd.DataFrame): The DataFrame to convert.

    Returns:
        ColumnDataSource: Bokeh ColumnDataSource containing the data.
    """
    return ColumnDataSource(data)

# Function to map colors to DataFrame
def map_colors(data: pd.DataFrame, column_name: str, palette: List[str], new_column_name: str = 'color') -> pd.DataFrame:
    """
    Maps colors to a new column in the DataFrame based on values in the specified column.

    Parameters:
        data (pd.DataFrame): The DataFrame to modify.
        column_name (str): The column to map colors from.
        palette (List[str]): List of colors for mapping.
        new_column_name (str): Name of the new column for colors. Defaults to 'color'.

    Returns:
        pd.DataFrame: DataFrame with the new color column added.
    """
    data[new_column_name] = data[column_name].map(lambda cluster: palette[cluster-1])
    return data

# Function to create a donut plot
def create_donut_plot(title: str, wedge_data: pd.DataFrame, column_name: str, radius: float = 0.8) -> figure:
    """
    Creates a donut plot based on provided wedge data.

    Parameters:
        title (str): Title of the plot.
        wedge_data (pd.DataFrame): DataFrame containing wedge data.
        column_name (str): Column name used for the legend.
        radius (float): Radius of the donut. Defaults to 0.8.

    Returns:
        figure: Bokeh figure object containing the donut plot.
    """
    plot = figure(height=350, width=350, title=title, tools='hover',
                  tooltips=f"@{column_name}: @value", x_range=(-1, 1), y_range=(-1, 1))
    plot.wedge(x=0, y=0, radius=radius, start_angle='start_angle', end_angle='end_angle',
               line_color="white", fill_color='color', legend_field=column_name, source=wedge_data)
    plot.circle(x=0, y=0, radius=0.4, fill_color='white')
    plot.axis.visible = False
    plot.grid.grid_line_color = None
    return plot

# Function to create a scatter plot
def create_scatter_plot(data_source: ColumnDataSource, tooltips: List[str], width: int = 800, height: int = 400) -> figure:
    """
    Creates a scatter plot based on the provided data source.

    Parameters:
        data_source (ColumnDataSource): The data source for the plot.
        tooltips (List[str]): Tooltips to display on hover.
        width (int): Width of the plot. Defaults to 800.
        height (int): Height of the plot. Defaults to 400.

    Returns:
        figure: Bokeh figure object containing the scatter plot.
    """
    scatter = figure(
        title="Detailed Scatter Plot",
        tools="pan,wheel_zoom,box_zoom,reset,hover",
        width=width,
        height=height,
        tooltips=tooltips,
        background_fill_color="#efefef"
    )
    scatter.scatter(x='x', y='y', color='color', source=data_source, size=10)
    scatter.add_tools(HoverTool(tooltips=tooltips))
    return scatter

# Function to create a minimap
def create_minimap(data_source: ColumnDataSource, detailed_plot: figure, width: int = 800) -> figure:
    """
    Creates a minimap for the detailed scatter plot.

    Parameters:
        data_source (ColumnDataSource): The data source for the minimap.
        detailed_plot (figure): The detailed plot to be miniaturized.
        width (int): Width of the minimap. Defaults to 800.

    Returns:
        figure: Bokeh figure object containing the minimap.
    """
    minimap = figure(
        width=width,
        height=150,
        tools="",
        toolbar_location=None,
        background_fill_color=detailed_plot.background_fill_color,
        title="Minimap"
    )
    minimap.scatter(x='x', y='y', color='color', source=data_source, size=10)
    minimap.x_range.range_padding = 0
    minimap.ygrid.grid_line_color = None

    # Add RangeTool
    range_tool = RangeTool(x_range=detailed_plot.x_range, y_range=detailed_plot.y_range)
    range_tool.overlay.fill_color = "darkblue"
    range_tool.overlay.fill_alpha = 0.3
    minimap.add_tools(range_tool)

    return minimap

# Function to create a toggle button for the minimap
def create_toggle_button(minimap: figure) -> Button:
    """
    Creates a button to toggle the visibility of the minimap.

    Parameters:
        minimap (figure): The minimap figure to toggle.

    Returns:
        Button: Bokeh Button object for toggling the minimap.
    """
    button = Button(label="Toggle Minimap", button_type="success")
    button.js_on_click(CustomJS(args=dict(minimap=minimap), code="""
        minimap.visible = !minimap.visible;
    """))
    return button

# Function to create a text blurb
def create_text_blurb() -> Div:
    """
    Creates a text blurb for the dashboard.

    Returns:
        Div: Bokeh Div object containing the text blurb.
    """
    return Div(text="""
        <h2>Data Visualization Dashboard</h2>
        <p>This dashboard includes various visualizations to help understand the dataset:</p>
        <ul>
            <li>Donut plots representing <b>clusters</b> and <b>age groups</b>.</li>
            <li>A detailed scatter plot with an interactive minimap.</li>
            <li>Multiple image placeholders for relevant graphics.</li>
            <li>Additional graph placeholders for further analysis.</li>
            <li>A video placeholder for visual content.</li>
        </ul>
        <p>Mathematical formula example: \( E = mc^2 \)</p>
    """, width=800)

# Function to create an image placeholder
def create_image_placeholder(url: str, width: int = 150, height: int = 150) -> Div:
    """
    Creates an image placeholder for the dashboard.

    Parameters:
        url (str): URL of the image.
        width (int): Width of the image. Defaults to 150.
        height (int): Height of the image. Defaults to 150.

    Returns:
        Div: Bokeh Div object containing the image placeholder.
    """
    return Div(text=f"<img src='{url}' width='{width}' height='{height}'/>")

# Main function to set up the dashboard
def setup_dashboard(data: pd.DataFrame) -> None:
    """
    Sets up the dashboard with all visualizations.

    Parameters:
        data (pd.DataFrame): The DataFrame containing the data for visualizations.

    Returns:
        None
    """
    colors = Category10[10]  # Example color palette
    wedge_data = prepare_wedge_data(data, 'Cluster', colors)

    donut_plot = create_donut_plot("Donut Plot of Clusters", wedge_data, 'Cluster')
    
    # Create a ColumnDataSource for the scatter plot
    scatter_data_source = create_column_data_source(data)
    scatter_tooltips = [("X", "@x"), ("Y", "@y"), ("Cluster", "@color")]
    scatter_plot = create_scatter_plot(scatter_data_source, scatter_tooltips)

    # Create minimap for the scatter plot
    minimap = create_minimap(scatter_data_source, scatter_plot)

    # Create the toggle button
    toggle_button = create_toggle_button(minimap)

    # Create text blurb and image placeholders
    text_blurb = create_text_blurb()
    image_placeholder = create_image_placeholder("https://example.com/image.png")

    # Arrange layout
    layout = column(text_blurb, donut_plot, row(scatter_plot, minimap), toggle_button, image_placeholder)

    # Add to document
    curdoc().add_root(layout)
    show(layout)

# # Example usage with dummy data
# if __name__ == "__main__":
#     # Sample data generation
#     sample_data = pd.DataFrame({
#         'x': np.random.rand(100),
#         'y': np.random.rand(100),
#         'Cluster': np.random.randint(1, 4, size=100)  # Clusters 1, 2, or 3
#     })

#     # Run dashboard setup
#     setup_dashboard(sample_data)
