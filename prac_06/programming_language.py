class ProgrammingLanguage:
    """Represent a programming language with typing, reflection support, and first appearance year."""

    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if this language uses dynamic typing."""
        return self.typing.strip().lower() == "dynamic"

    def __str__(self):
        """Return a readable string for this language."""
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection={self.reflection}, First appeared in {self.year}")