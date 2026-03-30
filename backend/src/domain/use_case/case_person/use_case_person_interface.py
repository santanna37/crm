from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models.model_person import PersonModel
from fastapi import BackgroundTasks

class UseCasePersonInterface(ABC):

    @abstractmethod
    def health(self) -> str: pass

    @abstractmethod
    def create(self, person: PersonModel, background_tasks: BackgroundTasks = None) -> Dict: pass

    @abstractmethod
    def read(self, filters: PersonModel) -> List: pass