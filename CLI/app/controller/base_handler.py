from abc import ABC, abstractmethod

class BaseHandler(ABC):
    @abstractmethod
    def add(self, session):
        pass

    @abstractmethod
    def update(self, session):
        pass

    @abstractmethod
    def delete(self, session):
        pass

    @abstractmethod
    def select(self, session):
        pass
