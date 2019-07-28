# ----------------------------------------------------------------------------------------
# Log class
# ----------------------------------------------------------------------------------------


class Log:
    """Sort unique log messages in categories,
    and then retrieve them or store them in a file,
    as a easily legible string."""

    def __init__(self, filename):
        self.log = {}
        self.filename = filename

    def post(self, category, *items):
        """Insert on or more messages in the specified category."""
        # Each item in the log is
        # stored under a category
        if category not in self.log:
            # The category is a set, so the
            # items are unique, there are
            # no duplicate items
            self.log[category] = set()
        for item in items:
            self.log[category].add(item)

    def __str__(self):
        s = ""
        for cat in sorted(self.log):
            s += '-------------------------------------------------------------\n'
            s += ' ' + cat + '\n'
            s += '-------------------------------------------------------------\n'
            for item in sorted(self.log[cat]):
                s += item + '\n'
            s += '\n'
        return s

    def write(self):
        open(self.filename, 'w').write(str(self))

