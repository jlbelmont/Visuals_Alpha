from function_config import *

def prepare_wedge_data(column_name, colors, data):
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
    
def frame():
    pass

def video():
    pass

def scatter():
    pass

def scatter_minimap():
    pass

def arrange(graphs: List):
    pass

def display():
    pass

def html_dash():
    pass

def latex_dash():
    pass

def extra():
    pass

def initialize_output(notebook: bool = False, file_name: str = "data_visualization_dashboard.html"):
    if notebook:
        output_notebook()
    else:
        output_file(file_name)

def create_column_data_source(data: pd.DataFrame) -> ColumnDataSource:
    return ColumnDataSource(data)

def map_colors(data: pd.DataFrame, column_name: str, palette: list, new_column_name: str = 'color') -> pd.DataFrame:
    data[new_column_name] = data[column_name].map(lambda cluster: palette[cluster-1])
    return data

def prepare_wedge_data(data: pd.DataFrame, column_name: str, colors: list) -> pd.DataFrame:
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

def create_donut_plot(title: str, wedge_data: pd.DataFrame, column_name: str, radius: float = 0.8) -> figure:
    plot = figure(height=350, width=350, title=title, tools='hover',
                  tooltips=f"@{column_name}: @value", x_range=(-1, 1), y_range=(-1, 1))
    plot.wedge(x=0, y=0, radius=radius, start_angle='start_angle', end_angle='end_angle',
               line_color="white", fill_color='color', legend_field=column_name, source=wedge_data)
    plot.circle(x=0, y=0, radius=0.4, fill_color='white')
    plot.axis.visible = False
    plot.grid.grid_line_color = None
    return plot

def create_scatter_plot(data_source: ColumnDataSource, tooltips: list, width: int = 800, height: int = 400) -> figure:
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

def create_minimap(data_source: ColumnDataSource, detailed_plot: figure, width: int = 800) -> figure:
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

def create_toggle_button(minimap: figure) -> Button:
    button = Button(label="Toggle Minimap", button_type="success")
    button.js_on_click(CustomJS(args=dict(minimap=minimap), code="""
        minimap.visible = !minimap.visible;
    """))
    return button

def create_text_blurb() -> Div:
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

def create_image_placeholder(url: str, width: int = 150, height: int = 150) -> Div:
    return Div(text=f'<img src="{url}" alt="Image" width="{width}" height="{height}">', width=width, height=height)

def create_dashboard_layout(text_blurb: Div, donut_plots: row, scatter_plot: figure, minimap: figure,
                            toggle_button: Button, additional_plots: row, image_placeholders: list, video_url: str):
    video_div = Div(text=f'<video width="320" height="240" controls><source src="{video_url}" type="video/mp4">Your browser does not support the video tag.</video>', width=320, height=240)
    layout = column(
        text_blurb,
        row(*image_placeholders),
        donut_plots,
        additional_plots,
        scatter_plot,
        minimap,
        toggle_button,
        video_div,
        sizing_mode='stretch_both'
    )
    return layout

def build_dashboard(data: pd.DataFrame):
    initialize_output()

    # Prepare data
    source = create_column_data_source(data)
    cluster_colors = Category10[3]
    data = map_colors(data, 'c', cluster_colors)
    
    cluster_wedge_data = prepare_wedge_data(data, 'c', cluster_colors)
    age_colors = Category20[len(data['age'].unique())]
    age_wedge_data = prepare_wedge_data(data, 'age', age_colors)

    # Create plots
    cluster_plot = create_donut_plot("Donut Plot of Clusters", cluster_wedge_data, 'c')
    age_plot = create_donut_plot("Donut Plot of Age Groups", age_wedge_data, 'age')
    scatter_plot = create_scatter_plot(source, TOOLTIPS)
    minimap = create_minimap(source, scatter_plot)
    toggle_button = create_toggle_button(minimap)

    # Create placeholders and blurb
    text_blurb = create_text_blurb()
    image_placeholders = [create_image_placeholder("https://via.placeholder.com/150") for _ in range(3)]

    # Additional plots
    additional_plot_1 = figure(height=350, width=350, title="Additional Graph 1")
    additional_plot_2 = figure(height=350, width=350, title="Additional Graph 2")

    # Layout and rendering
    layout = create_dashboard_layout(
        text_blurb,
        row(cluster_plot, age_plot),
        scatter_plot,
        minimap,
        toggle_button,
        row(additional_plot_1, additional_plot_2),
        image_placeholders,
        video_url="your_video.mp4"
    )

    curdoc().add_root(layout)
    show(layout)
