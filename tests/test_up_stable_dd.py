import unittest
from handlers.run_main import run_main
from test.test_data_creator import TestDataCreator


def run_6():
    """
    Generates stable data for a normal scenario,
    tests the data-driven detector's ability to detect anomalies.

    :return:
    """
    detect_time = 1681711200000
    ts = TestDataCreator.create_stable_ts(end_time=detect_time, ts_length=5 * 1440, period=60000, down=500, up=600)
    ts[str(detect_time)] = 1000
    body = {"inputTimeSeries": ts, "intervalTime": 60000,
            "detectTime": detect_time,
            "algorithmConfig": {"algorithmType": "up", "sensitivity": "mid"},
            "ruleConfig": {"defaultDuration": 1,
                           "customChangeRate": 0.1}
            }
    result = run_main(body)
    return result


class TestFunction(unittest.TestCase):

    def test(self):
        self.assertEqual(run_6().get("isException"), True)
        pass


if __name__ == "__main__":
    pass
