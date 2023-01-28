from flask import Flask, json, request
from domain.audio.transcriber import GoogleSpeechAPITranscriber
from domain.audio.audio import GoogleBucketAudio
from domain.action.action_recorder import RepositoryRecorder
from impl.mongo_repository import save_actions, fetch_actions
from domain.action.action import Action
from impl.errors import ErrorBoundary
from impl.auth import get_current_user

app = Flask(__name__)

@app.route("/")
def hello():
    response = json.dumps({"message": "Hello World!"})
    return response


@app.route("/scan", methods = ["POST"])
def scan_audio():
    with ErrorBoundary() as error_context:
        user = get_current_user(request.headers)

        recorder = RepositoryRecorder(save_actions=save_actions)
        recorder.record_action(Action.new_access(user=user, endpoint='POST /scan'))        

        body = request.json
        file_uri, words = body['file'], body['words']

        recorder.record_action(Action.new_scan(words, file=file_uri))

        transcriber = GoogleSpeechAPITranscriber()
        audio = GoogleBucketAudio(file_uri)
        audio_transcription = transcriber.transcribe(audio)

        recorder.record_action(Action.new_results(words, file=file_uri))

        word_matches = audio_transcription.compute_word_matches(words)

        response = json.dumps(
            word_matches.to_json()
        )

        recorder.dump()
    
    if error_context.has_error():
        response = json.dumps(error_context.error_to_json())
        return response, 500

    return response


@app.route("/logs", methods = ["GET"])
def get_logs():
    with ErrorBoundary() as error_context:
        user = get_current_user(request.headers)

        recorder = RepositoryRecorder(save_actions=save_actions)
        recorder.record_action(Action.new_access(user=user, endpoint='GET /logs'))   

        actions = fetch_actions(request.args)

        response = json.dumps({
            "logs": [a.to_json() for a in actions],
            "page": 1,
            "page_size": 50
            # TODO: implement pagination feature
        })

        recorder.dump()

    if error_context.has_error():
        response = json.dumps(error_context.error_to_json())
        return response, 500

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)