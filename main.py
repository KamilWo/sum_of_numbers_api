from app.utils import sum_of_numbers
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "This is a REST API providing total value " \
           "of provided numbers. " \
           "To use it, access '/total' endpoint"


@app.get("/total")
async def total():
    """ Returns total of the provided numbers. """

    # This is an example list of numbers
    numbers_to_add = list(range(10000001))

    try:
        total_sum = {
            'total': sum_of_numbers(numbers_to_add)
        }
    except Exception as e:
        return f"Error: {e}"

    return total_sum
