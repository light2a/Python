from dataclasses import dataclass, field


def average(values: list[float  ]) -> float:
    """Calculates the average of a list of numbers."""
    if not values:
        raise ValueError("The list is empty, cannot compute average.")
    return sum(values) / len(values) 

@dataclass
class Candidate:
    name: str
    scores: list[float]  = field(default_factory=list)

    def mean_score(self) -> float:
        """Calculates the mean score of the candidate."""
        return average(self.scores)

a = Candidate("An", [8, 9, 10])
print(f"{a.name}: {a.mean_score():.1f}")

b = Candidate("Binh")
try:
    b.mean_score()
except ValueError as e:
    print(f"Lỗi: {e}")    