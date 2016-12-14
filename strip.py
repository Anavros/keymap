
import util


def minify(path):
    """
    Remove whitespace from a data file. Outputs to stdout to be redirected.
    """
    with util.read_file_or_stdin(path) as f:
        while True:
            c = f.read(1)
            if not c: break  # EOF
            if c.isspace(): continue  # remove whitespace
            print(c, end='')
