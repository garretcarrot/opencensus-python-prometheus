#!/usr/bin/env python

import sys
import time

from opencensus.stats import aggregation
from opencensus.stats import measure
from opencensus.stats import stats
from opencensus.stats import view
from opencensus.tags import tag_key
from opencensus.tags import tag_map
from opencensus.tags import tag_value

# Make the measures
m_latency_ms = measure.MeasureFloat("repl_latency", "The latency in millisecnds per REPL loop", "ms")
m_line_lengths = measure.MeasureInt("repl_line_lengths", "The distributes of line lengths", "By")

# Make the thing that records the measurements
stats_recorder = stats.Stats().stats_recorder

def main():
    while True:
        readEvalPrint()

def readEvalPrint():
    line = sys.stdin.readline()
    start = time.time()
    print(line.upper())

    # Make a thing to store measurements
    measure_map = stats_recorder.new_measurement_map()

    # Record the duration
    end_ms = (time.time() - start) * 1000.0
    measure_map.measure_float_put(m_latency_ms, end_ms)

    # Record the line length
    measure_map.measure_int_put(m_line_lengths, len(line))

if __name__ == "__main__":
    main()
