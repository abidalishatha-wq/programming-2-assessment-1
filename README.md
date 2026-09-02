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


## 2. Design Rationale for Refactored Solution

### 2.1. Design Sketch
                              Animal (ABC)
                        -------------------------
                          -  _animal_id : int
                           _ name : str
                            - _health : int
                            - _feeding_history
                        ----------------------------
                            + animal_id
                            + health
                            + feeding_history
                            + feed()
                            + speak() [abstract]
                            + __str__()
                         -----------------------------
                                    ^
                                    |
                                inheritance
                +-------------------------------------------------
                |                   |                     |
            +--------             +------             +--------
            Lion                  snak                  Parrot
          + speak()               + speak()             + speak()

                        +------------------------------
                               Enclousur 
                              - enclosure_id : str        
                            | - _animals : list (Animal)  
                        +------------------------------- 
                           + animlas
                           + add_animal()
                           + remove_animal()
                           + find_animal()
                           + contains
                           + __str__()
                        +--------------------------------
                                       |
                                       |  contains   0..* 
                                       |
                                       V
                                     Animal 

                        +-------------------------------
                        
                                 MenagerieManager
                        +-------------------------------
                                - _enclosures : dict
                                - _animals_by_id : dict 
                                - _next_animal_id : int 
                        +--------------------------------
                                + add_enclosure() 
                                + get_enclosure() 
                                + add_animal() 
                                + find_animal()
                                + feed_animal()
                                + roll_call()
                                + move_animal() 
                        +--------------------------------
                                     |
                                     |    manages
                                     |
                                     V
                                  Enclosure





### 2.2. Class Structure
Animal-hierarchy Abstract Base Class (Animal)

I designed Animal as an Abstract Base Class (ABC) using Python's abc module. Its single responsibility is to define the common state and behaviour shared by all animal species in the system.

The class stores the animal's unique ID, name, and health. It also defines the speak() method using @abstractmethod. This prevents the Animal class from being instantiated directly and ensures that every concrete animal subclass must provide its own implementation of speak().

This design supports abstraction because common animal features are defined once in the base class, while species-specific behaviour is delegated to the subclasses. It also provides a consistent interface that allows the rest of the system to work with different animal types in the same way.

As an additional enhancement, I implemented a validated health property. Health values must remain between 0 and 100. Invalid values are rejected, which protects the internal state of each animal and improves encapsulation and robustness.

The Animal class also implements __str__() to provide a clear and consistent text representation of animal objects. This avoids repeating display logic in every concrete species class and improves code reuse and readability.

Overall, the Animal class provides the shared foundation for the animal hierarchy while ensuring that species-specific behaviour is implemented only where it belongs.

Concrete Animal Subclasses: Lion, Snake, and Parrot

I implemented Lion, Snake, and Parrot as concrete subclasses of Animal.
Each class inherits the shared state and behaviour from Animal and implements its own version of the speak() method:

Lion   -> "roars"
Snake  -> "hisses"
Parrot -> "squawks"

This demonstrates inheritance because the subclasses reuse functionality defined in the base class, and polymorphism because the same speak() interface produces different behaviour depending on the actual animal object.
The rest of the system can simply call:
animal.speak()
without checking the species using if/elif.
This directly fixes a weakness in the legacy program, where cage_roll_call() contains species-specific if/elif branches. The new design therefore supports the Open/Closed Principle.

Container Class: Enclosure

I designed Enclosure to represent one container that can hold zero or more Animal objects. Its single responsibility is to manage the animals currently located inside one enclosure.
The class stores a unique enclosure_id and keeps its Animal objects in a private _animals collection.

Its public interface includes:

animals
add_animal()
remove_animal()
find_animal()
contains()
__str__()

add_animal() adds an animal while preventing duplicate animal IDs. remove_animal() removes and returns an Animal object, which is useful for transferring the same object during move_animal().
find_animal() searches for an animal by ID, while contains() provides a simple Boolean membership check.
The animals property returns a tuple rather than exposing the internal list directly. This improves encapsulation because outside code can inspect the enclosure without directly changing its private collection.
The class also implements __str__() so both populated and empty enclosures can be represented clearly. Supporting an empty enclosure is important because an enclosure may contain zero animals after an animal is moved out.
This design demonstrates composition, because an Enclosure contains zero or more Animal objects.


Controller Class: MenagerieManager

