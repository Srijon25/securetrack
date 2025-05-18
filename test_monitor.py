import unittest
from securetrack import RiskAnalyzer, EmergencyAlertSystem

class TestSecureTrack(unittest.TestCase):
    def test_risk_analysis_high(self):
        analyzer = RiskAnalyzer(location="unknown", profile="night")
        self.assertEqual(analyzer.analyze_risk(), "High Risk")

    def test_risk_analysis_low(self):
        analyzer = RiskAnalyzer(location="home", profile="day")
        self.assertEqual(analyzer.analyze_risk(), "Low Risk")

    def test_risk_analysis_medium(self):
        analyzer = RiskAnalyzer(location="work", profile="day")
        self.assertEqual(analyzer.analyze_risk(), "Medium Risk")

    def test_alert_trigger(self):
        system = EmergencyAlertSystem(wake_words=["help", "emergency"])
        self.assertTrue(system.detect_phrase("emergency"))

    def test_alert_not_triggered(self):
        system = EmergencyAlertSystem(wake_words=["help", "emergency"])
        self.assertFalse(system.detect_phrase("hello"))

    def test_alert_cancel_success(self):
        system = EmergencyAlertSystem(wake_words=["help"])
        system.detect_phrase("help")
        self.assertTrue(system.cancel_alert("help", "help"))

    def test_alert_cancel_failure(self):
        system = EmergencyAlertSystem(wake_words=["help"])
        system.detect_phrase("help")
        self.assertFalse(system.cancel_alert("help", "nope"))

    def test_no_alert_to_cancel(self):
        system = EmergencyAlertSystem(wake_words=["help"])
        self.assertFalse(system.cancel_alert("help", "help"))
