import unittest
from handlers.run_main import run_main
from test.test_data_creator import TestDataCreator


def run_9():
    """
    Generates data for a cold-start scenario,
    tests the rule filter's ability to filter noise.

    :return:
    """
    detect_time = 1681711200000
    ts = TestDataCreator.create_stable_ts(detect_time, 1 * 1440, 60000, 500, 600)
    ts[str(detect_time)] = 1000
    body = {"inputTimeSeries": ts, "intervalTime": 60000,
            "detectTime": detect_time,
            "algorithmConfig": {"algorithmType": "up", "sensitivity": "mid"},
            "ruleConfig": {"defaultDuration": 1,
                           # "customUpThreshold": 0,
                           "customDownThreshold": 1001,  # rule filer
                           "customChangeRate": 0.1}}
    result = run_main(body)
    # TestDataCreator.plot(ts, detect_time, 60000)
    return result


class TestFunction(unittest.TestCase):

    def test(self):
        self.assertEqual(run_9().get("isException"), False)
        pass


if __name__ == "__main__":
    pass
