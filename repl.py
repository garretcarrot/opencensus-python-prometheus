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

# Make some tag keys
method_key = tag_key.TagKey("method")
status_key = tag_key.TagKey("status")
error_key = tag_key.TagKey("error")

def main():
    while True:
        readEvalPrint()

def readEvalPrint():
    line = sys.stdin.readline()
    start = time.time()
    print(line.upper())

    # Make a thing to store measurements
    measurements = stats_recorder.new_measurement_map()

    # Record the duration
    end_ms = (time.time() - start) * 1000.0
    measurements.measure_float_put(m_latency_ms, end_ms)

    # Record the line length
    measurements.measure_int_put(m_line_lengths, len(line))

    # Get a thing to store tag values
    tags = tag_map.TagMap()
    tags.insert(method_key, tag_value.TagValue("repl"))
    tags.insert(status_key, tag_value.TagValue("OK"))

    # Record the tag values
    measurements.record(tags)

if __name__ == "__main__":
    main()
