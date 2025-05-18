import unittest
from securetrack import Monitor

class TestMonitor(unittest.TestCase):
    def test_initial_settings(self):
        monitor = Monitor()
        self.assertEqual(monitor.safe_radius_km, 1.0)
        self.assertEqual(monitor.voice_phrase, "Help!")

    def test_set_safe_zone(self):
        monitor = Monitor()
        monitor.set_safe_zone(radius_km=2.5)
        self.assertEqual(monitor.safe_radius_km, 2.5)

    def test_enable_voice_trigger(self):
        monitor = Monitor()
        monitor.enable_voice_trigger("Emergency")
        self.assertEqual(monitor.voice_phrase, "Emergency")

if __name__ == '__main__':
    unittest.main()
