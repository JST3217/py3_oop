import random


RANDOM_SEED = 98
random.seed(RANDOM_SEED)  # This helps to reproduce results


class FriendlyName(object):
    color = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "purple", "pink"]
    verb = ["playing", "jumping", "eating", "working", "studying", "driving", "walking", "writing", "reading", "talking"]
    noun = ["Ava", "Brooklyn", "Charlotte", "Delilah", "Emma", "Faith", "Grace", "Henry", "Isaac", "James"]

    friendly_name_list = []

    def __init__(self):
        """
        The __init__ function is called automatically every time the class is instantiated.

        param :self: Represent the instance of the class
        return: a friendly name as an object
        """
        self.name = None
        self.counter = 1
        self.counter_limit = 3
        while self.name is None:
            self.temp_name = self.generate_friendly_name()
            if FriendlyName.is_unique(self.temp_name, FriendlyName.friendly_name_list):
                self.name = self.temp_name
                FriendlyName.friendly_name_list.append(self.name)
            elif self.counter < self.counter_limit and FriendlyName.is_unique(self.temp_name,
                                                                              FriendlyName.friendly_name_list) is False:
                print(f'non unique name generated, [{self.counter}/{self.counter_limit}] tries')
                self.counter += 1
            else:
                print('out of tries, obj cannot be generated.')
                return

    def __str__(self):
        return f'friendly name: {self.name}'

    def generate_friendly_name(self):
        """
        The generate_friendly_name function generates a friendly name.
        It chooses a color and a verb from lists of colors, verbs and names, respectively.
        Then it concatenates them together to form the friendly name.

        param self: Access variables that belongs to the class
        return: a friendly name as a string
        """
        self.color = random.choice(FriendlyName.color)
        self.verb  = random.choice(FriendlyName.verb)
        self.noun  = random.choice(FriendlyName.noun)
        return self.color + "-" + self.verb + "-" + self.noun

    @staticmethod
    def is_unique(friendly_name: str, friendly_name_list: list):
        """
        The is_unique function checks to see if the friendly name is already in use.
        If it is not, then True will be returned. If it is, False will be returned.

        param friendly_name: str: Check if the friendly_name has already been generated
        param friendly_name_list: list: A cumulative list of all the friendly_name generated
        return: True if the friendly_name is not in the friendly_name list
        """
        if (any(friendly_name_list) is False) or (friendly_name not in friendly_name_list):
            return True
        else:
            return False
