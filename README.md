# Assessment 1: "Digital Menagerie" Refactoring Report

**Student Name:** Shatha Abid Ali
**Student ID:** 20251597

---

## 1. Analysis of Legacy Code

The legacy script programm is worked for a small amount of data and successfully manages a small collection of animals, but its design creates several software-engineering problems that reduce maintainability, scalability, extensibility, and testability. This current structure would become harder to manage as the zoo system grows or new requirements are introduced.


**Flaw 1:**.  Global Mutable State

The legacy program stores important application data in global variables such as animals_db, next_animal_id, and cages. Functions such as add_animal() directly depend on and modify this shared state.

This  program creates weakens encapsulation by tight coupling between different parts of the program . It also makes testing and debugging more difficult because one function can change data that is used by another function.

Planned solution: The refactored design will introduce a MenagerieManager controller class that owns and manages the application state. This removes the need for global variables and improves maintainability, testability, and separation of responsibilities.

**Flaw 2:**.   Animals Are Stored as Dictionaries

legacy program, make each animal is represented as a dictionary containing values such as id, name, species, health, and cage_id.
This separates animal data from animal behaviour. For example, feeding and speaking behaviour are implemented in separate functions rather than belonging to the animal itself. Every function must also know the correct dictionary keys, which increases the risk of errors and reduces cohesion.

Planned solution: The refactored system will replace animal dictionaries with an abstract Animal class and concrete subclasses such as Lion, Snake, and Parrot. This keeps related data and behaviour together and creates a clearer Object-Oriented structure (OOS).

**Flaw 3:**.  Species Logic Violates the Open/Closed Principle

The legacy program cage_roll_call() function uses an if/elif chain to determine the sound made by each species. For example, the function explicitly checks whether an animal is a lion, snake, or parrot.
This creates an architectural problem because adding a new species, such as a penguin, would require modifying the existing roll-call function. This violates the Open/Closed Principle, which states that software should be open for extension but closed to unnecessary modification.

Planned solution: The refactored system will use polymorphism. The abstract Animal class will define a speak() interface, and every concrete species will implement its own version. The controller can then call animal.speak() without checking the species using if/elif.

**Flaw 4:**.  Inefficient O(n) Searching

The legacy program used feed_animal() function searches through animals_db one animal at a time until it finds the requested ID. The roll-call operation also searches through the full animal collection to find animals belonging to a particular cage.
These operations use O(n) searching, meaning that the amount of work increases as more animals are added. Although this is acceptable for a very small system, it reduces scalability.
Planned solution: The refactored controller will use dictionaries for ID-based access, including a dictionary of enclosures keyed by unique enclosure ID. This provides average-case O(1) lookup and gives the system a more efficient and scalable structure.

