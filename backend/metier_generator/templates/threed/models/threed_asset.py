"""
Module métier Python avancé
Contient les classes User, Project, Permission pour la logique métier et les tests.
"""


class User:
    def __init__(self, username, email, is_active=True):
        self.username = username
        self.email = email
        self.is_active = is_active


class Project:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner


class Permission:
    def __init__(self, user, project, level):
        self.user = user
        self.project = project
        self.level = level
