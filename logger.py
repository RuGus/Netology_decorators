from datetime import datetime

def logger(file_name = "log.txt"):
    def write_log(old_function):
        def logged_func(*args):
            result = old_function(*args)
            log_str = f"{datetime.now()}: {old_function.__name__}, params = {args}, result = {result}\n"
            with open(file_name, "a") as log_file:
                log_file.write(log_str)
            return result

        return logged_func
    return write_log