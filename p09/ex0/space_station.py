from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2024-03-20T10:00:00",
            notes="Operational"
        )
        print("Valid station created:")
        print(f"id: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        print(f"Status: {valid_station.notes}\n")
        print("=" * 40)

    except ValidationError as e:
        print(f"Expected validation error: \n{e}")

    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_mainenance="2024-03-20t10:00:00",
            notes="Operational"
        )
        print("Valid station created:")
        print(f"id: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size}")
        print(f"Power: {valid_station.power_level}")
        print(f"Oxygen: {valid_station.oxygen_level}")
        print(f"Status: {valid_station.notes}")
        print("=" * 40)

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
