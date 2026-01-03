"""
MUST-KNOW DESIGN PATTERNS – SIMPLE INTERVIEW EXAMPLES (WITH NOTES)

HOW TO USE THIS FILE:
- Each pattern has:
  1) Small classes
  2) Clear comments (WHY this class exists)
  3) Immediate caller/demo
- Read comments + run code = interview ready
"""

# =========================================================
# 1️⃣ SINGLETON
# =========================================================
class Logger:
    """
    Singleton class.
    WHY:
        Logging should be centralized.
        Multiple instances = inconsistent logs.

    INTERVIEW LINE:
        "Singleton ensures only one instance per process."
    """
    _instance = None

    def __new__(cls):
        # Control object creation
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, msg):
        print(f"[LOG]: {msg}")


# --- Caller ---
print("\n--- Singleton Demo ---")
logger1 = Logger()
logger2 = Logger()
logger1.log("App started")
print("Same instance:", logger1 is logger2)


# =========================================================
# 2️⃣ FACTORY METHOD
# =========================================================
class Notification:
    """
    Product interface.
    WHY:
        Client should depend on interface, not concrete classes.
    """
    def send(self, msg):
        pass


class Email(Notification):
    """Concrete product: Email notification"""
    def send(self, msg):
        print("Email:", msg)


class SMS(Notification):
    """Concrete product: SMS notification"""
    def send(self, msg):
        print("SMS:", msg)


class NotificationFactory:
    """
    Factory Method.
    WHY:
        Centralize object creation.
        Avoid if-else scattered across code.

    INTERVIEW LINE:
        "Factory encapsulates object creation logic."
    """
    @staticmethod
    def create(channel):
        if channel == "email":
            return Email()
        if channel == "sms":
            return SMS()
        raise ValueError("Invalid channel")


# --- Caller ---
print("\n--- Factory Method Demo ---")
NotificationFactory.create("email").send("Hello User")


# =========================================================
# 3️⃣ ABSTRACT FACTORY
# =========================================================
class PaymentGateway:
    """Abstract product: Payment"""
    def pay(self, amount):
        pass


class InvoiceService:
    """Abstract product: Invoice"""
    def generate(self):
        pass


class StripePayment(PaymentGateway):
    """Concrete product (Stripe family)"""
    def pay(self, amount):
        print(f"Stripe payment: {amount}")


class StripeInvoice(InvoiceService):
    """Concrete product (Stripe family)"""
    def generate(self):
        print("Stripe invoice generated")


class PaymentFactory:
    """
    Abstract Factory.
    WHY:
        Create families of related objects.
    """
    def create_payment(self):
        pass

    def create_invoice(self):
        pass


class StripeFactory(PaymentFactory):
    """
    Concrete Factory.
    INTERVIEW LINE:
        "Abstract Factory creates families of related objects."
    """
    def create_payment(self):
        return StripePayment()

    def create_invoice(self):
        return StripeInvoice()


# --- Caller ---
print("\n--- Abstract Factory Demo ---")
factory = StripeFactory()
factory.create_payment().pay(100)
factory.create_invoice().generate()


# =========================================================
# 4️⃣ BUILDER
# =========================================================
class User:
    """
    Complex object.
    WHY:
        Many optional fields.
    """
    def __init__(self, name, age=None, email=None):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"User(name={self.name}, age={self.age}, email={self.email})"


class UserBuilder:
    """
    Builder.
    WHY:
        Avoid large constructors.
        Build object step-by-step.

    INTERVIEW LINE:
        "Builder helps construct complex objects cleanly."
    """
    def __init__(self, name):
        self.name = name
        self.age = None
        self.email = None

    def with_age(self, age):
        self.age = age
        return self

    def with_email(self, email):
        self.email = email
        return self

    def build(self):
        return User(self.name, self.age, self.email)


# --- Caller ---
print("\n--- Builder Demo ---")
print(UserBuilder("Krishna").with_age(30).with_email("k@mail.com").build())


