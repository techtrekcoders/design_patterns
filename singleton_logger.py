"""
Singleton Design Pattern – Logger Example (Interview Ready)

INTENT:
    Ensure that a class has only ONE instance and provide a global point of access.

WHY LOGGER IS A GOOD SINGLETON:
    - Logging should be centralized
    - Multiple logger instances can cause inconsistent logs
    - Shared resource across the application

WHAT THIS IMPLEMENTATION GUARANTEES:
    ✔ Single instance per Python process
    ✔ Controlled object creation
    ✔ Simple and readable

WHAT THIS IMPLEMENTATION DOES NOT GUARANTEE:
    ✘ Single instance across distributed systems
    ✘ Thread safety (unless lock is added)

INTERVIEW TALKING POINT:
    "Singleton ensures a single shared instance per process, not per cluster."
"""


class Logger:
    """
    Logger implemented as a Singleton.

    HOW IT WORKS:
        - `_instance` stores the single instance
        - `__new__()` controls object creation
        - If instance exists, return it
        - Otherwise, create it once
    """

    _instance = None

    def __new__(cls):
        """
        __new__() is responsible for creating the object.
        This method runs BEFORE __init__().
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, message: str) -> None:
        """
        Log a message.
        In real systems, this could write to a file or logging system.
        """
        print(f"[LOG]: {message}")


# ------------------ USAGE EXAMPLE ------------------

if __name__ == "__main__":
    logger1 = Logger()
    logger2 = Logger()

    logger1.log("Application started")
    logger2.log("Processing request")

    # Interview proof: both references point to the same object
    print("Same instance:", logger1 is logger2)


"""
COMMON INTERVIEW QUESTIONS & ANSWERS:

Q: Why not use a global variable?
A: Global variables lack encapsulation and control. Singleton provides controlled access.

Q: Is Singleton thread-safe?
A: Not by default. Thread safety can be added using locks.

Q: Is Singleton an anti-pattern?
A: Overuse is bad. Use it only when a single shared resource is required.

Q: How would you implement Singleton in a distributed system?
A: Use external coordination systems like Redis, database locks, or ZooKeeper.

ONE-LINE INTERVIEW SUMMARY:
    "Singleton ensures a single shared logger instance across the application process."
"""
