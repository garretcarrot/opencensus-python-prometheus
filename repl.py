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
m_latency_ms = measure.MeasureFloat(
    "repl_latency", "The latency in millisecnds per REPL loop", "ms"
)
m_line_lengths = measure.MeasureInt(
    "repl_line_lengths", "The distributes of line lengths", "By"
)

# Get the stats object
stats = stats.stats

# Make the thing that records the measurements
stats_recorder = stats.stats_recorder

# Make some tag keys
method_key = tag_key.TagKey("method")
status_key = tag_key.TagKey("status")
error_key = tag_key.TagKey("error")

# Set up views

latency_view = view.View(
    "demo_latency",
    "The distro of latencies",
    [method_key, status_key, error_key],
    m_latency_ms,
    # Latency in buckets:
    # [>=0ms, >=25ms, >=50ms, >=75ms, >=100ms, >=200ms, >=400ms, >=600ms,
    #  >=800ms, >=1s, >=2s, >=4s, >=6s]
    aggregation.DistributionAggregation(
        [0, 25, 50, 75, 100, 200, 400, 600, 800, 1000, 2000, 4000, 6000]
    ),
)

line_count_view = view.View(
    "demo_lines_in",
    "The number of lines from stdin",
    [method_key, status_key, error_key],
    m_line_lengths,
    aggregation.CountAggregation(),
)

line_length_view = view.View(
    "demo_line_lengths",
    "Groups lengths of keys in buckets",
    [method_key, status_key, error_key],
    m_line_lengths,
    # Lengths:
    # [>=0B, >=5B, >=10B, >=15B, >=20B, >=40B, >=60B, >=80B, >=100B, >=200B,
    #  >=400B, >=600B, >=800B, >=1MB]
    aggregation.DistributionAggregation(
        [0, 5, 10, 15, 20, 40, 60, 80, 100, 200, 400, 600, 800, 1000]
    ),
)


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
