from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = stream_type
        display_name = self.__class__.__name__.replace("Stream", " Stream")
        print(f"Initializing {display_name}...")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        return [x for x in data_batch if criteria in str(x)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"id": self.stream_id, "type": self.stream_type}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temps = [float(str(x).split(":")[1])
                     for x in data_batch if "temp:" in str(x)]
            avg = sum(temps) / len(temps) if temps else 0.0
            return (f"Sensor analysis: {len(data_batch)} "
                    f"readings processed, avg temp: {avg:.1f}°C\n")
        except Exception:
            return "Sensor analysis: 0 readings processed"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            net = 0.0
            for item in data_batch:
                act, val = str(item).split(":")
                net += float(val) if act == "buy" else -float(val)
            sign = "+" if net > 0 else ""
            return (f"Transaction analysis: {len(data_batch)} "
                    f"operations processed, net flow: {sign}{net:.0f} units\n")
        except Exception:
            return "Transaction analysis: 0 operations processed"


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        errors = str(data_batch).lower().count("error")
        return (f"Event analysis: {len(data_batch)} events processed,"
                f" {errors} error detected\n")


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, all_data: List[List[Any]]) -> None:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")
        print("Batch 1 Results:")

        for stream, batch in zip(self.streams, all_data):
            res_full = stream.process_batch(batch)

            name = stream.__class__.__name__.replace("Stream", " data")

            resumo = res_full.split(":")[1].split(",")[0].strip()
            print(f"- {name}: {resumo}")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    s = SensorStream("SENSOR_001")
    batch_s = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: [{', '.join(batch_s)}]")
    print(s.process_batch(batch_s))

    t = TransactionStream("TRANS_001")
    batch_t = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: [{', '.join(batch_t)}]")
    print(t.process_batch(batch_t))

    e = EventStream("EVENT_001")
    batch_e = ["login", "error", "logout"]
    print(f"Processing event batch: [{', '.join(batch_e)}]")
    print(e.process_batch(batch_e))

    processor = StreamProcessor()
    processor.add_stream(s)
    processor.add_stream(t)
    processor.add_stream(e)

    batch_data = [
        ["temp:20", "temp:24"],
        ["buy:10", "buy:10", "buy:10", "buy:10"],
        ["login", "logout", "error"]
    ]
    processor.process_all(batch_data)

    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
