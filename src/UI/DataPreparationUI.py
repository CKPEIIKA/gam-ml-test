from dataclasses import dataclass
from typing import Any

import ipywidgets as iw
from Managers import DataManager

from .CustomWidgets.DataPreparation import (
    DataGridWidget,
    DataPlotWidget,
    UploadFileWidget,
)


@dataclass
class DataFile:
    """The data file container."""

    file: Any = None
    headers: Any = None


class DataPreparationUI(iw.VBox):
    """UI widgets for data preperation."""

    data_file = DataFile()
    manager = DataManager(data=data_file)

    widget_children = [
        UploadFileWidget(manager=manager),
        DataGridWidget(manager=manager),
        DataPlotWidget(manager=manager),
    ]
    widget_titles = ["Upload File", "Show Data Grid", "Show Data Plot"]
    widget = iw.Accordion(children=widget_children)
    for i, title in enumerate(widget_titles):
        widget.set_title(i, title)

    def __init__(self, **kwargs) -> None:
        """Initialize the main widget."""
        super().__init__(children=[self.widget], **kwargs)