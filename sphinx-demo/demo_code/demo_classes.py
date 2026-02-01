class InsufficientNumberError(Exception):
    """Exception raised when attempting to subtract more than available.

    Args:
        demo_number (float): Current demo number.
        amount (float): Attempted subtraction amount.

    Attributes:
        demo_number (float): Current balance.
        amount (float): Attempted amount of subtraction.
    """

    def __init__(self, demo_number: float, amount: float):
        self.demo_number = demo_number
        self.amount = amount
        super().__init__(f"Attempted to subtract {amount}, but demo number is {demo_number}.")

class DemoClass:
    """A simple class for demo purposes.

    Args:
        initial_demo_number (float): A description of the initial demo number that is passed on class initialization.

    Attributes:
        demo_number (float): A description of the class attribute that represents the demo number.
    """

    def __init__(self, initial_demo_number: float = 0.0):
        self.demo_number = initial_demo_number

    def add(self, amount: float):
        """Increases the demo number by specified amount.

        Args:
            amount (float): Amount to add.

        Returns:
            None
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self.demo_number += amount

    def subtract(self, amount: float):
        """Subtracts the specified amount from the demo number.

        Args:
            amount (float): Amount to subtract.

        Returns:
            None

        Raises:
            InsufficientNumberError: If the demo number is insufficient.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.demo_number:
            raise InsufficientNumberError(self.demo_number, amount)
        self.demo_number -= amount

    def get_demo_number(self) -> float:
        """Returns the current demo number.

        Returns:
            float: Current demo number.
        """
        return self.demo_number