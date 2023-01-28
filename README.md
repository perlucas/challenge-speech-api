# Speech Recognition Test API
Basic REST API for transcribing and finding specified words within MP3 audio files:
- Based on the Google Speech API solution
- Built in Python 3 and MongoDB
- Built using a Docker multi-container environment

## Set up instructions
1. Clone this repository
2. Create a `credentials.json` file under the root directory, containing the Google Cloud credentials
3. Create a `.env` file (rename the provided example) 
4. Run `docker compose up --build`
5. Test this API in `localhost:85/`

## API endpoints & examples

### __`POST /scan`__
_Given a MP3 audio file and a set of words, processes the given file and looks up the words in the transcription. Returns the number of ocurrences and timestamps found for each word._

JSON body examples:
```
{
	"file": "gs://speech-api-test-2344/PartyAnimal.mp3",
	"words": [
		"party",
		"not",
		"people"
	]
}
```
```
{
	"file": "gs://speech-api-test-2344/GreetingsandIntroductions.mp3",
	"words": [
		"athlete",
		"architect",
		"people"
	]
}
```
```
{
	"file": "gs://speech-api-test-2344/AirPollution.mp3",
	"words": [
		"pollution",
		"think",
		"people"
	]
}
```
HTTP 200 Response examples:
```
{
	"results": [
		{
			"count": 5,
			"timestamps": [
				"00:00:12.1",
				"00:00:14.8",
				"00:00:16.3",
				"00:00:33.8",
				"00:00:59.2"
			],
			"word": "pollution"
		},
		{
			"count": 1,
			"timestamps": [
				"00:00:10.6"
			],
			"word": "think"
		},
		{
			"count": 0,
			"timestamps": [],
			"word": "people"
		}
	]
}
```
HTTP 500 Response examples:
```
{
	"message": "No such object: speech-api-test-2344/Greetings and Introductions Basi.mp3"
}
```
### __`GET /logs`__
_Returns the latest logged in actions for this API._

HTTP 200 Response examples:
```
{
	"logs": [
		{
			"metadata": {
				"endpoint": "GET /logs",
				"user": "tester"
			},
			"timestamp": "2023-01-28 16:06:22",
			"type": "ACTION_APP_ACCESS"
		},
		{
			"metadata": {
				"endpoint": "POST /scan",
				"user": "tester"
			},
			"timestamp": "2023-01-28 16:06:22",
			"type": "ACTION_APP_ACCESS"
		},
		{
			"metadata": {
				"file": "gs://speech-api-test-2344/PartyAnimal.mp3",
				"words": [
					"party",
					"not",
					"people"
				]
			},
			"timestamp": "2023-01-28 16:06:22",
			"type": "ACTION_SCAN_AUDIO"
		},
	],
	"page": 1,
	"page_size": 50
}
```

## TODO's
The following list contains additional features and capabilities that I've decided not to include in the current task's scope so as not to extend its delivery unnecessarily:
- Implement basic data parameters validation:
    - validate that _words_ is a list of strings
    - validate the _file_ parameter
- Add basic authentication by username and password
- Allow API users to configure audio scanning parameters such as audio language and rate in Hertz
- Implement pagination for logs endpoint
- Implement logs filtering on action type, users, timestamp and metadata
- Run this API using an isolated WSGI server running in its own container instead of using the Flask development server