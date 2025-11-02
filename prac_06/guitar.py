from __future__ import annotations
from datetime import date


class Guitar:
    """Represent a Guitar with name, year and cost."""

    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year=0):
        """Return how old the guitar is in years.
        If current_year is None, use the actual current calendar year.
        """
        if current_year is None:
            current_year = date.today().year
        return current_year - self.year

    def is_vintage(self, current_year=0):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age(current_year) >= 50