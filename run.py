from __future__ import annotations

import logging

import distributed
import holoviews as hv
import panel as pn
from holoviews import opts as hvopts

import thalassa.ui
from thalassa.utils import setup_logging

# configure logging
setup_logging()

# load bokeh
hv.extension("bokeh")
pn.extension(sizing_mode="scale_width")

# Set some defaults for the visualization of the graphs
hvopts.defaults(
    hvopts.Curve(  # pylint: disable=no-member
        height=500,
        responsive=True,
        show_title=True,
        tools=["hover"],
        active_tools=["pan", "wheel_zoom"],
        align="end",
    ),
    hvopts.Image(  # pylint: disable=no-member
        # Don't set both height and width, or the UI will not be responsive!
        # width=800,
        height=500,
        responsive=True,
        show_title=True,
        tools=["hover"],
        active_tools=["pan", "wheel_zoom"],
        align="end",
    ),
    hvopts.Layout(toolbar="right"),  # pylint: disable=no-member
)


ui = thalassa.ui.ThalassaUI()

# https://panel.holoviz.org/reference/templates/Bootstrap.html
bootstrap = pn.template.BootstrapTemplate(
    site="example.com",
    title="Thalassa",
    # logo="thalassa/static/logo.png",
    # favicon="thalassa/static/favicon.png",
    sidebar=[ui.sidebar],
    sidebar_width=350,  # in pixels! must be an integer!
    # main_max_width="1050px", #  must be a string!
    main=[ui.main],
)

_ = bootstrap.servable()
