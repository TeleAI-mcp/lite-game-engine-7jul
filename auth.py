"""
Authentication module for the Lite Game Engine.
"""

class AuthManager:
    """Manages user authentication and authorization."""
    
    def __init__(self):
        self.users = {}
    
    def authenticate(self, username: str, password: str) -> bool:
        """Authenticate a user."""
        return username in self.users and self.users[username] == password
    
    def register(self, username: str, password: str) -> bool:
        """Register a new user."""
        if username in self.users:
            return False
        self.users[username] = password
        return True
