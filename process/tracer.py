import sys
import trace


def trace_code(path, code=None):
    # create a Trace object, telling it what to ignore, and whether to
    # do tracing or line-counting or both.
    tr = trace.Trace(
        ignoredirs=[sys.prefix, sys.exec_prefix],
        trace=0,
        count=1,
        outfile='.results',
        timing=True)

    # Subtitution of path

    # run the new command using the given tracer
    tr.run(code)

    # make a report, placing output in the current directory
    r = tr.results()
    trace.CoverageResults
    r.write_results(show_missing=True, coverdir="tracer")

    return r
