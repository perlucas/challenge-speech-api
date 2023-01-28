from impl.get_database import db
from domain.action.action import Action
from pymongo import DESCENDING

def __action_to_document(action: Action):

    return {
        "user": 1,
        "timestamp": action.timestamp(),
        "type": action.action_type(),
        "metadata": action.metadata()
    }


def save_actions(actions: list):

    if len(actions) == 0:
        return

    collection = db["actions"]
    collection.insert_many(
        [__action_to_document(a) for a in actions]
    )


def __document_to_action(doc):
    print(doc)
    return Action(type=doc['type'],
                    metadata=doc['metadata'],
                    ts=doc['timestamp'])


def fetch_actions(criteria: dict):
    # TODO: allow support for query string filters/sorting passed in as criteria
    collection = db["actions"]
    cursor = collection.find(
        limit=50, 
        sort=[('timestamp', DESCENDING)])
    
    return [__document_to_action(doc) for doc in cursor]