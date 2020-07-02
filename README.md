# Purple Tools

This is a collection of various Python automation scripts I use daily in my work and life. 

## A small note on licensing

Purple Tools is licensed under BSD 0-clause license. This means that you are free to do **whatever you want** with the application. You **don't have any obligations** if you want to use Purple tools. You don't even have to reproduce any copyright notices in your code if you're using the code from Purple Tools in your projects (like you would have had to if it was under MIT for example). Enjoy!

## What can it do?
- Time calculations
  - Convert between the amount of pomodoro units and time in various formats;
  - Add times and show results in a uniform format;
  - Subtract times and show results in a uniform format;
  - Add some label to the resulting time string for clarification.
- Unit testing itself
  - unit test the application with one command;
  - perform exploratory tests with one command.
- Calculate parameters of arithmetic progressions
  - Given an integer number (progression sum limiter), and assuming that the first element and the step of the arithmetic progression is equal to 1, calculate the last element of the progression and the sum of the progression, outputting the last element and the sum-to-limiter remainder;
  - Given the lower and the upper bounds of an arithmetic progression (both ints, upper bound <= lower bound), and assuming that the step of the progression is 1, calculate the sum of such progression.

  ## Some examples

  ### Time calculations

  `$ python purple.py time print 30` or `python purple.py t p 30`

  `[30 U @ 12:30:00]` <- outputs time in pomodoro units, assuming 1 U == 00:25:00

  `$ python purple.py time print 30h` or `$ python purple.py t p 30h`

  `[72 U @ 30:00:00]` <- 30 hours in pomodoro units

  `$ python purple.py time print 3000s100m1h` or `python purple.py t p 3000s100m1h`

  `[8.4 U @ 03:30:00]` <- doesn't care about the amount of seconds/minutes being < 60, will properly convert to a `[<Pomodoro units> U @ <HH>:<MM>:<SS>]` time string, this can be used for any conversions e.g. "How much is a 1000 seconds? etc.

  `$ python purple.py time print 0:3000:0` or `python purple.py t p 0:3000:0`

  `[120 U @ 50:00:00]` <- 0:3000:0 is the same as 3000m, will properly convert to a uniform time string and show the result

  `$ python purple.py time print 4:3:2` or `python purple.py t p 4:3:2`

  `[9.721 U @ 04:03:02]` <- doesn't care about the amount of zeroes in the time value, will properly convert to a uniform time string

  `$ python purple.py time print 3h --label "Grocery store"` or `python purple.py t p 3h -l "Grocery store"`

  `[Grocery store: 7.2 U @ 03:00:00]` <- includes a non-default label with a short explanation regarding what the time is about

  `$ python purple.py time print 3h --label` or `python purple.py t p 3h -l`

  `[WEIGHT: 7.2 U @ 03:00:00]` <- default label is "WEIGHT"

  `$ python purple.py time subtract 30h 4:3:2 10` or `python purple.py t s 30h 4:3:2 10`

  `[52.279 U @ 21:46:58]` <- will properly convert `30h` to `[72 U @ 30:00:00]`, `4:3:2` to `[9.721 U @ 04:03:02]` and `10` to `[10 U @ 04:10:00]` and subtract `4:3:2` and `10` from `30h`.

  `$ python purple.py time subtract 1h 2h30m` or `python purple.py t s 1h 2h30m`

  `[-3.6 U @ -2:30:00]` <- known bug, this happens due to how timedelta internally works in Python. This can be easily fixed by using Python's builtin abs() function for taking an absolute value of the subtraction result. Refer to issue [#36](https://github.com/Oleksii-Kshenskyi/purple_tools/issues/36) for details.

  `$ python purple.py time subtract 1h` or `python purple.py t s 1h`

  `[2.4 U @ 01:00:00]` <- subtract with one argument behaves exactly like a print would, just prints out the value.

  `$ python purple.py time add 1h 1s1m 3:1:2 2` or `python purple.py t a 1h 1s1m 3:1:2 2`

  `[11.682 U @ 04:52:03]` <- add times in various formats, correctly converts them into Python's timedelta internally and prints out the result in the uniform time string format of Purple Tools.

  `$ python purple.py time add 1h` or `python purple.py t a 1h`

  `[2.4 U @ 01:00:00]` <- add with one argument behaves exactly like a print would, just prints out the value.

  ### Testing

  `$ python purple.py test unit` or `$ python purple.py ts u`

  *runs all unit tests, currently 41 of them, to test the application*

  `$ python purple.py test exploratory` or `$ python purple.py ts e`

  *runs all exploratory tests, to test some of the assertions and assumptions about Python I had while developing Purple Tools*

  ### Calculating arithmetic progressions

  `$ python purple.py calculate progression --by-limiter 100` or `$ python purple.py c pr -l 100`

  ```
  The progression is: 1 .. 13
  Limiter-to-sum remainder: 9
  ```
  ^ calculates an arithmetic progression's parameters where sum of all elements <= specified integer limiter, first element and step == 1. Calculates the last element (13 in this example) and the limiter-to-sum remainder. From this, one could see that the actual sum of the progression was `<limiter> - <remainder>` == `100 - 9` == `91` in this case.

  `$ python purple.py calculate progression --by-limiter 350000000000000000000000000` or `$ python purple.py c pr -l 350000000000000000000000000`

  ```
  The progression is: 1 .. 26457513110645
  Limiter-to-sum remainder: 10739237286665
  ```

  ^ doesn't care about how big the specified limiter is, always calculates progression parameters correctly. You could check that by calculating the actual sum via `350000000000000000000000000 - 10739237286665` and then running the same command on the resulting value (remainder should be 0):
  `$ python purple.py c pr -l 349999999999989260762713335`

  ```
  The progression is: 1 .. 26457513110645
  Limiter-to-sum remainder: 0
  ```

  `$ python purple.py calculate progression --by-bounds 3 100` or `python purple.py c pr -b 3 100`

  `sum(3 .. 100) = 5047` <- calculates the sum of an arithmetic progression specified by first element 3 and last element 100.

  `$ python purple.py calculate progression --by-bounds 1 20000000000` or `$ python purple.py c pr -b 1 20000000000`

  ```
  sum(1 .. 20000000000) = 200000000010000007168
                                           ^^^^
  ```

  This is a known bug (see issue [#38](https://github.com/Oleksii-Kshenskyi/purple_tools/issues/38)) where some of the last digits in the sum in the `--by-bounds` case will be calculated incorrectly. This happens due to `--by-bounds`'s reliance on floats. In the future this will have to be rewritten into using purely Python's unlimited int as `--by-limiter` already does.

  ## Additional help

  There are also quite a few extensive help messages in Purple Tools itself in case this help is not enough.

  `$ python purple.py -h` <- General help for the entire Purple Tools project

  `$ python purple.py test -h` <- help with the test module

  `$ python purple.py time -h` <- help with the time module

  `$ python purple.py calculate -h` <- help with the calculate module

  `$ python purple.py calculate progression -h` <- help with the progression module

  ^ Remember that you can also use short module names like `t` for `time`, `ts` for `test`, `c` for `calculate` and `pr` for `progression`.

  **NOTE** these help messages will only work **after** you set the `PT_PROJECT_DIR` environment variable. Read below for details.

  ## How to start using it?

  Purple Tools works on any system where there is a Python >= 3.6.8 interpreter available. To run it successfully:
  - Install Python >= 3.6.8 (`sudo pacman -S python` on Manjaro/Arch, `sudo yum install python3` on CentOS 7, install via [official website](https://www.python.org/downloads/) on Windows, etc.)
  - git clone https://github.com/Oleksii-Kshenskyi/purple_tools.git
  - Set environment variable `PT_PROJECT_DIR` to `<cloned repo\'s root folder>`
  - For convenience, I usually set a couple of aliases in my ~/.bashrc config file and run those via Bash afterwards:
    ```bash
    export PT=<your Purple Tools repo root folder>
    export PT_PROJECT_DIR=$PT
    alias purple="python purple.py"
    ```
    `$ source ~/.bashrc`

    From this point, you can simply use `purple` instead of the full `python purple.py` to run Purple Tools.
  - If you're on a system that does not have a Bash by default, e.g. Windows etc., you could install a bash as the first step. On Windows, I usually use either [Cmder](https://cmder.net/) or [Git Bash](https://git-scm.com/download/win).

  ## The 2020 Challenge

  For precise statistics on estimations and time spent on this project, please refer to issue [#25](https://github.com/Oleksii-Kshenskyi/purple_tools/issues/25) of this project.
  For the kanban board project of this repo, visit [here](https://github.com/Oleksii-Kshenskyi/purple_tools/projects/1).
