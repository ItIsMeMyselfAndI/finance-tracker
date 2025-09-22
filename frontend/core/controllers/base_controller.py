from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from frontend.core.models import Model
from frontend.core.views import View

M = TypeVar("M", bound=Model)
V = TypeVar("V", bound=View)


class Controller(ABC, Generic[M, V]):

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def update_display(self):
        pass

    @property
    @abstractmethod
    def model(self) -> M:
        pass

    @model.setter
    @abstractmethod
    def model(self, value: M):
        pass

    @property
    @abstractmethod
    def view(self) -> V:
        pass

    @view.setter
    @abstractmethod
    def view(self, value: V):
        pass
