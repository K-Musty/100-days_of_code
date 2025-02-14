# CODING EXERCISE
# Create your own decorator
import time

current_time = time.time()

def speed_calc_decorator(function):
    def run_speed():
        start_time = time.time()
        function()
        end_time = current_time
        time_difference = start_time - end_time

        print(f"{function.__name__}, speed: {time_difference}")

    run_speed()


@speed_calc_decorator
def test_speed():
    for i in range(1000000000):
        yes = i * i
        return yes



