import numpy as np
import pandas as pd

from bokeh.io import output_notebook, show, output_file, save, push_notebook, curdoc
from bokeh.plotting import figure, curdoc, gridplot
from bokeh.models import (DateRangeSlider, ColumnDataSource, HoverTool, CustomJS, 
                          Slider, Range1d, FactorRange, Legend, Label, 
                          LabelSet, ColorBar, NumeralTickFormatter, 
                          DatetimeTickFormatter, Toggle, CheckboxGroup, 
                          RadioButtonGroup, TextInput, Button, Div, Tabs, Panel)
from bokeh.layouts import row, column, gridplot, layout
from bokeh.palettes import HighContrast3, Viridis256, Category20, Inferno256, Cividis256, Turbo256
from bokeh.transform import factor_cmap, dodge, linear_cmap, log_cmap
from bokeh.events import DoubleTap, MouseMove, PanStart, Tap
from bokeh.tile_providers import get_provider, Vendors
from bokeh.embed import components, file_html
from bokeh.resources import CDN
from bokeh.themes import Theme
from bokeh.application import Application
from bokeh.application.handlers import FunctionHandler


class Dashboard():
    
    def __init__(self) -> None:
        pass

def create_dashboard():
    pass

def grab_data(tuple):
    pass

def search():
    pass

def standardize_df():
    pass

