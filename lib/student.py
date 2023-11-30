#!/usr/bin/env python

from user import User

class Student(User):
    

    def learn(self, knowledge_string):
        self.knowledge = []
        self.knowledge.append(knowledge_string)