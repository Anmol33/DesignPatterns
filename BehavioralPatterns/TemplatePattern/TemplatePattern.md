# Template Pattern: Real-Life Analogy, UML Diagram, and Practice Questions

## Real-Life Analogy for the Template Pattern

The **Template Pattern** can be compared to a **recipe** for baking a cake. Consider a recipe that defines the general steps of making a cake: preparing ingredients, mixing, baking, and cooling. However, different cakes (chocolate, vanilla, etc.) may have specific variations in the ingredients or methods.

- **Template (Recipe)**: The common steps (prepare, mix, bake, cool).
- **Subclasses (Specific Cakes)**: Chocolate cake and vanilla cake provide their own variations (chocolate vs. vanilla flavoring).

In the Template Pattern:
- The **template** defines the skeleton of the algorithm (just like the steps in the recipe).
- Subclasses implement variations (just like choosing different types of cakes or ingredients).

### Example:
- **Base Recipe (Template Method)**: Prepare ingredients -> Mix -> Bake -> Cool.
- **Concrete Recipes (Concrete Implementations)**: Chocolate cake, vanilla cake (implementing variations of the base steps).

## UML Diagram for the Template Pattern

Here is the UML diagram for the Template Pattern:

```plaintext
         +---------------------------+
         |      AbstractClass         |
         +---------------------------+
         | +templateMethod()          |
         | +operation1()              |
         | +operation2()              |
         | -primitiveOperation1()     |
         | -primitiveOperation2()     |
         +---------------------------+
                    ^
                    |
         +---------------------------+
         |      ConcreteClassA        |
         +---------------------------+
         | -primitiveOperation1()     |
         | -primitiveOperation2()     |
         +---------------------------+

         +---------------------------+
         |      ConcreteClassB        |
         +---------------------------+
         | -primitiveOperation1()     |
         | -primitiveOperation2()     |
         +---------------------------+
```

# Real-Life Practice Questions for the Template Pattern

### Question 1: Travel Booking System
You are tasked with developing a **travel booking system** that allows users to book different modes of transportation (e.g., flights, trains, buses). Each mode of transport requires slightly different booking steps, but the overall process is the same: selecting a route, entering passenger details, and making a payment.

How would you use the **Template Method Pattern** to design the booking process?

### Question 2: Document Generation System
Consider a **document generation system** that supports the creation of different types of reports (e.g., PDF, Excel, HTML). Each report type has a common structure (header, body, footer), but the way the content is formatted differs for each report type.

How can you implement this using the **Template Method Pattern**?

### Question 3: Online Exam System
In an **online examination system**, students can take different types of exams (e.g., multiple choice, written, coding). Each exam type follows the same process: instructions are displayed, questions are presented, answers are submitted, and the exam is graded. However, the question presentation and grading mechanism differ for each exam type.

Describe how you would apply the **Template Method Pattern** to build this system.

### Question 4: Payment Gateway Integration
You are working on a payment gateway that integrates with multiple payment services (e.g., Stripe, PayPal, Square). The payment process generally involves authenticating the user, charging the payment, and handling the response. Each payment gateway has its own specific API for these steps.

How would you design a **Template Method Pattern** to standardize the payment flow, allowing for different implementations depending on the gateway?

### Question 5: Game Development
You are developing a **video game** that has different game modes (e.g., single-player, multiplayer, co-op). The overall game lifecycle involves initializing the game, playing a level, and ending the game, but each mode has different logic for the play phase (e.g., handling AI for single-player, handling player synchronization for multiplayer).

How can you design this game architecture using the **Template Method Pattern**?

### Question 6: Coffee Shop Order System
At a **coffee shop**, customers can order different beverages (e.g., espresso, cappuccino, latte). The preparation process generally involves selecting ingredients, brewing the coffee, and serving the drink, but each beverage requires different preparation steps.

How would you apply the **Template Method Pattern** to manage the preparation of different coffee beverages in a scalable way?

### Question 7: Software Build System
Consider a **software build system** that compiles different types of projects (e.g., Java, C++, Python). While the build process is similar (clean, compile, package), each type of project has unique requirements for each step.

How can you design a build system using the **Template Method Pattern** that supports different project types while ensuring common build steps are followed?

### Question 8: Cooking Recipe Application
In a **cooking recipe application**, different types of recipes (e.g., baking, frying, grilling) have a similar structure: preparing ingredients, cooking, and serving. However, the cooking steps vary depending on the method (e.g., baking a cake, frying an egg, grilling a steak).

Explain how you would use the **Template Method Pattern** to implement this recipe system, where each recipe has its own cooking steps but follows the same overall process.

### Question 9: E-learning Content Delivery System
In an **e-learning platform**, content is delivered in different formats (e.g., video, text, interactive quizzes). Each content type has a common delivery process: loading the content, displaying it, and marking it as complete. However, how the content is presented and the interactions differ for each type.

Describe how the **Template Method Pattern** can be applied to ensure consistency in the content delivery process while allowing for variations in presentation.

### Question 10: Employee Onboarding System
You are building an **employee onboarding system** that handles onboarding for different departments (e.g., Engineering, Sales, HR). The onboarding process is generally the same: filling out personal details, assigning equipment, and introducing the team. However, each department requires additional department-specific onboarding steps.

How would you use the **Template Method Pattern** to design this onboarding system to accommodate both common and department-specific steps?

