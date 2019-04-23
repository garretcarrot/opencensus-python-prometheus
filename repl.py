#!/usr/bin/env python

import sys

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

def main():
    while True:
        line = sys.stdin.readline()
        print(line.upper())

if __name__ == "__main__":
    main()
