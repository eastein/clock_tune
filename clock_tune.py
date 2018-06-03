#!/usr/bin/env python3

"""
This program, given 3 or 4 timestamps
"""

import optparse
import datetime
import iso8601
import sys

def seconds_difference_float(begin, end):
    td = end - begin
    # Don't use this tool around leap seconds or DST because it won't work right.. but neither will your mechanical clock that even
    # needs this software, natch.
    return td.days * 86400.0 + td.seconds * 1.0


if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option('--real-start', dest='real_start', help="Mandatory. Actual start time of the measured period.")
    parser.add_option('--real-end', dest='real_end', help="Mandatory. Actual end time of the measured period.")
    parser.add_option('--clock-start', dest='clock_start', default=None, help="Mandatory. Clock reading at start time of the measured period.")
    parser.add_option('--clock-end', dest='clock_end', help="Mandatory. Clock reading at end time of the measured period.")
    (options, args) = parser.parse_args()

    if options.real_start is None or options.real_end is None or options.clock_end is None:
        print("Error: Mandatory option not specified.")
        parser.print_help()
        sys.exit(1)


    real_start = iso8601.parse_date(options.real_start)
    real_end = iso8601.parse_date(options.real_end)
    if options.clock_start is not None:
        clock_start = iso8601.parse_date(options.clock_start)
    else:
        clock_start = real_start
    clock_end = iso8601.parse_date(options.clock_end)

    print('Actual times:')
    print('\t', real_start, real_end)
    print('Clock times:')
    print('\t', clock_start, clock_end)

    real_elapsed = seconds_difference_float(real_start, real_end)
    clock_elapsed = seconds_difference_float(clock_start, clock_end)

    error = clock_elapsed - real_elapsed
    error_ratio = (error / real_elapsed)

    print('Elapsed during period:')
    print('* Real seconds: {real_elapsed:0.3f}'.format(real_elapsed=real_elapsed))
    print('* Clock seconds: {clock_elapsed:0.3f}'.format(clock_elapsed=clock_elapsed))

    print('Calibration results:')
    print('* Error seconds: {error:n}'.format(error=error))
    print('* Error ratio: {error_ratio:0.4f}'.format(error_ratio=error_ratio))