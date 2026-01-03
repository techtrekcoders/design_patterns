"""# Design Pattern"""

# Singleton Classes

class Singleton:
  _instance = None

  def __new__(cls,*args,**kwargs):
    if cls._instance is None:
      cls._instance = super().__new__(cls,*args,**kwargs)
    return cls._instance

s1 = Singleton()
s1.data=10
print('s1 data:',s1.data)

s2 = Singleton()
print('s2 data:',s2.data)

s2.data=15
print('s1 data:',s1.data)

# Factory Pattern

from abc import ABCMeta, abstractmethod

class Person(metaclass=ABCMeta):
  @abstractmethod
  def create(self):
    pass

class HR(Person):
  def create(self,name):
    print(f'HR {name} is created')

class Engineer(Person):
  def create(self,name):
    print(f'Engineer {name} is created')

class PersonFactory:
  @classmethod
  def createPerson(cls,designation,name):
    eval(designation)().create(name)

if __name__=='__main__':
  designation='Engineer'
  name = 'Krishna'
  PersonFactory.createPerson(designation,name)

# Template design pattern

class Cook:
  def prepareDish(self):
    self.cutter = Cutter()
    self.cutter.cutVegetable()

    self.boiler = Boiler()
    self.boiler.boilVegetables()

    self.frier = Frier()
    self.frier.fryVegetables()

class Cutter:
  def cutVegetable(self):
    print('All vegies are cut')

class Boiler:
  def boilVegetables(self):
    print('All vegies are boiled')

class Frier:
  def fryVegetables(self):
    print('All vegies are fried')


if __name__=='__main__':
  cook = Cook()
  cook.prepareDish()

from abc import ABCMeta, abstractmethod

class ThreeDaysTrip(metaclass=ABCMeta):
  @abstractmethod
  def transport(self):
    pass

  @abstractmethod
  def day1(self):
    pass

  @abstractmethod
  def day2(self):
    pass

  @abstractmethod
  def day3(self):
    pass

  @abstractmethod
  def backtohome(self):
    pass

  def iternary(self):
    print('trip is started')
    self.transport()
    self.day1()
    self.day2()
    self.day3()
    self.backtohome()
    print('Trip is over')

class KeralaTrip(ThreeDaysTrip):
  def transport(self):
    print('will go to Kerala by train')

  def day1(self):
    print('go to boat')

  def day2(self):
    print('go to beach')

  def day3(self):
    print('to for shopping')

  def backtohome(self):
    print('will go back by plan')

k = KeralaTrip()
k.iternary()

# command design pattern

from abc import ABC, abstractmethod

class BaseCommand(ABC):
  @abstractmethod
  def execute(self):
    pass

class EmailCommand(BaseCommand):
  def __init__(self,receiver,data):
    self.receiver=receiver
    self.data=data

  def execute(self):
    self.receiver.send_email(self.data)

class SMSCommand(BaseCommand):
  def __init__(self,receiver,data):
    self.receiver=receiver
    self.data=data

  def execute(self):
    self.receiver.send_sms(self.data)


class NotificationService:
  def send_email(self,data):
    print('sending email:',data)

  def send_sms(self,data):
    print('sending sms:',data)

class NotificationInvoker:
  def __init__(self):
    self.notification_history=[]

  def invoke(self,command):
    self.notification_history.append(command)
    command.execute()

invoker = NotificationInvoker()
receiver = NotificationService()

invoker.invoke(EmailCommand(receiver,{'sub':'Test email'}))
invoker.invoke(SMSCommand(receiver,{'sub':'Test SMS'}))

# Observer Design Pattern
class Subject:
  def __init__(self):
    self.observers=[]

  def register_observer(self,observer):
    self.observers.append(observer)

  def remove_observer(self,observer):
    self.observers.remove(observer)

  def notify_observers(self,message):
    for observer in self.observers:
      observer.update(message)

class Observer:
  def __init__(self,name):
    self.name=name

  def update(self,message):
    print(f'{message} received message')

subject = Subject()
o1 = Observer('Observer 1')
o2 = Observer('Observer 2')
o3 = Observer('Observer 3')

subject.register_observer(o1)
subject.register_observer(o2)
subject.register_observer(o3)

subject.notify_observers('Hello Team')
subject.remove_observer(o2)
subject.notify_observers('Hello Again')

# Command design pattern

from abc import ABCMeta, abstractmethod

class AbstractCmd(metaclass=ABCMeta):
  @abstractmethod
  def execute(self,command):
    pass

class RealCmd(AbstractCmd):
  def execute(self,command):
    print(f'{command} command executed')

class ProxyCmd(AbstractCmd):
  def __init__(self,user):
    self.is_authorised=False
    if user=='admin':
      self.is_authorised=True
    self.executor=RealCmd()
    self.restricted_commands = ['rm','mv']

  def execute(self,command):
    if self.is_authorised:
      self.executor.execute(command)
    else:
      if any([command.strip().startswith(cmd) for cmd in self.restricted_commands]):
        print(f'{command} is not allowed for non-admin users')
      else:
        self.executor.execute(command)

admin_executor = ProxyCmd('admin')
admin_executor.execute('ls -la')
admin_executor.execute('rm -rf/')

other_executor=ProxyCmd('other')
other_executor.execute('ls -la')
other_executor.execute('rm -rf/')

# TheadPoolExecutor

import concurrent.futures

def task(name):
  import time
  print(f'Task{name} is started')
  time.sleep(2)
  print(f'Task {name} is completed')
  return f'Result from Task {name}'

with concurrent.futures.ThreadPoolExecutor() as executor:
  results = executor.map(task,range(1,6))

print('All tasks completed:')

for result in results:
  print(result)

# ProcessPoolExecutor

import concurrent.futures

def task(name):
  import time
  print(f'task {name} is started')
  time.sleep(2)
  print(f'task {name} is completed')
  return f'Result from task {name}'

with concurrent.futures.ProcessPoolExecutor() as executor:
  results = executor.map(task, range(1,6))

print('All tasks completed')

for result in results:
  print(result)

# Multiprocessing Process

import multiprocessing

def worker_function(x):
  print(f'Worker {x} started')
  result = x*x
  print(f'Worker {x} is completed')
  return result

if __name__=='__main__':
  processes = []
  for i in range(4):
    process = multiprocessing.Process(target=worker_function, args=(i,))
    processes.append(process)
    process.start()

  for process in processes:
    process.join()

# Multiprocessing Pool

import multiprocessing

def worker_function(x):
  return x*x

if __name__=='__main__':
  with multiprocessing.Pool(processes=4) as pool:
    result = pool.map(worker_function, range(10))
    print(result)

# Multiprocessing Queue

import multiprocessing

def producer(queue):
  for i in range(5):
    queue.put(i)
    print(f'Produced: {i}')

def consumer(queue):
  while True:
    item = queue.get()
    if item is None:
      break
    print(f'Consumed {item}')

if __name__ =='__main__':
  queue = multiprocessing.Queue()
  producer_process = multiprocessing.Process(target=producer, args=(queue,))
  consumer_process = multiprocessing.Process(target=consumer, args=(queue,))

  producer_process.start()
  consumer_process.start()

  producer_process.join()
  queue.put(None)

  consumer_process.join()

  print('Both producer and consumer process is completed')

# Multithreading

import threading

def worker_function():
  for i in range(5):
    print(f'Thread {threading.current_thread().name}: {i}')

thread1 = threading.Thread(target=worker_function)
thread2 = threading.Thread(target=worker_function)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('Both threads have finished')
