from typing import List, Optional

from src.entities import Greeting


class GreetingRepository:
    def __init__(self) -> None:
        self._greetingMap = {}
        self._autoIncrement = 1

    def save(self,greeting: Greeting) -> Greeting:
        g = Greeting(greeting.get_message(),self._autoIncrement)
        self._greetingMap[self._autoIncrement] = g
        self._autoIncrement += 1
        return g

    def existsById(self,id: int) -> bool:
        if id in self._greetingMap:
            return True
        else:
            return False

    def findById(self, id: int) -> Optional[Greeting]:
        return self._greetingMap.get(id)

    def findAll(self) -> List[Greeting]:
        return list(self._greetingMap.values())

    def deleteById(self,id: int) -> None:
        del self._greetingMap[id]

    def count(self) -> int:
        return len(self._greetingMap)