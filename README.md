# 🚗 Python Car Builder Using Abstract Factory Pattern

A beginner-friendly and fully structured Python example of the **Abstract Factory Design Pattern** to simulate car production across different brands like **Benz** and **BMW**.

This project clearly shows how **families of related objects** (like SUVs and Coupes) can be produced using an abstract factory architecture — making it an ideal resource for students, interview prep, or developers learning scalable design patterns.

---

## 💡 What Is Abstract Factory?

> The Abstract Factory Pattern provides an interface to create **families of related objects** without specifying their concrete classes.

In this project:

* The *family* is a car brand (e.g., Benz, BMW)
* The *products* in each family are two types: **SUV** and **Coupe**

---

## 🧱 Core Components of This Pattern

This project demonstrates all **four essential building blocks** of the Abstract Factory pattern:

| Component             | Purpose                                            | Code Example             |
| --------------------- | -------------------------------------------------- | ------------------------ |
| **Abstract Factory**  | Defines methods for creating each abstract product | `Car` interface          |
| **Concrete Factory**  | Implements creation of specific product families   | `Benz`, `Bmw`            |
| **Abstract Products** | Base classes/interfaces for each type of product   | `Suv`, `Coupe`           |
| **Concrete Products** | Specific implementations of each product type      | `Gla`, `Cls`, `X1`, `M2` |

---

## 🧠 Why Is This an Abstract Factory Example?

✅ **Brand-based object grouping:** You can generate a full set of car types (SUV + Coupe) by just choosing a brand.

✅ **Interface separation:** The client code doesn’t depend on any real class (like `Gla` or `X1`), only on abstract interfaces like `Suv` or `Coupe`.

✅ **Easy to scale:** Want to add a new brand? Just create a new factory and its car models — no core logic changes required.

✅ **SOLID principles in action:** Especially the **Open/Closed Principle** and **Dependency Inversion** are preserved.

---

## 🧩 Code Structure

```python
# Abstract Factory
class Car(ABC):
    def call_suv(self): ...
    def call_coupe(self): ...

# Concrete Factories
class Benz(Car):
    def call_suv(self): return Gla()
    def call_coupe(self): return Cls()

class Bmw(Car):
    def call_suv(self): return X1()
    def call_coupe(self): return M2()

# Abstract Products
class Suv(ABC):
    def create_suv(self): ...

class Coupe(ABC):
    def create_coupe(self): ...

# Concrete Products
class Gla(Suv):
    def create_suv(self): print("This is your suv benz gla...")

class M2(Coupe):
    def create_coupe(self): print("This is your coupe bmw m2...")
```

---

## 🧪 Sample Usage

```python
def client_coupe(order):
    brands = {"benz": Benz, "bmw": Bmw}
    coupe = brands[order]().call_coupe()
    coupe.create_coupe()

client_coupe("benz")
```

**Output:**

```
This is your coupe benz cls...
```

---

## 🚀 Benefits for Developers

* Learn how to decouple object creation from usage
* Apply this pattern to real-world domains (cars, UI themes, operating systems)
* Improve code flexibility, testability, and scalability

---

## 📚 Who Is This For?

* Python beginners studying OOP and design patterns
* Students preparing for interviews
* Developers building plug-and-play systems

---

## 🌐 SEO Keywords (for discoverability)

`abstract factory pattern python`, `python car factory example`, `oop design pattern cars`, `python suvs and coupes`, `benz bmw design pattern`, `abstract factory solid example`, `create related objects python`, `software engineering design pattern examples`

---

## 🪪 License

MIT — Feel free to reuse, study, or modify for your learning journey 🚀
