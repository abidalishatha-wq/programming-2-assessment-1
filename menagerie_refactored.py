"""
Digital Menagerie Refactored Solution

Author: Shatha Abid Ali
"""

from abc import ABC, abstractmethod
"""Object-oriented refactor of the Digital Menagerie."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for all animals."""

    def __init__(self, animal_id, name, health=100):
        """Create an animal with an ID, name, and health."""
        self._animal_id = animal_id
        self.name = name
        self._health = health

    @property
    def animal_id(self):
        """Return the animal ID."""
        return self._animal_id

    @property
    def health(self):
        """Return the current health."""
        return self._health

    @abstractmethod
    def speak(self):
        """Return the animal's distinctive sound."""
        pass