#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python TC 7 

@author: Yiyang Wang 999028285
python-winter-2024
"""


def is_valid_line(line: str) -> bool:
    """
    Checks if a line is valid.
    A valid line contains a number followed by a unit (C, F, or K).

    Args:
        line (str): A line from the temperature file.

    Returns:
        bool: True if the line is valid, False otherwise.
    """
    line = line.strip()
    if not line:
        return False
    if line[-1] not in "CFK":
        return False
    try:
        float(line[:-1])  # Check if the numeric part can be converted to float
        return True
    except ValueError:
        return False


def convert_to_celsius(line: str) -> float:
    """
    Converts a valid temperature line to Celsius.

    Args:
        line (str): A valid line from the temperature file.

    Returns:
        float: The temperature in Celsius.
    """
    line = line.strip()
    value = float(line[:-1])  # Extract numeric part
    unit = line[-1]  # Extract unit

    if unit == "C":
        return value
    elif unit == "F":
        return (value - 32) * 5.0 / 9.0
    elif unit == "K":
        return value - 273.15


def calculate_max(values: list[float]) -> float:
    """
    Returns the maximum value from a list of temperatures.

    Args:
        values (list[float]): A list of temperatures in Celsius.

    Returns:
        float: The maximum temperature.
    """
    return max(values)


def calculate_min(values: list[float]) -> float:
    """
    Returns the minimum value from a list of temperatures.

    Args:
        values (list[float]): A list of temperatures in Celsius.

    Returns:
        float: The minimum temperature.
    """
    return min(values)


def calculate_mean(values: list[float]) -> float:
    """
    Returns the average value from a list of temperatures.

    Args:
        values (list[float]): A list of temperatures in Celsius.

    Returns:
        float: The average temperature.
    """
    return sum(values) / len(values)


def main():
    """
    This function reads temperatures from a file, and calculates the max, min and mean in Celsius.

    The temperature file will contain temperature with its units (C,K,F), for example:
        - 25F
        - 32C
        - 200K

    The results are saved into a new file.
    """
    input_filename = "temperatures.txt"
    file_input = open(input_filename, "r")

    # Read and process the file
    valid_temperatures = []
    for line in file_input:
        if is_valid_line(line):
            temperature_in_celsius = convert_to_celsius(line)
            valid_temperatures.append(temperature_in_celsius)

    file_input.close()

    # Calculate values
    max_temp = calculate_max(valid_temperatures)
    min_temp = calculate_min(valid_temperatures)
    avg_temp = calculate_mean(valid_temperatures)

    # Save the results to a file
    output_filename = "temperatures_results.txt"
    file_output = open(output_filename, "w")
    file_output.write(f"Maximum Temperature: {max_temp:.2f} C\n")
    file_output.write(f"Minimum Temperature: {min_temp:.2f} C\n")
    file_output.write(f"Average Temperature: {avg_temp:.2f} C\n")
    file_output.close()  # Close the file when you finish writing


# once you have everything defined you can run the main() function to read and write the results.
main()