class WordMatchResult:

    def __init__(self, words_to_match=list):
        self.__words = [w.lower() for w in words_to_match]
        self.__stats = {}
        for w in self.__words:
            self.__stats[ w ] = { "count": 0, "timestamps": [] }
    
    def add_word_timestamp(self, ts):
        if ts.word().lower() not in self.__words:
            return
        
        if ts.word() in self.__stats:
            current_stat = self.__stats[ ts.word() ]
            current_stat["count"] += 1
            current_stat["timestamps"].append(ts.timestamp())
            return
        
        self.__stats[ ts.word() ] = { "count": 1, "timestamps": [ts.timestamp()] }

    def to_json(self):
        arr = []
        for word, stats in self.__stats.items():
            arr.append({
                "word": word,
                "count": stats["count"],
                "timestamps": stats["timestamps"]
            })
        return { "results": arr}