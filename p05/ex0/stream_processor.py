from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(
            isinstance(x, (int, float)) for x in data)

    def process(self, data: Any) -> str:
        try:
            if not data:
                return "Processed 0 values"
            total = sum(data)
            avg = total / len(data)
            return (f"Processed {len(data)} "
                    f"numeric values, sum={total}, avg={avg}")
        except Exception as e:
            return f"Error: {e}"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        is_log = data.startswith("ERROR") or data.startswith("INFO")
        return not is_log

    def process(self, data: str) -> str:
        try:
            words = data.split()
            return (
                f"Processed text: {len(data)} characters, "
                f"{len(words)} words"
            )
        except Exception as e:
            return f"Error: {e}"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and (
            data.startswith("ERROR") or data.startswith("INFO"))

    def process(self, data: str) -> str:
        try:
            level, msg = data.split(":", 1)
            return f"{level} level detected: {msg}"
        except ValueError:
            return "Invalid log format"

    def format_output(self, result: str) -> str:
        return f"Output: [ALERT] {result}"


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    test_data: List[Any] = [
        [1, 2, 3, 4, 5],
        "Hello Nexus World",
        "ERROR: Connection timeout"
    ]

    for data in test_data:
        for p in processors:
            if p.validate(data):
                print(f"\nInitializing {p.__class__.__name__}...")
                print(f"Processing data: {repr(data)}")
                print("Validation: Data verified")
                result = p.process(data)
                print(p.format_output(result))
                break

    print("\n=== Polymorphic Processing Demo ===")
    mixed_data: List[Any] = [[10, 20], "Simple Text", "INFO: System Update"]
    for i, data in enumerate(mixed_data, 1):
        for p in processors:
            if p.validate(data):
                print(f"Result {i}: {p.process(data)}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
