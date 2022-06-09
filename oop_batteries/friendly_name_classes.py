import random


class FriendlyName:
    color = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "purple", "pink"]
    verb = ["playing", "jumping", "eating", "working", "studying", "driving", "walking", "writing", "reading", "talking"]
    noun = ["Ava", "Brooklyn", "Charlotte", "Delilah", "Emma", "Faith", "Grace", "Henry", "Isaac", "James"]

    friendly_name_list = []

    def __init__(self):
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
        return f'friendly name: {self.name} \n'

    def generate_friendly_name(self):
        self.color = random.choice(FriendlyName.color)
        self.verb  = random.choice(FriendlyName.verb)
        self.noun  = random.choice(FriendlyName.noun)
        return self.color + "-" + self.verb + "-" + self.noun

    @staticmethod
    def is_unique(friendly_name: str, friendly_name_list: list):
        if (any(friendly_name_list) is False) or (friendly_name not in friendly_name_list):
            return True
        else:
            return False
