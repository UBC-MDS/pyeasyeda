import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pytest
from pytest import raises
from pyeasyeda import pyeasyeda as pye
    
def test_birds_eye_view_error():
    """tests birds_eye_view handling of erroneous inputs"""
    
    #Load toy data set
    data = {'product_name': 
            ['laptop', 'printer', 'tablet', 'laptop', 'printer', 'laptop'],
            'price': [1200, 150, 300, 450, 200, 1000],
            'weight':[200, 500, 700, 100, 1000, 800]}
    
    eda = pd.DataFrame(data)
    
    #Section of invalid inputs
    with raises(TypeError):
        pye.birds_eye_view(1)

    with raises(TypeError):
        pye.birds_eye_view(eda, var_list="list")

    with raises(TypeError):
        pye.birds_eye_view(eda, n="2")
    
    with raises(TypeError):
        pye.birds_eye_view(eda, var_list=['notreal'])
    
def test_birds_eye_view_outputs():
    """tests birds_eye_view vizualization outputs"""
    
    #Load toy data set
    data = {'product_name': 
            ['laptop', 'printer', 'tablet', 'laptop', 'printer', 'laptop'],
            'price': [1200, 150, 300, 450, 200, 1000],
            'weight':[200, 500, 700, 100, 1000, 800],
            'version':[400, 600, 200, 700, 2000, 100]}
    
    eda = pd.DataFrame(data)
    
    viz = pye.birds_eye_view(eda)
    viz_custom = pye.birds_eye_view(eda, var_list=['price','weight','product_name'])
    
    # Test birds_eye_view with default inputs
    
    # Test if each different vizualization type generated, that the correct amount generated, and that it saved correctly - default
    assert (
        type(viz["histograms"]) == list
    ), "Histogram objects should be stored in list of figures"
    assert (
        type(viz["bar_charts"]) == list
    ), "Bar Chart objects should be stored in list figures"
    assert (
            str(type(viz["heatmap"])) == "<class 'matplotlib.axes._subplots.AxesSubplot'>"

    ), "Heatmap should be stored as a single matplotlib figure"
    
    assert (
        len(viz) == 3
    ), "Number of items in the viz dictionary should be 3" 
    assert (
        len(viz["histograms"]) == 3
    ), "Number of items in the 'histograms' key should be 3"
    assert (
        len(viz["bar_charts"]) == 1
    ), "Number of items in the 'bar_charts' key should be 1" 
    assert (
        "heatmap" in viz.keys()
    ), "There should be a 'heatmap' key in the viz dictionary"

    # Test if each different vizualization type generated, that the correct amount generated, and that it saved correctly - custom
    assert (
        type(viz_custom["histograms"]) == list
    ), "Histogram objects should be stored in list of figures"
    assert (
        type(viz_custom["bar_charts"]) == list
    ), "Bar Chart objects should be stored in list figures"
    assert (
            str(type(viz_custom["heatmap"])) == "<class 'matplotlib.axes._subplots.AxesSubplot'>"

    ), "Heatmap should be stored as a single matplotlib figure"
    
    assert (
        len(viz_custom) == 3
    ), "Number of items in the viz dictionary should be 3" 
    assert (
        len(viz_custom["histograms"]) == 2
    ), "Number of items in the 'histograms' key should be 2"
    assert (
        len(viz_custom["bar_charts"]) == 1
    ), "Number of items in the 'bar_charts' key should be 1" 
    assert (
        "heatmap" in viz_custom.keys()
    ), "There should be a 'heatmap' key in the viz dictionary"

    