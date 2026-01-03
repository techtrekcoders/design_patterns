# 🎯 MUST-KNOW DESIGN PATTERNS – INTERVIEW THEORY NOTES

These notes are written for:
- 🔹 Quick revision before interviews
- 🔹 Explaining patterns confidently
- 🔹 Remembering *WHY* and *WHEN*, not just *WHAT*

---

## 1️⃣ Singleton → *One Instance*

### What it is
Singleton ensures **only one instance of a class exists** and provides a **global access point**.

### Why it exists
- Some resources must be shared:
  - Logger
  - Configuration
  - Connection pools

### When to use
- When multiple instances cause inconsistent behavior
- When a shared state is required

### When NOT to use
- When testability matters a lot
- When state should not be global
- In distributed systems (needs external coordination)

### Interview one-liner
> “Singleton ensures a single instance per application process.”

---

## 2️⃣ Factory → *Create Object*

### What it is
Factory encapsulates **object creation logic** and returns objects via a common interface.

### Why it exists
- Avoid `if-else` scattered everywhere
- Centralize object creation
- Follow Open–Closed Principle

### When to use
- Object creation depends on input
- Multiple implementations of same interface

### Interview one-liner
> “Factory hides object creation and returns interface types.”

---

## 3️⃣ Abstract Factory → *Create Families*

### What it is
Abstract Factory creates **families of related objects** that are meant to be used together.

### Why it exists
- Ensure compatibility among related objects
- Avoid mixing implementations from different families

### When to use
- Platform-based systems (AWS vs Azure)
- Theming (Light vs Dark)
- Multiple related services

### Key difference from Factory
| Factory | Abstract Factory |
|------|----------------|
| One object | Multiple related objects |

### Interview one-liner
> “Abstract Factory creates families of related objects.”

---

## 4️⃣ Builder → *Step-by-Step Creation*

### What it is
Builder constructs **complex objects step-by-step** instead of large constructors.

### Why it exists
- Avoid constructors with many optional parameters
- Improve readability and immutability

### When to use
- Many optional fields
- Object construction is complex

### When NOT to use
- Simple objects with few parameters

### Interview one-liner
> “Builder helps construct complex objects cleanly.”

---

## 5️⃣ Adapter → *Fix Interface Mismatch*

### What it is
Adapter allows **incompatible interfaces** to work together.

### Why it exists
- Integrate legacy or third-party code
- Avoid modifying existing stable code

### When to use
- Old system + new interface
- External API integration

### Interview one-liner
> “Adapter converts one interface into another.”

---

## 6️⃣ Decorator → *Add Behavior*

### What it is
Decorator adds **new behavior dynamically** without modifying the original class.

### Why it exists
- Follow Open–Closed Principle
- Avoid subclass explosion

### Common use cases
- Logging
- Authentication
- Compression

### Decorator vs Inheritance
- Inheritance → static behavior
- Decorator → dynamic behavior

### Interview one-liner
> “Decorator adds behavior without changing the original class.”

---

## 7️⃣ Facade → *Simplify System*

### What it is
Facade provides a **simple interface** to a complex subsystem.

### Why it exists
- Hide internal complexity
- Improve usability

### When to use
- Multiple subsystems must be coordinated
- Client should not know internal details

### Interview one-liner
> “Facade hides system complexity behind a simple interface.”

---

## 8️⃣ Strategy → *Switch Logic*

### What it is
Strategy defines a family of algorithms and **switches them at runtime**.

### Why it exists
- Avoid large `if-else` blocks
- Support dynamic behavior

### When to use
- Multiple ways to perform an action
- Algorithms change at runtime

### Interview one-liner
> “Strategy allows switching algorithms dynamically.”

---

## 9️⃣ Observer → *Event Notification*

### What it is
Observer defines a **one-to-many dependency** where observers are notified automatically.

### Why it exists
- Event-driven systems
- Loose coupling between components

### When to use
- Notifications
- Pub-Sub systems
- UI event handling

### Common issue
- Memory leaks if observers are not unsubscribed

### Interview one-liner
> “Observer enables event-driven communication.”

---

## 🔟 Chain of Responsibility → *Pipeline Processing*

### What it is
Chain passes a request through **a chain of handlers** until it is handled.

### Why it exists
- Decouple sender and receiver
- Flexible processing pipelines

### When to use
- Validation
- Middleware
- Request processing

### Interview one-liner
> “Chain of Responsibility processes requests in steps.”

---

## 1️⃣1️⃣ Proxy → *Access Control*

### What it is
Proxy controls access to a real object.

### Why it exists
- Add caching
- Add security
- Lazy loading

### Proxy vs Decorator
- Proxy → controls access
- Decorator → adds behavior

### Interview one-liner
> “Proxy controls access to the real object.”

---

## 🧠 FINAL MEMORY TRICK (VERY IMPORTANT)

Think in **WHY**, not definitions:

- Singleton → shared resource  
- Factory → object creation  
- Abstract Factory → related objects  
- Builder → complex construction  
- Adapter → compatibility  
- Decorator → enhancement  
- Facade → simplicity  
- Strategy → flexibility  
- Observer → events  
- Chain → pipeline  
- Proxy → protection  

---

## 🎯 HOW INTERVIEWERS EVALUATE YOU

They check:
- Can you **explain WHY**?
- Can you **give a real example**?
- Can you **avoid overusing patterns**?

Not memorization — **decision making**.

---

## ⭐ ONE FINAL INTERVIEW LINE (POWERFUL)

> “Design patterns are tools, not rules.  
> The goal is clean, flexible, and maintainable design.”

---
