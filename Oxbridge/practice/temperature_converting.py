#!/usr/bin/python
# Written on 13,7,2018 for in-class practice about selective control.
units = ['C', 'F']
full_names = {'C':'Celsius', 'F':'Fahrenheit'}
unit = raw_input('What unit atre you converting from?\n').upper()
temperature = float(raw_input('What is the temperature?\n'))
if unit in units:
    units.remove(unit)
    if unit == 'C':
        result = (9 / 5 * temperature) + 32
    elif unit == 'F':
        result = (temperature - 32) * 5 / 9

print('{original_temperature} degrees {original_unit} is {new_temperature} degrees {new_unit}.'.format(original_temperature=temperature,
                                                                                                       original_unit=full_names[unit],
                                                                                                       new_temperature=round(result, 3),
                                                                                                       new_unit=full_names[units[0]]))
