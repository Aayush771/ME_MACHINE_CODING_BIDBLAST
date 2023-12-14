class Greeting:
    def __init__(self, message: str, id=None ) -> None:
        self._message = message
        self._id = id

    def get_id(self):
        return self._id

    def get_message(self):
        return self._message

    def __hash__(self):
        return hash(self._id)

    def __eq__(self, other):
        return isinstance(other, Greeting) and self._id == other._id

    def __repr__(self) -> str:
        return f'Greeting [id={self._id}]'
