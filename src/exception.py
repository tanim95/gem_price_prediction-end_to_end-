import sys


def error_handling(error, err_details):
    exc_type, exc_value, exc_traceback = err_details
    detailed_message = {
        'error': str(error),
        'exception_type': exc_type.__name__,
        'exception_value': str(exc_value),
        'exception_traceback': exc_traceback,
        'filename': exc_traceback.tb_frame.f_code.co_filename,
        'line_number': exc_traceback.tb_lineno
    }
    return detailed_message


class Custom_exception (Exception):
    def __init__(self, detailed_message, details):
        super().__init__(detailed_message)
        self.error_message = error_handling(
            detailed_message, err_details=details)

    def __str__(self):
        return f"{self.error_message}"


if __name__ == "__main__":
    try:
        pass
    except Exception as e:
        raise Custom_exception(str(e), sys.exc_info())
