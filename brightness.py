#!/usr/bin/env python3

import subprocess
import sys


def brightness_value():
    # get the output of the xrandr command
    output = subprocess.check_output(["xrandr", "--verbose"]).decode()
    # iterate over each line of the output
    for line in output.splitlines():
        # check if the line contains the string "Brightness:"
        if "Brightness:" in line:
            # return the value of the brightness as a float
            return float(line.split()[1])
    # if the brightness could not be found, return None
    return None


# sets the brightness of the monitor connected to HDMI-2
def set_brightness(brightness):
    subprocess.run(["xrandr", "--output", "HDMI-2",
                   "--brightness", str(brightness)])


def main():
    current_brightness = brightness_value()
    # check if the brightness could be found
    if current_brightness is None:
        print("Failed to get current brightness.")
        sys.exit(1)
    # check if the user passed an argument and if it is valid (up or down) 
    if len(sys.argv) != 2 or sys.argv[1] not in ["up", "down"]:
        print("Usage: brightness.py [up|down]")
        sys.exit(1)

    # increment the brightness by 0.1 or -0.1 depending on the argument
    increment = 0.1 if sys.argv[1] == "up" else -0.1
    new_brightness = max(0.1, min(0.9, current_brightness + increment))
    set_brightness(new_brightness)


if __name__ == "__main__":
    main()
