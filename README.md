# Rocks

This project have continuous integration testing for automating code coverage in realtime for Python on SublimeText. This plugin simplify development process and check more quickly the problems. 

This project is inspired in [NCrunch](http://www.ncrunch.net) plugin for VS Studio. Not finded similar projects for python.

UI: 

![Example][logo]

[logo]: ./assets/example.png "Example of plugin"

Use Rocks.tmTheme to view color in icons. If you use a another theme, please add this lines in tmTheme file used.

```
... 
    <string>Sunburst</string>
    <key>settings</key>
    <array>
... 
<!-- Adding into <array> level -->

<dict>
    <key>name</key>
    <string>markup.tracked.rocks</string>
    <key>scope</key>
    <string>markup.tracked.rocks</string>
    <key>settings</key>
    <dict>
        <key>foreground</key>
        <string>#41a017</string>
    </dict>
</dict>
<dict>
    <key>name</key>
    <string>markup.untracked.rocks</string>
    <key>scope</key>
    <string>markup.untracked.rocks</string>
    <key>settings</key>
    <dict>
        <key>foreground</key>
        <string>#AAAAAA</string>
    </dict>
</dict>
<dict>
    <key>name</key>
    <string>markup.skipped.rocks</string>
    <key>scope</key>
    <string>markup.skipped.rocks</string>
    <key>settings</key>
    <dict>
        <key>foreground</key>
        <string>#FFF380</string>
    </dict>
</dict>
<dict>
    <key>name</key>
    <string>markup.error.rocks</string>
    <key>scope</key>
    <string>markup.error.rocks</string>
    <key>settings</key>
    <dict>
        <key>foreground</key>
        <string>#FF0000</string>
    </dict>
</dict>

... 
</array>

``` 

## Features proposed  

### Release 1 - Done

- Auto detect code coverage 
- Better UI to detect coverage inconsistences 

### Release 2 

- Detect impact of code and importance of system
- Metrics for development 
- Simple navigation in issues detected 

### Release 3 

- Integration of linty system 
- Suggestions refactories 

### Future relases 

- Distributing testing 
- Integration of test systems (tox, nunit, etc)


## Limitations

- Coverage tests not work in Django projects.

## Examples 

File `class_a.py`

```python
import time


class A(object):

    def __init__(self):
        self.value = "Some Value"

    def return_true(self):
        return True

    def raise_exc(self, val):

        if val == "TDD":
            return True

        raise ValueError(val)

    def repeat(self):
        return 1

    def sleeping_half_second(self):
        time.sleep(0.5)  # Warning running, show extra info warning

    def sleeping(self):
        time.sleep(1)  # Long running, show extra info slow

    def sleeping_more_one_seconds(self):
        # Long running greater than 1 seconds, show extra info slower
        time.sleep(1.1)

```

File `test_coverage.py`

```python
import unittest
from class_a import A


class TestSimple(unittest.TestCase):
    """Simple test coverage"""

    def test_pass(self):
        assert True

    # def test_fail(self):
    #     assert False

    # def test_fail_2(self):
    #     assert 2 == 1

    def test_init(self):
        a = A()

        assert a.return_true()
 
    def test_sleeping_half_second(self):
        a = A()
        a.sleeping_half_second()

        assert True

    def test_sleeping(self):
        a = A()
        a.sleeping()

        assert True

    def test_sleeping_more_one_seconds(self):
        a = A()
        a.sleeping_more_one_seconds()

        assert True

    def test_exception(self):
        a = A()

        assert a.raise_exc("DDD")

        return

        # Check code not reached in coverage
        d = 1 + 2 + 3
```


