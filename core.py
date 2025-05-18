import time
import logging

class RiskAnalyzer:
    def __init__(self, location, profile):
        self.location = location
        self.profile = profile

    def analyze_risk(self):
        if self.profile == 'night' and self.location in ['unknown area', 'high-crime zone']:
            return 'High Risk'
        return 'Low Risk'

class EmergencyAlertSystem:
    def __init__(self, wake_words):
        self.wake_words = set(wake_words)
        self.triggered = False

    def detect_phrase(self, phrase):
        if phrase.lower() in self.wake_words:
            self.trigger_alert()
            return True
        return False

    def trigger_alert(self):
        self.triggered = True
        print("Emergency Alert Triggered!")
        logging.warning("Emergency alert triggered at %s", time.ctime())

    def cancel_alert(self, cancel_phrase, detected_phrase):
        if cancel_phrase.lower() == detected_phrase.lower():
            self.triggered = False
            print("Emergency Alert Canceled")
            return True
        return False
