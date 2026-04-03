from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import List
from enum import Enum


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_safety(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        has_leadership = any(
            m.rank in [Rank.captain, Rank.commander] for m in self.crew)
        if not has_leadership:
            raise ValueError("Mission must have at "
                             "least one Commander or Captain")

        if self.duration_days > 365:
            exp_count = sum(1 for m in self.crew if m.years_experience >= 5)
            if exp_count < (len(self.crew) / 2):
                raise ValueError("Long mission need 50% "
                                 "experience crew (5+ years)")
        if not all(m.is_active for m in self.crew):
            raise ValueError('All crew members must be active')

        return self


def main():
    print("Space Mission Crew Validation")
    print("=" * 40)

    commander = CrewMember(
        member_id="CMD01",
        name="Sarah Connor",
        rank=Rank.commander,
        age=45, specialization="Mission Command",
        years_experience=20
    )
    pilot = CrewMember(
        member_id="PLT02",
        name="John Smith",
        rank=Rank.lieutenant,
        age=30, specialization="Navigation",
        years_experience=8
    )
    engineer = CrewMember(
        member_id="ENG03",
        name="Alice Johnson",
        rank=Rank.officer,
        age=28,
        specialization="Engineering",
        years_experience=4
        )
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-06-01T08:00:00",
            duration_days=900,
            crew=[commander, pilot, engineer],
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for m in mission.crew:
            print(f"- {m.name} ({m.rank.value}) - {m.specialization}")

    except ValidationError as e:
        print(f"Error: {e}")
    print()
    print("=" * 40)

    try:
        SpaceMission(
            mission_id="M_FAIL",
            mission_name="Unsupervised Mission",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=10,
            crew=[pilot],
            budget_millions=100.0
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            msg = error['msg'].split(", ", 1)[-1]
            print(msg)


if __name__ == "__main__":
    main()
