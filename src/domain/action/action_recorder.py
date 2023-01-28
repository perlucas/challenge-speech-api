from abc import ABC, abstractmethod
from domain.action.action import Action


class ActionRecorder(ABC):


    @abstractmethod
    def record_action(action: Action):
        pass



    @abstractmethod
    def dump():
        pass




class RepositoryRecorder(ActionRecorder):


    def __init__(self, save_actions):
        self.__collection = []
        self.__save_actions = save_actions



    def record_action(self, action: Action):
        self.__collection.append(action)


    def dump(self):
        self.__save_actions(self.__collection)