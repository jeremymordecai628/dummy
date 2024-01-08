#!/usr/bin/python3
"""
Defines the BaseModel class.
"""

from uuid
from Datetime import Datetime

class BaseModel :
    def __init__ (self):
        self.id=str(uuid.uuid4())

        self.created_at = datetime.utcnow.()
        self.updated_at = datetime.utcnow.()

    def save(self):
        """
        Update updated_at with the current datetime.
        """
        self.updated_at = datetime.utcnow.()
