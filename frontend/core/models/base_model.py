from abc import ABC, abstractmethod
from typing import Dict, List

from backend.transaction_manager import Transaction


class Model(ABC):

    @abstractmethod
    def initialize_managers(self, *args, **kwargs):
        pass

    @abstractmethod
    def initialize_vars(self, *args, **kwargs):
        pass

    @abstractmethod
    def save_user_inputs_to_database(self, form_per_transaction_type: Dict):
        pass

    @abstractmethod
    def load_transactions_per_filter(self) -> Dict[str, List[Transaction]]:
        pass

    @abstractmethod
    def load_amounts(self):
        pass
