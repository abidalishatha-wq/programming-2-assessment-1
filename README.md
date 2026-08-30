# Assessment 1: "Digital Menagerie" Refactoring Report

**Student Name:** Shatha Abid Ali
**Student ID:** 20251597

---

## 1. Analysis of Legacy Code

Identify and explain the most significant flaws you discovered in `menagerie_legacy.py` (3–4 well-explained points). For each flaw, do not just describe *what* it is — explain *why* it is a problem from a software-engineering perspective by naming the principle or quality it undermines (e.g. maintainability, scalability, robustness, testability, or a named principle such as the Open/Closed Principle or separation of concerns).

**Flaw 1:**  

[Name the flaw, then explain the engineering consequence and the principle it violates.]

**Flaw 2:**

[Your second flaw and its consequence.]

**Flaw 3:**

[Your third flaw and its consequence.]

**Flaw 4 (optional):**

[A further significant flaw.]

---

## 2. Design Rationale for Refactored Solution

### 2.1. Design Sketch

Insert your class diagram or design sketch here (an image, or a clear text outline). It should show your classes — with the names you chose — their key attributes and methods, and the relationships between them (inheritance and composition). This should match what you actually built in Task 2.

[Your diagram / outline here.]

### 2.2. Class Structure

The brief does not prescribe class names. Give a brief overview of each class you designed, using your own names, and explain its single responsibility within the system.

**Animal-hierarchy Abstract Base Class (your chosen name):**

[Explain the purpose of the ABC and the interface (abstract methods) it defines.]

**Concrete animal subclasses (lion, snake, parrot — your chosen names):**

[Explain how these inherit from your ABC and implement its interface, and how this removes the original `if/elif` species logic.]

**Container class (your chosen name):**

[Describe the responsibilities of your container class and its public interface.]

**Controller class (your chosen name):**

[Describe the role of your controller class as the replacement for the global state and free functions, including how it provides equivalents of every legacy operation — not only move_animal.]

### 2.3. Designing for Change (Extensibility)

The brief states two changes the system must support: (a) adding a new species (penguins — a design thought experiment, not an implementation task), and (b) moving an animal between containers (move_animal, which you have implemented).

[Explain how your design makes each of these changes easy, and which classes would — and would not — need to be modified. Refer to the relevant design principle.]

---

## 3. Data Structure Selection

### 3.1. Storing Containers in the Controller

[State and justify your choice of structure for holding the containers. Explain what the container-ID key buys you compared with the original approach.]

### 3.2. Holding Animals in a Container (list vs. set)

**Which data structure did you choose?**

[State your choice: list or set.]

**Justify your choice.**

[Evaluate the trade-offs — ordering, duplicate handling, lookup cost, and any hashability/equality implications for your Animal objects — and explain why your choice suits this scenario better than the alternative.]

### 3.3. Storing Each Animal's Feeding History

**Which data structure did you choose (e.g. list, deque, dict)?**

[State your choice.]

**Justify your choice.**

[Evaluate the trade-offs — ordering, how the history will be read (most-recent lookup vs full iteration), and whether it should be capped or pruned — and explain why your choice suits this scenario.]

---

## 4. Testing Summary

Briefly describe the unit tests you wrote and what behaviour each one verifies (e.g. health is capped on feeding, an animal moves correctly between containers, each species speaks correctly).

[Your testing summary here.]