# =========================================================
# 5️⃣ ADAPTER
# =========================================================
class OldPaymentSystem:
    """
    Legacy system.
    PROBLEM:
        Interface doesn't match new system.
    """
    def make_payment(self, amount):
        print(f"Old payment processed: {amount}")


class PaymentAdapter:
    """
    Adapter.
    WHY:
        Make incompatible interfaces work together.

    INTERVIEW LINE:
        "Adapter converts one interface into another."
    """
    def __init__(self, old_system):
        self.old_system = old_system

    def pay(self, amount):
        self.old_system.make_payment(amount)


# --- Caller ---
print("\n--- Adapter Demo ---")
PaymentAdapter(OldPaymentSystem()).pay(500)


# =========================================================
# 6️⃣ DECORATOR
# =========================================================
class Service:
    """Core service"""
    def execute(self):
        print("Executing service")


class LoggingDecorator:
    """
    Decorator.
    WHY:
        Add behavior without modifying original class.

    INTERVIEW LINE:
        "Decorator adds behavior dynamically."
    """
    def __init__(self, service):
        self.service = service

    def execute(self):
        print("Logging before execution")
        self.service.execute()


# --- Caller ---
print("\n--- Decorator Demo ---")
LoggingDecorator(Service()).execute()


# =========================================================
# 7️⃣ FACADE
# =========================================================
class OrderService:
    def place_order(self):
        print("Order placed")


class PaymentService:
    def pay(self):
        print("Payment done")


class OrderFacade:
    """
    Facade.
    WHY:
        Provide simple interface to complex subsystems.

    INTERVIEW LINE:
        "Facade hides system complexity."
    """
    def complete_order(self):
        OrderService().place_order()
        PaymentService().pay()


# --- Caller ---
print("\n--- Facade Demo ---")
OrderFacade().complete_order()


# =========================================================
# 8️⃣ STRATEGY
# =========================================================
class PaymentStrategy:
    """Strategy interface"""
    def pay(self, amount):
        pass


class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Card")


class UpiPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


class PaymentContext:
    """
    Context.
    WHY:
        Switch algorithms at runtime.

    INTERVIEW LINE:
        "Strategy avoids if-else logic."
    """
    def __init__(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)


# --- Caller ---
print("\n--- Strategy Demo ---")
PaymentContext(UpiPayment()).pay(200)


# =========================================================
# 9️⃣ OBSERVER
# =========================================================
class UserService:
    """
    Subject.
    WHY:
        Notify multiple listeners on event.
    """
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def register_user(self):
        print("User registered")
        for obs in self.observers:
            obs.update()


class EmailObserver:
    """
    Observer.
    INTERVIEW LINE:
        "Observer enables event-driven design."
    """
    def update(self):
        print("Email sent")


# --- Caller ---
print("\n--- Observer Demo ---")
service = UserService()
service.subscribe(EmailObserver())
service.register_user()


# =========================================================
# 🔟 CHAIN OF RESPONSIBILITY
# =========================================================
class Handler:
    """
    Base handler.
    WHY:
        Pass request through chain.
    """
    def __init__(self, next_handler=None):
        self.next = next_handler

    def handle(self, request):
        if self.next:
            self.next.handle(request)


class AuthHandler(Handler):
    def handle(self, request):
        print("Auth check")
        super().handle(request)


class LogHandler(Handler):
    def handle(self, request):
        print("Logging request")
        super().handle(request)


# --- Caller ---
print("\n--- Chain of Responsibility Demo ---")
AuthHandler(LogHandler()).handle("REQUEST")


# =========================================================
# 1️⃣1️⃣ PROXY
# =========================================================
class Database:
    """Real object"""
    def query(self):
        print("Fetching data from database")


class DatabaseProxy:
    """
    Proxy.
    WHY:
        Control access, add caching/security.

    INTERVIEW LINE:
        "Proxy controls access to the real object."
    """
    def __init__(self):
        self.db = Database()

    def query(self):
        print("Checking cache")
        self.db.query()


# --- Caller ---
print("\n--- Proxy Demo ---")
DatabaseProxy().query()
