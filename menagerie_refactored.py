"""Object-oriented refactor of the Digital Menagerie."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for all animals."""

    species_name = "animal"

    def __init__(self, animal_id, name, health=100):
        """Create an animal with an ID, name, and health."""
        self._animal_id = animal_id
        self.name = name

        # Use the property setter to validate health.
        self._health = 100
        self.health = health

    @property
    def animal_id(self):
        """Return the animal's unique ID."""
        return self._animal_id

    @property
    def health(self):
        """Return the current health value."""
        return self._health

    @health.setter              #controls changes to health
    def health(self, value):
        """Set health while keeping it between 0 and 100."""
        if not 0 <= value <= 100:
            raise ValueError("Health must be between 0 and 100.")

        self._health = value

    @abstractmethod
    def speak(self):
        """Return the animal's distinctive sound."""
        pass

    def __str__(self):     #this help how the animal prints
        """Return a readable description of the animal."""
        return (
            f"{self.name} the {self.species_name} "
            f"(ID {self.animal_id}, health {self.health})"
        )


class Lion(Animal):
    """Represent a lion."""

    species_name = "lion"

    def speak(self):        # Polymorphism(Each species has the same method)


        """Return the distinctive lion sound."""
        return "roars"


class Snake(Animal):
    """Represent a snake."""

    species_name = "snake"

    def speak(self):
        """Return the distinctive snake sound."""
        return "hisses"


class Parrot(Animal):
    """Represent a parrot."""

    species_name = "parrot"

    def speak(self):
        """Return the distinctive parrot sound."""
        return "squawks"
class Enclosure:
    """Container that stores zero or more Animal objects."""

    def __init__(self, enclosure_id):
        """Create an empty enclosure with a unique ID."""
        if not enclosure_id.strip():
            raise ValueError("Enclosure ID cannot be empty.")

        self.enclosure_id = enclosure_id
        self._animals = []

    @property
    def animals(self):
        """Return the animals as a read-only tuple."""
        return tuple(self._animals)

    def add_animal(self, animal):
        """Add an animal to the enclosure."""
        if self.contains(animal.animal_id):
            raise ValueError(
                f"Animal ID {animal.animal_id} is already "
                f"in enclosure {self.enclosure_id}."
            )

        self._animals.append(animal)

    def remove_animal(self, animal_id):
        """Remove and return an animal using its ID."""
        for index, animal in enumerate(self._animals):
            if animal.animal_id == animal_id:
                return self._animals.pop(index)

        raise KeyError(
            f"Animal ID {animal_id} is not in "
            f"enclosure {self.enclosure_id}."
        )

    def find_animal(self, animal_id):
        """Return an animal by ID, or None if it is absent."""
        for animal in self._animals:
            if animal.animal_id == animal_id:
                return animal

        return None

    def contains(self, animal_id):
        """Return True if the animal is in this enclosure."""
        return self.find_animal(animal_id) is not None

    def __str__(self):
        """Return a readable description of the enclosure."""
        if not self._animals:
            return f"Enclosure {self.enclosure_id}: empty"

        contents = ", ".join(
            str(animal) for animal in self._animals
        )

        return (
            f"Enclosure {self.enclosure_id}: "
            f"{contents}"
        )
    