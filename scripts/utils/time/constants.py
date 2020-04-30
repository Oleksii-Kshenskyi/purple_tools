VALID_TIMESTRING_REGEX = r'^(\d)+:(\d)+:(\d)+$'

VALID_DURATION_REGEX = r'^(((\d)+[h|m|s]){0,1}){1,3}$'
FINDALL_DURATION_REGEX = r'((\d)+[h|m|s])'

TIME_UNIT_LENGTH_IN_SECONDS = 1500

UNIFORM_TIME_STRING = '[{} U @ {:02d}:{:02d}:{:02d}]'
LABELED_UNIFORM_TIME_STRING = '[{}: {} U @ {:02d}:{:02d}:{:02d}]'


UNIFORM_TIME_STRING_DEFAULT = UNIFORM_TIME_STRING.format(0, 0, 0, 0)
def labeled_uniform_time_string_default(label):
  return LABELED_UNIFORM_TIME_STRING.format(label, 0, 0, 0, 0)
DEFAULT_LABEL = 'WEIGHT'

ROUND_UNITS_TO = 3

# A section for sizes of different time units
SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60

# Various help messages and descriptions
TIME_COMMAND_DESCRIPTION = "Time command is responsible for various calculations related to time.\nOutputs time in the format of a time string of '[<P> U @ HH:MM:SS]', where:\n<P> is a floating point number of pomodoro units the HH:MM:SS time string is equal to."
TIME_ARGUMENTS_TIME_HELP = "Time to work with (one or more arguments expected).\nCan be either <HOURS>:<MINUTES>:<SECONDS> or <NO_OF_HOURS>h<NO_OF_MINUTES>m<NO_OF_SECONDS>s\nor <number_of_pomodoro_units>.\nNOTE: in the <H>h<M>m<S>s format, hours minutes and seconds can go in any preferred order,\nand some may be missing. So 1s1m3h or 4h3s or 3s would be just as valid as 4h2m10s."
TIME_ARGUMENTS_COMMAND_HELP = "Various subcommands the time command supports.\n\t=> print    | p: print either HH:MM:SS or <H>h<M>m<S>s or <P> as the [<P> U @ HH:MM:SS] time string.\n\t=> add      | a: add all the time values specified in the 'time' argument and print out\n\t                 the result as [<P> U @ HH:MM:SS].\n\t=> subtract | s: subtract time values from the one entered first and print out the\n\t                 result as [<P> U @ HH:MM:SS].\n\n"
TIME_ARGUMENTS_LABEL_HELP = f"Add a helper label for clarification, so the output time string transforms to \n[<label>: <P> U @ HH:MM:SS]. Default label is '{DEFAULT_LABEL}'."