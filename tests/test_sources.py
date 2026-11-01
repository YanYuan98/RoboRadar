import os
import time
import unittest

from roboradar.sources import _iso


class RssTimestampTests(unittest.TestCase):
    def test_missing_timestamp(self):
        self.assertEqual(_iso(None), "")

    @unittest.skipUnless(hasattr(time, "tzset"), "requires time.tzset")
    def test_rss_timestamp_is_not_shifted_by_local_timezone(self):
        previous_tz = os.environ.get("TZ")
        try:
            os.environ["TZ"] = "Asia/Shanghai"
            time.tzset()
            self.assertEqual(
                _iso(time.gmtime(0)),
                "1970-01-01T00:00:00+00:00",
            )
        finally:
            if previous_tz is None:
                os.environ.pop("TZ", None)
            else:
                os.environ["TZ"] = previous_tz
            time.tzset()


if __name__ == "__main__":
    unittest.main()
