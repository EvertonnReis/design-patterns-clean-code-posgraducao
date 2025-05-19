from abc import ABC, abstractmethod
import threading


# -------------------- Singleton --------------------

class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        # Double‐checked locking
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class ConfigurationManager(metaclass=SingletonMeta):
    def __init__(self):
        self.settings = {}

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key, default=None):
        return self.settings.get(key, default)


# -------------------- Adapter --------------------

class LegacyPrinter:
    def print_legacy(self, text):
        return f"<<< {text} >>>"


class PrinterAdapter:
    def __init__(self, legacy_printer):
        self.legacy = legacy_printer

    def print(self, text):
        return self.legacy.print_legacy(text)


# -------------------- Strategy --------------------

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass


class BubbleSort(SortingStrategy):
    def sort(self, data):
        arr = data[:]
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class QuickSort(SortingStrategy):
    def sort(self, data):
        arr = data[:]
        if len(arr) < 2:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        mid  = [x for x in arr if x == pivot]
        right= [x for x in arr if x > pivot]
        return self.sort(left) + mid + self.sort(right)


class HybridSort(SortingStrategy):
    def __init__(self, threshold=10):
        self.threshold = threshold
        self._small = BubbleSort()
        self._large = QuickSort()

    def sort(self, data):
        strategy = self._small if len(data) <= self.threshold else self._large
        return strategy.sort(data)


class Sorter:
    def __init__(self, strategy: SortingStrategy = None):
        self.strategy = strategy or HybridSort()

    def sort(self, data):
        return self.strategy.sort(data)


# -------------------- Observer --------------------

class Observer(ABC):
    @abstractmethod
    def update(self, *args, **kwargs):
        pass


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, obs: Observer):
        self._observers.append(obs)

    def detach(self, obs: Observer):
        self._observers.remove(obs)

    def notify(self, *args, **kwargs):
        for obs in self._observers:
            obs.update(*args, **kwargs)


class Logger(Observer):
    def __init__(self):
        self.logs = []

    def update(self, message):
        entry = f"[LOG] {message}"
        self.logs.append(entry)


# Expondo tudo para testes
__all__ = [
    "ConfigurationManager", "LegacyPrinter", "PrinterAdapter",
    "Sorter", "BubbleSort", "QuickSort", "HybridSort",
    "Subject", "Logger"
]
