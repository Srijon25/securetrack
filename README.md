# SecureTrack

**SecureTrack** is an AI-powered personal safety system designed to detect and respond to environmental and contextual risks in real-time. It analyzes user location, behavior, and profile data to assess safety levels and activate emergency alerts using customizable wake-word detection. This tool is designed for researchers, developers, and security-focused applications.

## Features

- **AI-Based Risk Analysis**  
  Detects risk levels based on user-defined profiles (e.g., travel, work, night) and current environment.

- **Wake-Word Emergency Detection**  
  Triggers SOS alerts using spoken wake phrases like "Help", "Emergency", or custom-defined keywords.

- **Profile-Specific Safety Settings**  
  Allows the creation of multiple safety profiles with different emergency timeouts, phrases, and zones.

- **Emergency Alert System**  
  Sends alerts, enables voice-activated cancellation, and includes pre-warning phases and safety validation.

- **Modular and Extendable**  
  Designed to support future integration with GPS, map UIs, crime data APIs, and mobile platforms.

## Installation

Clone the repository and install the package:

```bash
git clone https://github.com/Srijon25/securetrack.git
cd securetrack
pip install .

Or manually install dependencies (if needed):

pip install -r requirements.txt

Usage Example

from securetrack import RiskAnalyzer, EmergencyAlertSystem

# Analyze risk based on profile and location
analyzer = RiskAnalyzer(location="urban", profile="night")
print(analyzer.analyze_risk())  # Outputs: High / Medium / Low

# Trigger an alert using a wake word
alert = EmergencyAlertSystem(wake_words=["help", "emergency"])
alert.detect_phrase("help")  # Activates alert
alert.cancel_alert("help", "help")  # Cancels alert using cancel phrase

Running Tests

All core components are covered with unit tests.

To run:

python -m unittest discover tests

Project Structure

securetrack/
├── securetrack/
│   ├── __init__.py
│   └── core.py
├── tests/
│   └── test_monitor.py
├── README.md
├── SECURITY.md
├── setup.py
└── LICENSE

Security Policy

See SECURITY.md for reporting vulnerabilities and threat disclosures.

Citation

If you use this software in your research, please cite:

Shill, S.K. (2025). SecureTrack: AI-Enhanced Real-Time Risk Analysis and Emergency Alert System. Journal of Open Source Software.

License

MIT License. See the LICENSE file for details.

Author

Srijon Kumar Shill
Independent Researcher
ORCID: 0009-0004-8924-2272
Email: theunpredictable157@gmail.com
GitHub: Srijon25

