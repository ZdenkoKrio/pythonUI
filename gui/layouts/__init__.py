"""
This package provides layout components for arranging and managing child components
in various configurations.

Layouts are responsible for defining how child components are positioned and sized
within their parent view. They allow developers to build complex and responsive UI
structures by combining different layout strategies.

Available Layouts:
- HorizontalStack: Arranges components horizontally.
- VerticalStack: Arranges components vertically.
- GridStack: Arranges components in a grid.
- ZStack: Stacks components on top of each other.
- HorizontalList: A horizontal list for managing items.
- VerticalList: A vertical list for managing items.

Layouts are designed to be flexible and composable, allowing nested and dynamic
structures.

Usage:
    from components.layouts import HorizontalStack, VerticalStack, GridStack, ZStack, HorizontalList, VerticalList

    # Horizontal Layout
    hstack = HorizontalStack(x=0, y=0, width=400, height=50)
    hstack.add_component(Label(x=0, y=0, width=100, height=50, text="Name"))
    hstack.arrange()

    # Vertical Layout
    vstack = VerticalStack(x=0, y=0, width=400, height=300)
    vstack.add_component(Label(x=0, y=0, width=400, height=50, text="Header"))
    vstack.arrange()

    # Horizontal List
    hlist = HorizontalList(x=0, y=0, width=400, height=50, item_width=100)
    hlist.add_item(Label(x=0, y=0, width=100, height=50, text="Item 1"))

    # Vertical List
    vlist = VerticalList(x=0, y=0, width=400, height=0, item_height=30)
    vlist.add_item(Label(x=0, y=0, width=400, height=30, text="Item 1"))
"""

from .layout import Layout
from .horizontal_stack import HorizontalStack
from .vertical_stack import VerticalStack
from .grid_stack import GridStack
from .zstack import ZStack
from .base_list import BaseList
from .horizontal_list import HorizontalList
from .vertical_list import VerticalList

__all__ = [
    "Layout",
    "HorizontalStack",
    "VerticalStack",
    "GridStack",
    "ZStack",
    "BaseList",
    "HorizontalList",
    "VerticalList",
]
