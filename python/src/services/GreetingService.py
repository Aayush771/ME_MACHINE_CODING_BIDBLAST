from typing import List

from src.entities import Greeting
from src.repositories import GreetingRepository

class GreetingService:
    def __init__(self, greetingRepository: GreetingRepository) -> None:
        self._greetingRepository = greetingRepository
    
    def create(self, message: str) -> Greeting:
        g = Greeting(message)
        return self._greetingRepository.save(g)

    def getAllGreetings(self) -> List[Greeting]:
        return self._greetingRepository.findAll()

    def getGreeting(self, id: int) -> Greeting:
        g = self._greetingRepository.findById(id)
        if g is None:
            raise Exception("Greeting with id: " + str(id) + " not found!")
        return g