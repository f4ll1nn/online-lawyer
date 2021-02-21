""" Module of realization Person ADT"""
class Person:
    """ Class of main persons in situations """

    def __init__(self, name: str, actions=None) -> None:
        """ Creates person """
        self.name = name
        self.actions = actions

    def define_actions(self) -> None:
        """ Define actions of this person """
        pass
