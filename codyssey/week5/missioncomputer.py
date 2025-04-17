import random
import time
import platform
import os
from datetime import datetime


class DummySensor:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': None,
            'mars_base_external_temperature': None,
            'mars_base_internal_humidity': None,
            'mars_base_external_illuminance': None,
            'mars_base_internal_co2': None,
            'mars_base_internal_oxygen': None
        }

    def set_env(self):
        self.env_values['mars_base_internal_temperature'] = round(random.uniform(18, 30), 2)
        self.env_values['mars_base_external_temperature'] = round(random.uniform(0, 21), 2)
        self.env_values['mars_base_internal_humidity'] = round(random.uniform(50, 60), 2)
        self.env_values['mars_base_external_illuminance'] = round(random.uniform(500, 715), 2)
        self.env_values['mars_base_internal_co2'] = round(random.uniform(0.02, 0.1), 2)
        self.env_values['mars_base_internal_oxygen'] = round(random.uniform(4, 7), 2)

    def get_env(self):
        return self.env_values


class MissionComputer:
    def __init__(self):
        self.ds = DummySensor()
        self.data_history = []

    def get_mission_computer_info(self):
        try:
            system_info = {
                'operating_system': platform.system(),
                'os_version': platform.version(),
                'cpu_type': platform.processor(),
                'cpu_core_count': os.cpu_count(),
            }
            for key, value in system_info.items():
                print(f"{key}: {value}")
            print('-' * 30)
        except Exception as e:
            print(f"error: {str(e)}")

    def get_mission_computer_load(self):
        try:
            if platform.system() == 'Windows':
                load = os.getloadavg() if hasattr(os, 'getloadavg') else ('N/A', 'N/A', 'N/A')
            else:
                load = os.getloadavg()

            print(f"1 min load average: {load[0]}")
            print(f"5 min load average: {load[1]}")
            print(f"15 min load average: {load[2]}")
            print('-' * 30)
        except Exception as e:
            print(f"error: {str(e)}")

    def get_sensor_data(self):
        count = 1
        start_time = time.time()

        try:
            while True:
                print("Mission Computer Information:")
                self.get_mission_computer_info()

                print("Mission Computer Load:")
                self.get_mission_computer_load()

                self.ds.set_env()
                env_values = self.ds.get_env()
                self.data_history.append(env_values.copy())

                print(f"Sensor Measurement Number: {count}")
                for key, value in env_values.items():
                    print(f"{key}: {value:.2f}")
                print('-' * 30)

                if time.time() - start_time >= 300:  # 5 minutes
                    avg_values = {key: round(sum(d[key] for d in self.data_history) / len(self.data_history), 2)
                                  for key in env_values}
                    print("5-minute average values:")
                    for key, value in avg_values.items():
                        print(f"{key}: {value:.2f}")
                    print('=' * 30)

                    self.data_history.clear()
                    start_time = time.time()
                    count = 0

                count += 1
                time.sleep(5)
        except KeyboardInterrupt:
            print('System stopped...')


if __name__ == '__main__':
    RunComputer = MissionComputer()
    RunComputer.get_sensor_data()