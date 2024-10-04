from exceptions import InvalidInputError

# Function to get valid input from the user and handle errors
def get_valid_input(prompt, cast_type=float):
    while True:
        try:
            value = cast_type(input(prompt))
            if value < 0:
                raise InvalidInputError(f"{cast_type.__name__} value must be greater than or equal to 0.")
            return value
        except ValueError:
            print(f"Please enter a valid {cast_type.__name__} value.")
        except InvalidInputError as e:
            print(f"Error: {e}")
