"""
Capy UI Theme Demo - Python
This file demonstrates Python syntax highlighting.
"""

from typing import List, Dict, Optional, Union
import asyncio
import re

# Constants
API_BASE_URL = "https://api.example.com"
MAX_RETRIES = 3

class ThemeManager:
    """
    A class to manage theme configurations.
    Demonstrates class definitions and methods.
    """
    
    def __init__(self, theme: str, accent_color: str):
        self.theme = theme
        self.accent_color = accent_color
        self._is_initialized = False
    
    @property
    def is_dark_mode(self) -> bool:
        """Check if dark mode is enabled."""
        return self.theme == "dark"
    
    @staticmethod
    def get_default_config() -> Dict[str, Union[str, bool]]:
        """Return default configuration."""
        return {
            "theme": "dark",
            "accent_color": "#1e80c7",
            "enable_animations": True
        }
    
    def apply_theme(self) -> None:
        """Apply the current theme configuration."""
        print(f"Applying theme: {self.theme}")
        self._is_initialized = True


async def fetch_user_data(user_id: int) -> Optional[Dict]:
    """
    Fetch user data asynchronously.
    Demonstrates async/await and error handling.
    """
    try:
        # Simulate API call
        await asyncio.sleep(0.1)
        
        if user_id < 0:
            raise ValueError("User ID must be positive")
        
        return {
            "id": user_id,
            "name": "Capy User",
            "email": f"user{user_id}@example.com"
        }
    except Exception as e:
        print(f"Error fetching user data: {e}")
        return None


def process_data(items: List[int]) -> List[int]:
    """
    Process a list of numbers.
    Demonstrates list comprehensions and functional programming.
    """
    # Filter even numbers and square them
    squared = [x ** 2 for x in items if x % 2 == 0]
    
    # Use map and filter
    doubled = list(map(lambda x: x * 2, filter(lambda x: x > 5, squared)))
    
    return doubled


# Regular expressions
EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def is_valid_email(email: str) -> bool:
    """Validate email address."""
    return bool(EMAIL_PATTERN.match(email))


# Decorators
def log_execution(func):
    """Decorator to log function execution."""
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper


@log_execution
def calculate_sum(numbers: List[int]) -> int:
    """Calculate sum with logging."""
    return sum(numbers)


# Dictionary and set operations
color_palette = {
    "primary": "#1e80c7",
    "background": "#1c1d21",
    "success": "#00ba7c",
    "error": "#f91880",
    "warning": "#ffac33"
}

# Set operations
tags = {"python", "theme", "vscode"}
new_tags = tags | {"dark", "blue"}

# String formatting
theme_name = "Capy UI"
message = f"""
Welcome to {theme_name}!
Electric blue accent: {color_palette['primary']}
Total colors: {len(color_palette)}
"""

# Context manager
class ThemeContext:
    def __enter__(self):
        print("Entering theme context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting theme context")
        return False


# Main execution
if __name__ == "__main__":
    manager = ThemeManager("dark", "#1e80c7")
    manager.apply_theme()
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = process_data(numbers)
    print(f"Processed data: {result}")
    
    # Using context manager
    with ThemeContext():
        print("Working with theme...")
