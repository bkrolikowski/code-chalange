#
# Copyright (C) 2023 intive GmbH.
#
# All rights reserved Franz-Mayer-Straße 5, 93053 Regensburg,
# info@intive.com
#
import json
import yaml


class BMW:

    def __init__(self, configuration_file):
        if configuration_file[-4:] == "json":
            self.max_speed, self.color = self.extract_parameters_from_json(configuration_file)
        elif configuration_file[-4:] == "yaml":
            self.max_speed, self.color = self.extract_parameters_from_yaml(configuration_file)

    def extract_parameters_from_json(self, configuration_file):
        file = open(configuration_file, "r")
        config = json.load(file)
        print("Debug: Configuration loaded:", config)
        return config["bmw_max_speed"], config["bmw_color"]

    def extract_parameters_from_yaml(self, configuration_file):
        file = open(configuration_file, "r")
        config = yaml.safe_load(file)
        print("Debug: Configuration loaded:", config)
        return config["bmw_max_speed"], config["bmw_color"]

    def drive(self):
        print(f"Beep beep, I'm a {self.color} BMW and my maximum speed is {self.max_speed}km/h.")


class Mercedes:

    def __init__(self, configuration_file):
        file_extension = configuration_file[-4:]
        if file_extension == "json":
            self.max_speed, self.color = self.extract_parameters_from_json(configuration_file)
        elif file_extension == "yaml":
            self.max_speed, self.color = self.extract_parameters_from_yaml(configuration_file)

    def extract_parameters_from_json(self, configuration_file):
        file = open(configuration_file, "r")
        config = json.load(file)
        print("Debug: Configuration loaded:", config)
        return config["max_speed"], config["color"]

    def extract_parameters_from_yaml(self, configuration_file):
        file = open(configuration_file, "r")
        config = yaml.safe_load(file)
        print("Debug: Configuration loaded:", config)
        return config["max_speed"], config["color"]

    def drive(self):
        print(f"Beep beep, I'm a {self.color} Mercedes and my maximum speed is {self.max_speed}km/h.")


if __name__ == '__main__':
    cars = [BMW("cfg_bmw.yaml"), BMW("cfg_bmw.json"), Mercedes("cfg_mercedes.yaml"), Mercedes("cfg_mercedes.json")]
    for i in range(len(cars)):
        cars[i].drive()
