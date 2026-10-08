from dataclasses import dataclass, field
from typing import Set

@dataclass
class Student:
    id: int
    name: str
    group: str            # "A" hoặc "B"
    sleep: float          # 21 đến 26 (26 nghĩa là 2h sáng)
    wake: float           # 5 đến 10
    tidy: int             # 1 đến 5
    study: str            # "phong", "thuvien", "it"
    noise: int            # 1 đến 5
    smoke: int            # 0 hoặc 1
    guests: int           # 1 đến 5
    hobbies: Set[str] = field(default_factory=set)
    top: str = "sleep"    # Tiêu chí quan trọng nhất
