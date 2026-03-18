from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.model_person import PersonModel



class UseCaseEmailInterface(ABC):

    @abstractmethod
    def builder(self, email_class: Dict):pass

    @abstractmethod
    def welcome_email(self, email,email_class:Dict):pass
