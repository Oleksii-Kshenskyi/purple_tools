VALID_TIMESTRING_REGEX = r'^(\d)+:(\d)+:(\d)+$'

TIME_UNIT_LENGTH_IN_SECONDS = 1500

UNIFORM_TIME_STRING = '[{} U @ {:02d}:{:02d}:{:02d}]'

UNIFORM_TIME_STRING_DEFAULT = UNIFORM_TIME_STRING.format(0, 0, 0, 0)

ROUND_UNITS_TO = 3

# A section for sizes of different time units
SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60

# Various help messages and descriptions
TIME_COMMAND_DESCRIPTION = "Time command is responsible for various calculations related to time."
TIME_PRINT_COMMAND_DESCRIPTION = "Prints out a universal time string of '[X U @ HH:MM:SS]' format, where X is a floating point number of pomodoro units the HH:MM:SS time string is equal to."
TIME_PRINT_ARGUMENTS_TIME_HELP = """Time units to print out (one or more arguments expected). Can be of the following format:\n
- HH:MM:SS - where HH is the amount of hours, MM is the amount of minutes, SS is the amount of seconds in the time string;
- <number> - a number of Pomodoro units. Can be either an integer or a floating point number.
"""