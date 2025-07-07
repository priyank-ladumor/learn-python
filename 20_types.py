name: str = "Alice"
age: int = 30
height: float = 5.9
is_active: bool = True

def greet(name: str) -> str:
    return f"Hello, {name}"

def add(x: int, y: int) -> int:
    return x + y

print(greet(name))

from typing import Optional, Union

def get_user_name(user_id: int) -> Optional[str]:
    # might return a string or None
    return "Alice" if user_id == 1 else None

def process(value: Union[int, str]) -> str:
    return str(value)

from typing import List, Dict, Tuple

names: List[str] = ["Alice", "Bob"]
scores: Dict[str, int] = {"Alice": 95, "Bob": 88}
coords: Tuple[float, float] = (45.0, 90.0)

