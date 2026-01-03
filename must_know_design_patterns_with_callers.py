"""
MUST-KNOW DESIGN PATTERNS – SIMPLE INTERVIEW EXAMPLES (WITH CALLERS)

Each pattern includes:
✔ Minimal classes
✔ Immediate caller/demo
✔ Easy to test & explain
"""

# =========================================================
# 1️⃣ SINGLETON
# =========================================================
class Logger:
    _instance = None

    def __new__(cls):
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
    def send(self, msg):
        pass


class Email(Notification):
    def send(self, msg):
        print("Email:", msg)


class SMS(Notification):
    def send(self, msg):
        print("SMS:", msg)


class NotificationFactory:
    @staticmethod
    def create(channel):
        if channel == "email":
            return Email()
        if channel == "sms":
            return SMS()
        raise ValueError("Invalid channel")


# --- Caller ---
print("\n--- Factory Method Demo ---")
notifier = NotificationFactory.create("email")
notifier.send("Hello User")


# =========================================================
# 3️⃣ ABSTRACT FACTORY
# =========================================================
class PaymentGateway:
    def pay(self, amount):
        pass


class InvoiceService:
    def generate(self):
        pass


class StripePayment(PaymentGateway):
    def pay(self, amount):
        print(f"Stripe payment: {amount}")


class StripeInvoice(InvoiceService):
    def generate(self):
        print("Stripe invoice generated")


class PaymentFactory:
    def create_payment(self):
        pass

    def create_invoice(self):
        pass


class StripeFactory(PaymentFactory):
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
    def __init__(self, name, age=None, email=None):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"User(name={self.name}, age={self.age}, email={self.email})"


class UserBuilder:
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
user = UserBuilder("Krishna").with_age(30).with_email("k@mail.com").build()
print(user)


# =========================================================
# 5️⃣ ADAPTER
# =========================================================
class OldPaymentSystem:
    def make_payment(self, amount):
        print(f"Old payment processed: {amount}")


class PaymentAdapter:
    def __init__(self, old_system):
        self.old_system = old_system

    def pay(self, amount):
        self.old_system.make_payment(amount)


# --- Caller ---
print("\n--- Adapter Demo ---")
adapter = PaymentAdapter(OldPaymentSystem())
adapter.pay(500)


# =========================================================
# 6️⃣ DECORATOR
# =========================================================
class Service:
    def execute(self):
        print("Executing service")


class LoggingDecorator:
    def __init__(self, service):
        self.service = service

    def execute(self):
        print("Logging before execution")
        self.service.execute()


# --- Caller ---
print("\n--- Decorator Demo ---")
service = LoggingDecorator(Service())
service.execute()


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
    def pay(self, amount):
        pass


class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using Card")


class UpiPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)


# --- Caller ---
print("\n--- Strategy Demo ---")
context = PaymentContext(UpiPayment())
context.pay(200)


# =========================================================
# 9️⃣ OBSERVER
# =========================================================
class UserService:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def register_user(self):
        print("User registered")
        for obs in self.observers:
            obs.update()


class EmailObserver:
    def update(self):
        print("Email sent")


# --- Caller ---
print("\n--- Observer Demo ---")
user_service = UserService()
user_service.subscribe(EmailObserver())
user_service.register_user()


# =========================================================
# 🔟 CHAIN OF RESPONSIBILITY
# =========================================================
class Handler:
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
chain = AuthHandler(LogHandler())
chain.handle("REQUEST")


# =========================================================
# 1️⃣1️⃣ PROXY
# =========================================================
class Database:
    def query(self):
        print("Fetching data from database")


class DatabaseProxy:
    def __init__(self):
        self.db = Database()

    def query(self):
        print("Checking cache")
        self.db.query()


# --- Caller ---
print("\n--- Proxy Demo ---")
DatabaseProxy().query()
