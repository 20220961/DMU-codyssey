import random
import time
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
        self.env_values = {}
        self.ds = DummySensor()
        self.data_history = []

    def get_sensor_data(self):
        count = 1
        start_time = time.time()

        try:
            while True:
                self.ds.set_env()
                self.env_values = self.ds.get_env()
                self.data_history.append(self.env_values.copy())
                
                print(f"측정 번호: {count}")
                for key, value in self.env_values.items():
                    print(f"{key}: {value:.2f}")
                print('-' * 30)

                if time.time() - start_time >= 300:  # 5분
                    avg_values = {key: round(sum(d[key] for d in self.data_history) / len(self.data_history), 2)
                                  for key in self.env_values}
                    print("5분 평균값:")
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