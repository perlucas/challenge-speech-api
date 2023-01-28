class ErrorBoundary:
    def __init__(self):
        self.__error = None

    def __enter__(self):
        return self
    
    def __exit__(self, e_type, e_value, e_traceback):
        print("executed error boundary context with {}".format(e_type))
        self.__error = e_value
        return True

    def has_error(self) -> bool:
        return not self.__error is None

    def error_to_json(self) -> dict:
        return { "message": self.__error.message if hasattr(self.__error, 'message') else str(self.__error) }