import random
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
        self.env_values['mars_base_internal_temperature'] = random.uniform(18, 30)
        self.env_values['mars_base_external_temperature'] = random.uniform(0, 21)
        self.env_values['mars_base_internal_humidity'] = random.uniform(50, 60)
        self.env_values['mars_base_external_illuminance'] = random.uniform(500, 715)
        self.env_values['mars_base_internal_co2'] = random.uniform(0.02, 0.1)
        self.env_values['mars_base_internal_oxygen'] = random.uniform(4, 7)

    def get_env(self):
        log_entry = f"{datetime.now()}, "\
                    f"{self.env_values['mars_base_internal_temperature']:.2f} °C, "\
                    f"{self.env_values['mars_base_external_temperature']:.2f} °C, "\
                    f"{self.env_values['mars_base_internal_humidity']:.2f} %, "\
                    f"{self.env_values['mars_base_external_illuminance']:.2f} W/m2, "\
                    f"{self.env_values['mars_base_internal_co2']:.3f} %, "\
                    f"{self.env_values['mars_base_internal_oxygen']:.2f} %\n"

        with open('sensor_log.txt', 'a') as log_file:
            log_file.write(log_entry)

        return self.env_values


if __name__ == '__main__':
    ds = DummySensor()
    ds.set_env()
    sensor_values = ds.get_env()
    
    for key, value in sensor_values.items():
        print(f"{key}: {value:.2f}")
