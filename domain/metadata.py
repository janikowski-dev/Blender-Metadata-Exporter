from abc import ABC, abstractmethod

class Metadata(ABC):
    @abstractmethod
    def to_dict(self) -> dict[str, object]:
        pass