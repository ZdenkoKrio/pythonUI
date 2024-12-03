from ...core import View, Renderer
from ..label import Label
from ...utils import log_event
from typing import List


class Tab:
    """
    Represents a single tab.
    """

    def __init__(self, label: Label, content: View):
        self.label = label
        self.content = content


class Tabs(View[None]):
    """
    A tab component for managing multiple views.
    """

    def __init__(self, x: int, y: int, width: int, height: int, tabs: List[Tab]):
        super().__init__(x, y, width, height)
        self._tabs = tabs
        self._selected_tab = 0

    @log_event
    def render(self, renderer: Renderer) -> None:
        """
        Renders the tabs and the content of the selected tab.

        :param renderer: The renderer responsible for drawing the tabs.
        """
        self.apply_modifiers()
        renderer.render_tabs(self)

        # Render tab labels
        for index, tab in enumerate(self._tabs):
            if index == self._selected_tab:
                tab.label.set_text(f"[{tab.label.state}]")  # Highlight selected tab
            tab.label.render(renderer)

        # Render content of the selected tab
        self._tabs[self._selected_tab].content.render(renderer)

    def select_tab(self, index: int) -> 'Tabs':
        """
        Selects a tab by index.

        :param index: The index of the tab to select.
        :return: Self for chaining.
        """
        if 0 <= index < len(self._tabs):
            self._selected_tab = index
        return self
