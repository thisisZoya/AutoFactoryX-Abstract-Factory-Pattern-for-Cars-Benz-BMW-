# AutoFactoryX-Abstract-Factory-Pattern-for-Cars-Benz-BMW-
# 🚗 Car Management System using Abstract Factory Pattern

This is a simple and extensible **Car Management System** built with Python using the **Abstract Factory Design Pattern**. It allows users to create and manage different families of car types (SUV, Coupe) for various brands like **Benz** and **BMW**.

---

## 🧱 Design Pattern

This project uses the **Abstract Factory Pattern** to:

* Create related objects (SUV & Coupe) without specifying their concrete classes
* Encapsulate a group of individual factories with a common interface

---

## 🧩 Structure

```
car_factory_system/
├── interfaces.py         # Abstract base classes (SUV, Coupe, CarFactory)
├── benz_models.py        # Benz SUV & Coupe implementations
├── bmw_models.py         # BMW SUV & Coupe implementations
├── benz_factory.py       # BenzFactory implementing CarFactory
├── bmw_factory.py        # BMWFactory implementing CarFactory
├── client.py             # Client logic using abstract factory
└── main.py               # Entry point for user interaction
```

---

## 🚀 How It Works

1. User selects a car brand (`benz` or `bmw`)
2. The factory creates both an SUV and a Coupe for that brand
3. Each vehicle exposes its own `drive()` method

---

## 💻 Example

```bash
$ python main.py
Enter brand (benz/bmw): bmw
Driving BMW SUV with dynamic power!
Driving BMW Coupe with aggressive design!
```

---

## 📦 Adding a New Brand

To add another brand:

1. Implement the `SUV` and `Coupe` classes
2. Create a new factory implementing `CarFactory`
3. Update `main.py` to register the new factory

---

## 📚 Educational Value

This project is ideal for:

* Understanding Abstract Factory in real-world use
* Practicing clean and modular Python code
* Preparing for design pattern interviews

---

## 🪪 License

This project is licensed under the MIT License.
