from abc import ABC, abstractmethod





class UseCaseEmailInterface(ABC):


    @abstractmethod
    def welcome_email(email: str, name:str, text_email: str): pass 
