from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def add(self, observer: Observer) -> None:
        """
        Agrega un observer a Subject
        """
        pass

    @abstractmethod
    def remove(self, observer: Observer) -> None:
        """
        Elimina un observer de Subject
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notifica a todos los observers sobre un evento
        """
        pass


class ConcreteSubject(Subject):

    _state: int = None
    """
    Por simplicidad, el estado de Subject se almacena en esta variable.
    """

    _observers: List[Observer] = []
    """
    Lista de suscriptores de un evento(categorized by event type, etc.).
    """

    def add(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def remove(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    Metodos de interes por otros objetos
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Recibe una actualizacion de Subject
        """
        pass


"""
Los Observer concretos reaccionan a las actualizaciones emitidas por el Subject a traves de Observer.
"""


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    # The client code.

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.add(observer_a)

    observer_b = ConcreteObserverB()
    subject.add(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.remove(observer_a)
