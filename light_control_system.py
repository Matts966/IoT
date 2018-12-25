import control_light
import motion_sensor
import datetime

def main():
    ms = motion_sensor(
        delay_from_last_motion = datetime.timedelta(second=3),
        on_callback = control_light.light_on,
        off_callback = control_light.light_off
    )
    ms.start()

if __name__ == '__main__':
    main()
