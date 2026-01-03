"""
Factory Method Pattern – Notification Example (Interview Ready)

INTENT:
    Define an interface for creating an object, but let subclasses (or a factory method)
    decide which class to instantiate.

WHY THIS IS INTERVIEW-RELEVANT:
    - Avoids long if-else chains spread across the codebase
    - Centralizes object creation
    - Makes adding new types easy (Open/Closed Principle)

WHEN TO USE:
    - When object creation depends on runtime input (type, config, environment)
    - When you want to decouple creation logic from usage logic

WHAT THIS IMPLEMENTATION GUARANTEES:
    ✔ Caller does not know the concrete class
    ✔ Adding a new notifier usually requires minimal change

WHAT THIS DOES NOT GUARANTEE:
    ✘ No magic: if you use a single "big factory" with many if-else cases,
      it can become a maintenance hotspot (fix by using registration/plugins)
"""

from abc import ABC, abstractmethod


# ----------- Product Interface -----------
class Notifier(ABC):
    """Common interface for all notification types."""

    @abstractmethod
    def send(self, user_id: str, message: str) -> None:
        pass


# ----------- Concrete Products -----------
class EmailNotifier(Notifier):
    def send(self, user_id: str, message: str) -> None:
        print(f"[EMAIL] to={user_id} msg='{message}'")


class SMSNotifier(Notifier):
    def send(self, user_id: str, message: str) -> None:
        print(f"[SMS] to={user_id} msg='{message}'")


class PushNotifier(Notifier):
    def send(self, user_id: str, message: str) -> None:
        print(f"[PUSH] to={user_id} msg='{message}'")


# ----------- Factory Method -----------
class NotifierFactory:
    """
    Factory Method: create_notifier() decides which Notifier to return.

    Interview Tip:
        You can say:
        "I use a factory to isolate object creation. Business logic depends on the interface,
         not concrete implementations."
    """

    @staticmethod
    def create_notifier(channel: str) -> Notifier:
        channel = channel.strip().lower()

        if channel == "email":
            return EmailNotifier()
        if channel == "sms":
            return SMSNotifier()
        if channel == "push":
            return PushNotifier()

        raise ValueError(f"Unsupported notification channel: {channel}")


# ----------- Client Code -----------
def notify_user(user_id: str, message: str, channel: str) -> None:
    """
    Client code depends only on Notifier interface.
    It doesn't care which concrete notifier is used.
    """
    notifier = NotifierFactory.create_notifier(channel)
    notifier.send(user_id, message)


if __name__ == "__main__":
    notify_user("user_101", "Welcome!", "email")
    notify_user("user_101", "OTP: 123456", "sms")
    notify_user("user_101", "You have a new message", "push")


"""
COMMON INTERVIEW QUESTIONS & ANSWERS:

Q: Why not just use if-else directly where needed?
A: If-else scattered across the codebase creates duplication and tight coupling.
   A factory centralizes creation and improves maintainability.

Q: Isn't this still if-else in the factory?
A: Yes, but it's in ONE place. For large systems, we can use a registration map (plugin style)
   to avoid modifying the factory for every new type.

Q: How is this different from Abstract Factory?
A: Factory Method creates ONE product family/type per decision.
   Abstract Factory creates a FAMILY of related products (multiple objects that work together).

ONE-LINE INTERVIEW SUMMARY:
    "Factory Method encapsulates object creation and returns interface types,
     making code extensible and reducing coupling."
"""
