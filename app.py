import os
from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__)

DISASTER_DATA = {
    "flood": {
        "title": "Flood Safety and Evacuation Protocol",
        "tips": [
            "Before (Evacuation Route): Map out the highest elevation points in your neighbourhood and identify two overland routes away from river basins and low drainage lines. Clear local drain grates around your property to prevent localized street pooling.",
            "Before (Emergency Supplies): Pack an emergency grab bag in a waterproof container. Keep at least 3 liters of potable water per person per day for 3 days, non-perishable food, water purification tablets, a battery-powered radio, a torch, spare batteries, and prescription medications in sealed plastic pouches.",
            "Before (Protecting Assets): Raise electrical appliances, fuse boxes, gas cylinders, and valuables above projected flood lines. Anchor outdoor fuel tanks to prevent them from floating, leaking, or blocking culverts.",
            "During (Power and Gas Safety): If water begins to enter your home, switch off the main electrical breaker and main gas valve immediately before water reaches the panels. If water has already reached the switches, do not touch them; evacuate immediately.",
            "During (Vertical Refuge): If trapped inside a building by rapidly rising water, move to the top floor or roof. Bring your emergency kit, warm clothing, and a whistle or torch to signal rescuers.",
            "What NOT to do: Never enter an enclosed attic space unless it has an accessible roof escape hatch. Rising water can trap you beneath the ceiling with no escape route.",
            "What NOT to do: Never walk, swim, or drive through moving floodwater. Moving water only 15 cm deep can sweep an adult off balance, and 30 cm can float and carry away most passenger motor vehicles.",
            "After (Inspecting Structures): Return home only after local authorities issue an official all-clear announcement. Inspect exterior foundations and load-bearing walls for cracking or settling before entering. Discard all food, beverages, and medicines that came into contact with floodwater.",
            "When to call for help: Call 112 (National Emergency) or 1078 (Disaster Management Authority) immediately if people are stranded, isolated, or trapped by water. For urgent trauma, drowning rescue, or medical emergencies, dial 108 for an ambulance. Report downed power lines and gas leaks to emergency services at once."
        ],
        "helplines": [
            {"service": "National Emergency", "number": "112", "purpose": "Immediate life threats and multi-agency rescue dispatch"},
            {"service": "Disaster Management (NDRF)", "number": "1078", "purpose": "Flood evacuation, boat rescue teams, and relief coordination"},
            {"service": "Ambulance", "number": "108", "purpose": "Drowning, waterborne trauma, hypothermia, medical emergencies"},
            {"service": "Police", "number": "100", "purpose": "Hazard cordoning, perimeter security, and missing person reports"}
        ]
    },
    "earthquake": {
        "title": "Earthquake Safety and Survival Protocol",
        "tips": [
            "Before (Securing Heavy Items): Fasten tall bookcases, cabinets, water heaters, and heavy appliances firmly to wall studs with metal brackets. Store heavy glassware, pots, and breakable items on bottom shelves, and latch cabinet doors.",
            "Before (Identifying Safe Zones): Locate safe cover spots in every room: underneath sturdy desks, heavy work tables, or against interior load-bearing walls away from exterior windows, glass partitions, and hanging lights.",
            "During (Drop, Cover, and Hold): Drop to your hands and knees immediately to prevent being knocked down. Take cover beneath a sturdy table or desk. Hold on firmly with one hand while shielding your head and neck with your other arm until all shaking stops.",
            "During (Outdoors): If outdoors when tremors begin, move into an open area away from buildings, streetlights, overhead power cables, brick boundary walls, and chimneys. Drop to the ground and shield your head.",
            "What NOT to do: Do not run outside or attempt to use stairwells during active shaking. Most earthquake casualties occur when falling glass, facade tiles, and parapet bricks strike individuals attempting to flee buildings.",
            "What NOT to do: Never use elevators during or immediately after an earthquake. Do not light matches, candles, or operate electrical light switches until you have verified there are no ruptured gas pipes.",
            "After (Expect Aftershocks): Put on sturdy thick-soled shoes and leather work gloves before walking past debris. Check gas valves and water lines for damage. If you detect a gas odor, open doors and windows, turn off the cylinder valve, and evacuate the building.",
            "When to call for help: Dial 112 (National Emergency) or 100 (Police) if people are trapped beneath rubble, collapsed walls, or damaged structures. Call 108 (Ambulance) for serious trauma, crush injuries, or severe bleeding. Contact 1078 (Disaster Management) for structural collapse assessments and coordinated rescue response."
        ],
        "helplines": [
            {"service": "National Emergency", "number": "112", "purpose": "Immediate life safety and debris rescue dispatch"},
            {"service": "Disaster Management (NDRF)", "number": "1078", "purpose": "Urban search and rescue, structural collapse response"},
            {"service": "Ambulance", "number": "108", "purpose": "Trauma, crush syndrome, emergency medical transport"},
            {"service": "Police", "number": "100", "purpose": "Area cordoning, public safety, law enforcement"}
        ]
    },
    "cyclone": {
        "title": "Cyclone and High Wind Safety Protocol",
        "tips": [
            "Before (Securing Structures): Inspect roof sheets, tiles, doors, and window latches. Fasten loose roofing with screws or tie-downs. Trim overhanging tree branches close to power lines and structures. Remove or store indoors loose outdoor furniture, signs, and metal sheets that could become high-speed projectiles.",
            "Before (Water and Power Reserve): Store at least 15 liters of potable drinking water per person in clean, sealed containers. Fully charge mobile devices, power banks, and battery-powered radios to receive official meteorological bulletins.",
            "During (Secure Sheltering): Remain indoors inside the strongest central room of the building, away from exterior walls and glass windows. Close all interior doors and secure window shutters. Unplug sensitive electronics to avoid damage from power surges.",
            "What NOT to do: Do not leave your shelter during the eye of the storm when winds abruptly die down. The calm is temporary; violent hurricane-force winds will resume from the opposite direction within minutes, often with even greater destructive force.",
            "What NOT to do: Do not visit beaches, coastal promenades, riverbanks, or storm-surge barriers to watch waves. Never touch or approach fallen electrical lines, sagging utility cables, or metallic fences touching water.",
            "After (Post-Storm Caution): Stay sheltered until disaster management officials issue a formal all-clear announcement. Watch out for snakes, scorpions, and other wildlife displaced by water. Inspect your home for gas leaks and structural damage before turning services back on.",
            "After (Water Safety): Boil municipal or well water vigorously for at least 1 minute before drinking or cooking. Avoid consuming perishable refrigerated foods if electrical power has been interrupted for more than 4 hours.",
            "When to call for help: Call 112 (National Emergency) or 1078 (Disaster Management) if wind damage compromises your roof, if water breaches your building, or if trees fall across exit passages. Dial 108 for emergency medical response and evacuation of injured persons. Dial 101 if fallen power lines spark fires."
        ],
        "helplines": [
            {"service": "National Emergency", "number": "112", "purpose": "Critical multi-agency emergency response"},
            {"service": "Disaster Management (NDRF)", "number": "1078", "purpose": "Cyclone relief, storm surge rescue, shelter coordination"},
            {"service": "Ambulance", "number": "108", "purpose": "Medical triage and emergency patient transport"},
            {"service": "Fire Service", "number": "101", "purpose": "Electrical sparking, transformer fires, fallen tree clearance"}
        ]
    },
    "fire": {
        "title": "Structure Fire and Smoke Safety Protocol",
        "tips": [
            "Before (Detection and Suppression): Install working smoke alarms on every level of your building and test them monthly. Keep an operational ABC-rated dry powder fire extinguisher near the kitchen and exit passages, and know how to operate it using the PASS method (Pull, Aim, Squeeze, Sweep).",
            "Before (Evacuation Route): Map out two clear escape paths from every room. Keep all exit corridors, hallways, and stairwells clear of storage, furniture, and bicycles at all times.",
            "During (Crawl Low Under Smoke): If smoke or flames are detected, alert everyone in the building and evacuate immediately. Crawl on your hands and knees where the air is coolest and cleanest; toxic gases and hot smoke rise toward the ceiling.",
            "During (Feel Doors Before Opening): Test door panels and metal door handles with the back of your hand before opening. If the door feels warm or hot, do not open it; use your alternate exit route. If cool, open cautiously with your shoulder braced against the door.",
            "What NOT to do: Never use elevators during a fire. Elevators can lose power between floors or open directly onto fire floors; always use the fire escape stairs. Never return inside a burning structure to retrieve documents, money, or pets.",
            "What NOT to do: If your clothes catch fire, do not run; running fans the flames. Stop immediately, drop to the ground, cover your face with your hands, and roll back and forth until the fire is smothered.",
            "After (Assembly and Accountability): Once you exit the building, stay out at your pre-designated assembly location. Never re-enter a smoke-filled or burned structure until fire officials declare it safe. Report missing occupants to arriving fire commanders immediately.",
            "When to call for help: Call 101 (Fire Service) or 112 (National Emergency) the moment you are safely outside the building; never delay escape to place a phone call from inside an active fire. Dial 108 (Ambulance) immediately if anyone has sustained burns, smoke inhalation, or trauma."
        ],
        "helplines": [
            {"service": "Fire Service", "number": "101", "purpose": "Immediate fire suppression, structural rescue, and ventilation"},
            {"service": "National Emergency", "number": "112", "purpose": "Centralized life-safety and emergency dispatch"},
            {"service": "Ambulance", "number": "108", "purpose": "Burn care, smoke inhalation treatment, medical transport"},
            {"service": "Police", "number": "100", "purpose": "Traffic clearing for fire engines and perimeter security"}
        ]
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tips")
@app.route("/get_tips")
def tips():
    disaster = (request.args.get("type") or request.args.get("disaster") or "").strip().lower()
    if disaster in DISASTER_DATA:
        return jsonify({
            "success": True,
            "data": DISASTER_DATA[disaster]
        })
    return jsonify({
        "success": False,
        "error": "Disaster type not recognized. Valid options: flood, earthquake, cyclone, fire."
    }), 404

@app.route("/privacy")
@app.route("/privacy-policy")
def privacy():
    return render_template("privacy.html")

@app.route("/terms")
@app.route("/terms-and-conditions")
def terms():
    return render_template("terms.html")

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"), "favicon.svg", mimetype="image/svg+xml")

@app.route("/health")
def health():
    return jsonify({
        "status": "running",
        "project": "Disaster Management System"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() in ("true", "1")
    app.run(host="0.0.0.0", port=port, debug=debug)
