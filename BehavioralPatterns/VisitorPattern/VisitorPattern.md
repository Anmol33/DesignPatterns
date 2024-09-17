
# Visitor Pattern

## Real-Life Analogy

Imagine a museum where different types of visitors (students, art critics, tourists) visit various exhibits (paintings, sculptures, artifacts). Each visitor has a different way of appreciating the exhibits:

- **Students** might take notes and ask questions.
- **Art critics** might analyze the technique and composition.
- **Tourists** might simply take pictures and enjoy the beauty.

The museum doesn’t change for each type of visitor, but the behavior towards each exhibit changes based on who the visitor is. This is similar to how the Visitor Pattern works.

In this pattern:
- The **museum** represents a structure (objects).
- The **exhibits** are the elements being visited (classes).
- The **different types of visitors** are different visitor classes (algorithms) that operate on the elements but are defined externally to them.

## UML Diagram

Here is a breakdown of the UML diagram for the Visitor Pattern:

1. **Visitor**: Declares a `visit` method for each type of element in the structure.
2. **ConcreteVisitor**: Implements the operations defined by the `Visitor` interface for specific elements.
3. **Element**: Declares an `accept` method that takes a `Visitor` as an argument.
4. **ConcreteElement**: Implements the `accept` method, usually passing itself (`this`) to the visitor's `visit` method.
5. **ObjectStructure**: Holds a collection of `Elements` and allows the visitor to visit each element.

### UML Representation:

```
+-------------------+           +----------------------+
|    <<interface>>   |           |  <<interface>>       |
|     Visitor        |<--------- |  Element             |
|-------------------|           |----------------------|
| + visitElementA()  |           | + accept(visitor)    |
| + visitElementB()  |           |                      |
+-------------------+           +----------------------+
           ^                                 ^
           |                                 |
+-------------------+           +----------------------+
| ConcreteVisitor   |           | ConcreteElementA      |
|-------------------|           |----------------------|
| + visitElementA() |           | + accept(visitor)     |
| + visitElementB() |           | + specificMethodA()   |
+-------------------+           +----------------------+
                                     ^
                                     |
                               +----------------------+
                               | ConcreteElementB      |
                               |----------------------|
                               | + accept(visitor)     |
                               | + specificMethodB()   |
                               +----------------------+
```


## Visitor Pattern Practice Questions

Here are some practice questions to help you better understand and implement the Visitor Pattern:

### 1. Basic Visitor Implementation:
Implement the Visitor Pattern for a small zoo where there are different animals like **Lion**, **Monkey**, and **Dolphin**. Each animal can perform different actions when visited by a **SpeakVisitor** or **JumpVisitor**. Each visitor performs a specific behavior for each animal.

**Hint**:
- **SpeakVisitor** makes the animals “speak.”
- **JumpVisitor** makes the animals “jump.”

### 2. File System Example:
You are tasked with creating a file system that contains two types of files: **TextFile** and **AudioFile**. Implement the Visitor Pattern where different visitors can:
- Count the number of words in a **TextFile**.
- Calculate the total playtime in an **AudioFile**.

Create two visitors: **WordCounterVisitor** and **PlayTimeVisitor** to handle these operations.

### 3. Shopping Cart Example:
In an e-commerce platform, you need to implement a shopping cart system where there are different types of items, such as **Book** and **Electronics**. Implement the Visitor Pattern so that:
- **PriceVisitor** can calculate the total price of items in the cart.
- **WeightVisitor** can calculate the total shipping weight of items in the cart.

### 4. Tax Calculation for Different Countries:
You are tasked with building a tax calculation system for two countries: **USA** and **UK**. Implement the Visitor Pattern where:
- Different types of products like **Food**, **Electronics**, and **Clothes** are subject to different tax rates in each country.
- Implement visitors like **USATaxVisitor** and **UKTaxVisitor** that calculate the correct tax for each product based on the country.