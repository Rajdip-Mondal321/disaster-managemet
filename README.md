# 🛡️ Disaster Management System

An emergency preparedness, real-time hazard monitoring, and disaster response web platform built with **Python**, **Flask**, and modern responsive **Vanilla CSS/JS**.

The platform equips citizens and emergency responders with verified safety protocols for critical disasters (Floods, Earthquakes, Cyclones, Fires), live localized meteorological hazard detection, interactive mapping, and one-click access to official 24/7 national emergency helplines.

---

## 📌 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Setup](#installation--setup)
  - [Running the Development Server](#running-the-development-server)
  - [Running with Gunicorn (Production)](#running-with-gunicorn-production)
- [API Documentation](#-api-documentation)
- [Supported Disasters & Protocols](#-supported-disasters--protocols)
- [Emergency Helplines Directory](#-emergency-helplines-directory)
- [Configuration & Environment Variables](#-configuration--environment-variables)
- [Deployment](#-deployment)
- [Privacy & Data Safety](#-privacy--data-safety)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### 📋 Verified Disaster Safety Protocols
- **Phase-by-Phase Guidance**: Structured protocols segmented into **Before**, **During**, **What NOT to do**, **After**, and **When to call for help**.
- **Four Critical Disaster Modules**:
  - 🌊 **Flood**: Evacuation routes, drinking water purification, electrical isolation, vertical refuge guidelines.
  - 🏚️ **Earthquake**: Drop-Cover-Hold rules, safe interior zones, post-tremor inspection, and structural hazard avoidance.
  - 🌀 **Cyclone**: High-wind preparation, sheltering protocols, eye-of-storm cautions, and surge safety.
  - 🔥 **Fire**: Smoke crawl techniques, PASS extinguisher methods, touch-door safety, and escape accountability.
- **Dynamic Filtering**: Interactive quick-switch tabs and dropdown selectors powered by asynchronous client-side API requests.

### 🌤️ Live Weather Hazard Monitor & Geolocation
- **Client-Side Geolocation**: Instant one-click coordinate detection using the browser's HTML5 Geolocation API.
- **City Search & Geocoding**: Search weather conditions for any city or district globally using the Open-Meteo Geocoding API.
- **Real-Time Meteorological Metrics**: Live temperature readings, weather conditions (clear, overcast, thunderstorms, drizzle, rain), and wind speed measurements.
- **Automated Wind Hazard Evaluation**: Dynamic safety warning triggers when sustained wind speeds exceed **40 km/h** (Gale Force Advisory).
- **Embedded Interactive Map**: Google Maps view auto-centered on detected or queried coordinates.

### 🚨 24/7 National Emergency Helplines
- **Emergency Quick-Dial Bar**: Always-accessible top banner for rapid access to core toll-free numbers.
- **One-Click Dialing**: Direct `tel:` links formatted for mobile devices and VoIP callers.
- **Incident-Specific Contacts**: Tailored helpline recommendations displayed dynamically for each disaster type (NDRF, Ambulance, Fire, Police, National Emergency).

### 📄 Legal & Compliance Ready
- Dedicated **Privacy Policy** and **Terms & Conditions** pages detailing strict client-side-only coordinate handling and zero-retention policies.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend** | Python 3.9+ / Flask 3.0+ | Lightweight WSGI web application framework & REST API |
| **Production Server** | Gunicorn 21.2+ | UNIX WSGI HTTP Server for production deployment |
| **Frontend** | HTML5, Vanilla JavaScript | Semantic markup and asynchronous DOM manipulation |
| **Styling** | Vanilla CSS (CSS3) | Custom responsive design system, dark/light accents, zero external CSS dependencies |
| **Weather & Geocoding** | Open-Meteo APIs | Free, high-accuracy, privacy-friendly weather and geocoding services (no API key required) |
| **Maps** | Google Maps Embed | Embedded geographic coordinate visualization |

---

## 📂 Project Structure

```text
Disaster-Management/
├── app.py                  # Main Flask application, routing, disaster data & API endpoints
├── requirements.txt        # Python package dependencies (Flask, Gunicorn)
├── README.md               # Project documentation
├── static/
│   ├── favicon.svg         # SVG vector favicon with disaster shield icon
│   └── style.css           # Comprehensive design system, layout & component styles
└── templates/
    ├── index.html          # Main dashboard (Safety guide, weather monitor, emergency directory)
    ├── privacy.html        # Privacy policy page
    └── terms.html          # Terms and conditions page
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.9** or higher installed on your system.
- **pip** package installer.
- **Git** (optional, for cloning).

### Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Rajdip-Mondal321/disaster-managemet.git
   cd Disaster-Management
   ```

2. **Create a virtual environment** (recommended):
   - On Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Development Server

Start the local Flask development server:

```bash
python app.py
```

The application will be accessible at:
👉 **`http://localhost:5000`**

### Running with Gunicorn (Production)

For production Linux/macOS environments:

```bash
gunicorn --bind 0.0.0.0:5000 --workers 4 app:app
```

---

## 📡 API Documentation

The backend provides public JSON endpoints for integration with external dashboards, emergency alerts, or mobile apps.

### 1. Retrieve Safety Tips & Helplines
Returns verified safety protocols, actionable phases, and emergency helplines for a specified disaster.

- **URL**: `/tips` (Alias: `/get_tips`)
- **Method**: `GET`
- **Query Parameters**:
  - `type` (or `disaster`): `flood` | `earthquake` | `cyclone` | `fire`

#### Example Request:
```http
GET /tips?type=flood HTTP/1.1
Host: localhost:5000
```

#### Example Response:
```json
{
  "success": true,
  "data": {
    "title": "Flood Safety and Evacuation Protocol",
    "tips": [
      "Before (Evacuation Route): Map out the highest elevation points in your neighbourhood...",
      "During (Power and Gas Safety): If water begins to enter your home, switch off the main electrical breaker...",
      "What NOT to do: Never walk, swim, or drive through moving floodwater...",
      "After (Inspecting Structures): Return home only after local authorities issue an official all-clear announcement...",
      "When to call for help: Call 112 (National Emergency) or 1078 (Disaster Management Authority)..."
    ],
    "helplines": [
      {
        "service": "National Emergency",
        "number": "112",
        "purpose": "Immediate life threats and multi-agency rescue dispatch"
      },
      {
        "service": "Disaster Management (NDRF)",
        "number": "1078",
        "purpose": "Flood evacuation, boat rescue teams, and relief coordination"
      }
    ]
  }
}
```

### 2. Health Check Endpoint
Validates that the service is running and operational.

- **URL**: `/health`
- **Method**: `GET`

#### Example Response:
```json
{
  "status": "running",
  "project": "Disaster Management System"
}
```

---

## 🌪️ Supported Disasters & Protocols

| Disaster Type | Primary Hazards Addressed | Emergency Focus |
| :--- | :--- | :--- |
| **Flood** | River overflows, flash floods, urban waterlogging, contaminated water | Evacuation elevations, electrical shutoff, water purification, raft/boat rescue |
| **Earthquake** | Ground tremors, structural collapse, aftershocks, fallen debris | Drop-Cover-Hold, non-elevator evacuation, structural inspections |
| **Cyclone** | Gale-force winds, storm surges, flying debris, fallen transmission lines | Indoor sheltering, eye-of-storm vigilance, water reserves, post-storm power hazards |
| **Fire** | Structural fires, toxic smoke inhalation, electrical fires | Smoke crawl, PASS extinguisher technique, rapid outdoor assembly |

---

## ☎️ Emergency Helplines Directory

Official 24/7 public emergency numbers across India:

| Service | Number | Scope & Response Unit |
| :--- | :---: | :--- |
| **National Emergency Service** | **112** | Unified nationwide single-number emergency dispatch (Police, Fire, Medical) |
| **Disaster Management (NDRF)** | **1078** | National Disaster Response Force for floods, cyclones, and collapsed structures |
| **Emergency Medical Ambulance** | **108** | Emergency patient care, trauma dispatch, waterborne and burn trauma |
| **Fire & Rescue Service** | **101** | Structural fire suppression, hazardous material clearance, extrications |
| **Police Control Room** | **100** | Perimeter security, disaster cordoning, public safety, search and rescue coordination |

---

## ⚙️ Configuration & Environment Variables

The application can be configured via environment variables:

| Variable | Type | Default | Description |
| :--- | :---: | :---: | :--- |
| `PORT` | Integer | `5000` | Port on which the application listens |
| `FLASK_DEBUG` | Boolean (`true`/`false`) | `false` | Enables Flask debug mode and live reloading for development |

Example in PowerShell:
```powershell
$env:PORT="8080"
$env:FLASK_DEBUG="true"
python app.py
```

Example in Bash:
```bash
export PORT=8080
export FLASK_DEBUG=true
python app.py
```

---

## 🚢 Deployment

### Render / Railway / Heroku

1. Create a `Procfile` (if required by your platform):
   ```text
   web: gunicorn app:app
   ```
2. Set the build command to:
   ```bash
   pip install -r requirements.txt
   ```
3. Set the start command to:
   ```bash
   gunicorn --bind 0.0.0.0:$PORT app:app
   ```

### Docker (Optional)

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "app:app"]
```

---

## 🔒 Privacy & Data Safety

- **Zero Coordinate Storage**: Device location coordinates retrieved via browser geolocation or city searches are handled **strictly client-side**. No location data is logged to server databases or shared with third parties.
- **Free & Open APIs**: Weather data and geocoding rely on Open-Meteo, which does not require API keys or tracking user identity.

---

## 🤝 Contributing

Contributions to enhance disaster safety protocols, add multi-lingual support, or integrate additional emergency contacts are welcome!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/SafetyImprovement`)
3. Commit your Changes (`git commit -m 'Add localized safety protocol'`)
4. Push to the Branch (`git push origin feature/SafetyImprovement`)
5. Open a Pull Request

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
