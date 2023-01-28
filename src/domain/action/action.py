from datetime import datetime
from domain.user import User

NEW_SCAN_TYPE = 'ACTION_SCAN_AUDIO'
NEW_RESULTS_TYPE = 'ACTION_GOT_RESULTS'
NEW_ACCESS_TYPE = 'ACTION_APP_ACCESS'

class Action:
    
    def __init__(self, type: str, metadata = {}, ts = None):
        self.__type = type
        self.__metadata = metadata
        self.__timestamp = datetime.now() if ts is None else ts

    def metadata(self):
        return self.__metadata

    def timestamp(self):
        return self.__timestamp

    def action_type(self):
        return self.__type

    def to_json(self):
        return {
            "type": self.__type,
            "metadata": self.__metadata,
            "timestamp": self.__timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }


    def new_scan(words: list, file: str):
        return Action(type=NEW_SCAN_TYPE, metadata={'words': words, 'file': file})

    def new_results(words: list, file: str):
        return Action(type=NEW_RESULTS_TYPE, metadata={'words': words, 'file': file})

    def new_access(user: User, endpoint: str):
        return Action(type=NEW_ACCESS_TYPE, metadata={'user': user.get_username(), 'endpoint': endpoint})
    
    