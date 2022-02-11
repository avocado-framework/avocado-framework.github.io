---
layout: default
---

# Avocado's quick guide

## Running avocado from the command line

The fastest way of running `avocado` is from the command line to run a test. This test can be a binary or script:

```bash
$ avocado run examples/tests/sleeptest.py

JOB ID     : 5edc01147e75c0f120263ddf17915e130d8bb7e9
JOB LOG    : /home/user/avocado/job-results/job-2021-09-27T14.46-5edc011/job.log
 (1/1) examples/tests/sleeptest.py:SleepTest.test: STARTED
 (1/1) examples/tests/sleeptest.py:SleepTest.test: PASS (1.01 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 0 | SKIP 0 | WARN 0 | INTERRUPT 0 | CANCEL 0
JOB TIME   : 3.77 s
```

## Writing a Avocado Python test

To write basic Avocado tests in Python, the test class should inherit from the avocado.Test.  This kind of test is also known as an instrumented test in Avocado.

Following is a basic Avocado test written in Python. Copy and paste it to a file named `basic.py`

```python
from avocado import Test

class BasicTests(Test):

    def test_file_name_pass(self):
        expected_file_name = 'basic'
        file_name = __name__
        self.assertEqual(file_name, expected_file_name)
```

The file contains one single test. To run it execute:

```python
$ avocado run basic.py
JOB ID     : 927ee8f6973235d5137cb63695242cb025ee0e93
JOB LOG    : /home/user/avocado/job-results/job-2021-11-24T17.03-927ee8f/job.log
 (1/1) basic.py:BasicTests.test_file_name_pass: STARTED
 (1/1) basic.py:BasicTests.test_file_name_pass: PASS (0.01 s)
RESULTS    : PASS 1 | ERROR 0 | FAIL 0 | SKIP 0 | WARN 0 | INTERRUPT 0 | CANCEL 0
JOB TIME   : 1.32 s

```

### Naming conventions

Avocado interprets all methods starting with the `test` string in a class inheriting from `avocado.Test` as a test.

### Test statuses

| Status       | Description       |
|:-------------|:------------------|
| PASS         | The test ran without problems |
| WARN         | The test passed with a soft event that does not impact the test, but it is worth checking   |
| SKIP         | The test did not run |
| CANCEL       | The test was canceled during its execution |
| FAIL         | The test result is not the expected |
| ERROR        | Something went wrong with the test execution, not what is being tested itself |
| INTERRUPTED  | The test was interrupted while it was executing |

In an ordinary run, a test is expected to PASS or FAIL.

It is possible to force some error status calling the specific test method, like `self.fail`, `self.error`, and `self.cancel` from the test. To force a WARN status, write a warning to the test log using `self.log.warning`.

The following code extends the previous example of a basic Avocado test to demonstrate the test statuses.


```python
class BasicTests(Test):

    def test_file_name_pass(self):
        expected_file_name = 'basic'
        file_name = __name__
        self.assertEqual(file_name, expected_file_name)

    def test_file_name_fail(self):
        expected_file_name = 'not-basic'
        file_name = __name__
        self.assertEqual(file_name, expected_file_name)

    def test_file_name_cancel(self):
        expected_file_name = 'basic'
        file_name = __name__
        self.cancel('Canceling before asserting')
        self.assertEqual(file_name, expected_file_name)

    def test_file_name_error(self):
        expected_file_name = 'basic'
        file_name = __name__
        self.assertEqual(file_name, expected_file_name)
        raise RuntimeError('Erroring a test')

    def test_file_name_warn(self):
        expected_file_name = 'basic'
        file_name = __name__
        self.assertEqual(file_name, expected_file_name)
        self.log.warning('Warning note')
```

The output of the execution will look like this:

```bash

$ avocado run basic.py
JOB ID     : 6e7e82df1046f86ca940d7e3f8ea637fc47c728f
JOB LOG    : /home/user/avocado/job-results/job-2021-11-25T17.51-6e7e82d/job.log
 (2/5) basic.py:BasicTests.test_file_name_fail: STARTED
 (1/5) basic.py:BasicTests.test_file_name_pass: STARTED
 (4/5) basic.py:BasicTests.test_file_name_error: STARTED
 (3/5) basic.py:BasicTests.test_file_name_cancel: STARTED
 (5/5) basic.py:BasicTests.test_file_name_warn: STARTED
 (1/5) basic.py:BasicTests.test_file_name_pass: PASS (0.01 s)
 (5/5) basic.py:BasicTests.test_file_name_warn: WARN: Test passed but there were warnings during execution. Check the log for details. (0.01 s)
 (4/5) basic.py:BasicTests.test_file_name_error: ERROR: Erroring a test (0.04 s)
 (3/5) basic.py:BasicTests.test_file_name_cancel: CANCEL: Canceling before asserting (0.01 s)
 (2/5) basic.py:BasicTests.test_file_name_fail: FAIL: 'basic' != 'not-basic'\n- basic\n+ not-basic\n? ++++\n (0.04 s)
RESULTS    : PASS 1 | ERROR 1 | FAIL 1 | SKIP 0 | WARN 1 | INTERRUPT 0 | CANCEL 1
JOB TIME   : 2.00 s

```



## Writing an Avocado non-Python test

Coming soon!
