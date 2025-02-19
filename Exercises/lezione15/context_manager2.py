from typing import Any

class Timer:

    def __enter__(self):
        import time

        self.time = time.time()

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any):

        import time

        print(f'Time Elapsed: {time.time() - self.time}')


with Timer():

    import time

    time.sleep()