from abc import ABC, abstractmethod


class Renderer(ABC):
    """
    Abstract base class for rendering components.
    """

    @abstractmethod
    def render_button(self, button: "Button") -> None:
        """
        Renders a button using the provided backend.

        :param button: The button to render.
        """
        pass

    @abstractmethod
    def render_textbox(self, textbox: "TextBox") -> None:
        """
        Renders a textbox using the provided backend.

        :param textbox: The textbox to render.
        """
        pass

    @abstractmethod
    def render_label(self, label: "Label") -> None:
        """
        Renders a label using the provided backend.

        :param label: The label to render.
        """
        pass
