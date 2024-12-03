from ...core import View, Event, EventType
from ..interactive_component import InteractiveComponent
from typing import Dict, Callable, Optional


class Form(View[None], InteractiveComponent):
    """
    A form component for managing grouped input components.
    """

    def __init__(self, x: int, y: int, width: int, height: int):
        """
        Initializes a form component.

        :param x: The x-coordinate of the form.
        :param y: The y-coordinate of the form.
        :param width: The width of the form.
        :param height: The height of the form.
        """
        super().__init__(x, y, width, height)
        self._fields: Dict[str, View] = {}  # Field name mapped to a View component
        self._on_submit: Optional[Callable[[Dict[str, any]], None]] = None

    def add_field(self, name: str, component: View) -> 'Form':
        """
        Adds a field to the form.

        :param name: The field name.
        :param component: The component associated with the field.
        :return: Self for chaining.
        """
        self._fields[name] = component
        return self

    def remove_field(self, name: str) -> 'Form':
        """
        Removes a field from the form.

        :param name: The field name.
        :return: Self for chaining.
        """
        if name in self._fields:
            del self._fields[name]
        return self

    def get_values(self) -> Dict[str, any]:
        """
        Retrieves the current values of all fields.

        :return: A dictionary of field names and their current values.
        """
        return {name: field.state for name, field in self._fields.items()}

    def set_on_submit(self, callback: Callable[[Dict[str, any]], None]) -> None:
        """
        Sets the callback to be executed on form submission.

        :param callback: The callback function.
        """
        self._on_submit = callback

    def submit(self) -> None:
        """
        Submits the form and executes the on_submit callback.
        """
        if self._on_submit:
            self._on_submit(self.get_values())

    def reset(self) -> None:
        """
        Resets all fields to their default state.
        """
        for field in self._fields.values():
            if hasattr(field, "state"):
                field.state = field.state.__class__()  # Reset to default value

    def handle_event(self, event: Event) -> None:
        """
        Handles events for the form.

        :param event: The event to handle.
        """
        if event.is_type(EventType.CLICK):
            # Check if submission button is clicked
            if "submit" in event.data:
                self.submit()

    def render(self, renderer: 'Renderer') -> None:
        """
        Renders the form and its fields.

        :param renderer: The renderer responsible for drawing the form.
        """
        self.apply_modifiers()
        renderer.render_form(self)
        for field in self._fields.values():
            field.render(renderer)
