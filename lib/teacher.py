#!/usr/bin/env python
import random
from user import User

class Teacher(User):
    def __init__(self, first_name, last_name, knowledge=[]):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def teach(self):
        if self.knowledge:
            return random.choice(self.knowledge)
        return None
