VALID_TIMESTRING_REGEX = r'^(\d)+:(\d)+:(\d)+$'

VALID_DURATION_REGEX = r'^(((\d)+[h|m|s]){0,1}){1,3}$'
FINDALL_DURATION_REGEX = r'((\d)+[h|m|s])'

TIME_UNIT_LENGTH_IN_SECONDS = 1500

UNIFORM_TIME_STRING = '[{} U @ {:02d}:{:02d}:{:02d}]'

UNIFORM_TIME_STRING_DEFAULT = UNIFORM_TIME_STRING.format(0, 0, 0, 0)

ROUND_UNITS_TO = 3

# A section for sizes of different time units
SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60

# Various help messages and descriptions
TIME_COMMAND_DESCRIPTION = "Time command is responsible for various calculations related to time.\nOutputs time in the format of a time string of '[<P> U @ HH:MM:SS]', where:\n<P> is a floating point number of pomodoro units the HH:MM:SS time string is equal to."
TIME_ARGUMENTS_TIME_HELP = "Time to work with (one or more arguments expected).\nCan be either <HOURS>:<MINUTES>:<SECONDS> or <number_of_pomodoro_units>."
TIME_ARGUMENTS_COMMAND_HELP = "Various subcommands the time command supports.\n\t=> print | p: print either HH:MM:SS or <P> as the [<P> U @ HH:MM:SS] time string."