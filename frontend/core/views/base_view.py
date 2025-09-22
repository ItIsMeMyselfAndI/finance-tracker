from abc import ABC, abstractmethod
import customtkinter as ctk


class View(ctk.CTkFrame, ABC):

    @abstractmethod
    def create(self):
        pass
