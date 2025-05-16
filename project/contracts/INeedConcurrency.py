from abc import ABC, abstractmethod


class INeedConcurrency(ABC):
    __concurrency: int

    @property
    @abstractmethod
    def concurrency(self) -> int:
        return self.__concurrency

    @concurrency.setter
    @abstractmethod
    def concurrency(self, value: int) -> None:
        if value != self.__concurrency:
            self.__concurrency = value
