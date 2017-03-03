import sys
import trace


# create a Trace object, telling it what to ignore, and whether to
# do tracing or line-counting or both.
tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=1,
    outfile='.results',
    timing=True)

# run the new command using the given tracer
tracer.run("""
import class_a
a = class_a.A()
for x in range(10):
    a.repeat()

a.sleeping()
a.sleeping_half_second()
a.sleeping_more_one_seconds()
""")

# make a report, placing output in the current directory
r = tracer.results()
r.write_results(show_missing=True, coverdir="tracer")