I designed MenagerieManager as the central controller for the application. Its responsibility is to coordinate the overall menagerie while delegating animal-specific behaviour to Animal objects and enclosure-specific behaviour to Enclosure.
The controller replaces the global variables and free functions used in the legacy script. The original program stores its state in global variables such as animals_db, next_animal_id, and cages. 
The MenagerieManager instead owns:
_enclosures
_animals_by_id
_next_animal_id
Its public interface includes:
add_enclosure()
get_enclosure()
add_animal()
find_animal()
feed_animal()
roll_call()
move_animal()
add_animal() provides the object-oriented equivalent of the original add operation. feed_animal() replaces the legacy feeding function, and roll_call() provides the equivalent of cage_roll_call().
The legacy feeding function scans the animal list sequentially to find a matching ID. In the refactored system, the controller can maintain an animal-ID dictionary to support average-case O(1) lookup.
This design removes global mutable state, improves encapsulation, reduces coupling, and gives the application a clear separation of responsibilities.


### 2.3. Designing for Change (Extensibility)

The design supports two important changes: adding a new species and moving an animal between enclosures.
Adding a Penguin
The original program determines species behaviour using an if/elif chain. Therefore, adding a new species would require modifying existing code. 
In the refactored design, a new species can be introduced by creating another subclass of Animal, for example:
class Penguin(Animal):
    species_name = "penguin"

    def speak(self):
        return "honks"
The existing Lion, Snake, Parrot, Enclosure, and roll-call logic would not need to be modified.
This follows the Open/Closed Principle because the application is open for extension through new subclasses while existing classes remain unchanged.
Moving an Animal
The move_animal() operation belongs to MenagerieManager because moving an animal affects two enclosures.
The controller:
1.	identifies the animal; 
2.	validates the source enclosure; 
3.	validates the destination enclosure; 
4.	removes the animal from the source; 
5.	adds the same Animal object to the destination. 
After the operation, the source no longer contains the animal and the destination does contain it.
This keeps both containers in a correct state and preserves the same Animal object rather than creating a duplicate.


## 3. Data Structure Selection

### 3.1. Storing Containers in the Controller

I chose a Python dictionary to store Enclosure objects in MenagerieManager.
The structure is conceptually:
{
    "c1": enclosure1,
    "c2": enclosure2,
    "c3": enclosure3
}
Each unique enclosure ID is used as the dictionary key.
This choice matches the way the application accesses enclosures. Most operations already know the enclosure ID and need to retrieve the corresponding object directly.
Dictionary lookup is average-case:
O(1)
By comparison, storing enclosures in a list would normally require an O(n) search to locate a specific ID.
The dictionary also naturally represents the relationship:
unique enclosure ID -> Enclosure object
and prevents two values from occupying the same key.
This makes the dictionary more appropriate than a list for controller-level enclosure management.


### 3.2. Holding Animals in a Container (list vs. set)

I chose a Python:
list
to hold Animal objects inside each Enclosure.
Justification
A list preserves insertion order, which is useful when displaying enclosure contents or performing a roll call because the output remains predictable.
Appending an animal to the end of a Python list is normally amortised:
O(1)
Finding or removing an animal by ID requires an:
O(n)
search through that enclosure.
However, each individual enclosure is expected to contain a relatively small number of animals, so this trade-off is acceptable.
Duplicate animal IDs are controlled through add_animal() rather than relying on the collection itself.
I considered using a set. A set would provide average-case O(1) membership checking, but it would require carefully designed:
__eq__()
and:
__hash__()
methods on Animal.

If Animal objects were stored in a set, equality and hashing should be based on an immutable value such as animal_id.
Mutable attributes such as health or name should not be used for hashing because changing a value that contributes to an object's hash after insertion can cause incorrect set behaviour.
A set would therefore provide faster membership lookup but introduce additional equality and hashing complexity and would not provide the same predictable ordering.
For this application, predictable order, simple iteration, and maintainability are more valuable, so a list is the better choice.

### 3.3. Storing Each Animal's Feeding History

Which data structure did you choose?
I chose a Python:
list
containing timestamp values for each feeding event.
For example, the internal structure can be represented as:

self._feeding_history = []

Each time feed() is called, the current timestamp is appended to this list.
Justification
Feeding history is naturally chronological, so preserving order is important.
A list provides efficient append operations, normally amortised:
O(1)
It also allows the complete feeding history to be processed in chronological order.
The most recent feeding event can be retrieved efficiently using the final item:

feeding_history[-1]
which is O(1).

I considered using a dictionary, but feeding events do not currently require key-based access, so a dictionary would add unnecessary complexity.
I also considered using deque. A deque would be useful if the business later decided to retain only a fixed number of recent feeding events.
For example:
deque(maxlen=100)
could automatically discard the oldest event when the limit is reached.
However, the current requirements do not specify that the history should be capped or pruned. Retaining the full chronological history may also be useful for future reporting.
Therefore, a list is the clearest and most appropriate structure for the current requirement.











