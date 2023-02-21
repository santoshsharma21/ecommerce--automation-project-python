# import libraries
import random
import string


class Utils:
    # random data generator
    @staticmethod
    def random_data_generator(size=8, chars=string.ascii_lowercase + string.digits):
        random_string = ''.join(random.choice(chars) for _ in range(size))
        return random_string
