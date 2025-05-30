from typing import Dict, Set, NamedTuple

from BaseClasses import LocationProgressType as LPT
from .options import DredgeOptions


class DredgeLocationData(NamedTuple):
    region: str
    location_group: str
    expansion: str
    requirement: str = ""
    can_catch_rod: bool = True
    can_catch_net: bool = False
    progress_type: LPT = LPT.DEFAULT


location_base_id = 3459028911689314

location_table: Dict[str, DredgeLocationData] = {
    "Fish - Abyssal Gar": DredgeLocationData("Gale Cliffs", "Encyclopedia", "IronRig", "Abyssal"),
    "Fish - All-Seeing Cod": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Anchovy King": DredgeLocationData(
        "Open Ocean", "Encyclopedia", "Base", "Oceanic", can_catch_rod=False, can_catch_net=True
    ),
    "Fish - Anchovy": DredgeLocationData(
        "Open Ocean", "Encyclopedia", "Base", "Oceanic", can_catch_rod=False, can_catch_net=True
    ),
    "Fish - Anglerfish": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Abyssal"),
    "Fish - Anvilfish": DredgeLocationData("The Marrows", "Encyclopedia", "IronRig", "Coastal"),
    "Fish - Arapaima": DredgeLocationData("Twisted Strand", "Encyclopedia", "IronRig", "Mangrove"),
    "Fish - Archon's Burden": DredgeLocationData("Gale Cliffs", "Encyclopedia", "Base", "Abyssal"),
    "Fish - Armored Searobin": DredgeLocationData(
        "Devil's Spine", "Encyclopedia", "Base", "Shallow", can_catch_net=True
    ),
    "Fish - Arrow Squid": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Astral Icefish": DredgeLocationData(
        "The Pale Reach", "Encyclopedia", "PaleReach", "Ice", can_catch_net=True
    ),
    "Fish - Aurora Jellyfish": DredgeLocationData(
        "Stellar Basin", "Encyclopedia", "Base", "Coastal", can_catch_rod=False, can_catch_net=True
    ),
    "Fish - Axial Matron": DredgeLocationData("The Marrows", "Encyclopedia", "IronRig", "Coastal"),
    "Fish - Barbed Eel": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Shallow", can_catch_net=True),
    "Fish - Barracuda": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Shallow"),
    "Fish - Barreleye": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Abyssal"),
    "Fish - Beaked Moonfish": DredgeLocationData("Open Ocean", "Encyclopedia", "Base", "Oceanic"),
    "Fish - Bearded Mackerel": DredgeLocationData("Open Ocean", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Bifurcated Gar": DredgeLocationData("Gale Cliffs", "Encyclopedia", "IronRig", "Abyssal"),
    "Fish - Black Grouper": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Shallow", can_catch_net=True),
    "Fish - Black Sea Bass": DredgeLocationData("Gale Cliffs", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Blackfin Tuna": DredgeLocationData("Open Ocean", "Encyclopedia", "Base", "Oceanic", can_catch_net=True),
    "Fish - Blackmouth Salmon": DredgeLocationData(
        "Gale Cliffs", "Encyclopedia", "Base", "Coastal", can_catch_net=True
    ),
    "Fish - Blacktip Reef Shark": DredgeLocationData(
        "The Marrows", "Encyclopedia", "Base", "Oceanic", can_catch_net=True
    ),
    "Fish - Blistered Tarpon": DredgeLocationData(
        "Twisted Strand", "Encyclopedia", "Base", "Shallow", can_catch_net=True
    ),
    "Fish - Blood Snapper": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Bloodskin Shark": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Oceanic", can_catch_net=True),
    "Fish - Blue Crab": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Crab"),
    "Fish - Blue Mackerel": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Bony Wreckfish": DredgeLocationData("Gale Cliffs", "Encyclopedia", "Base", "Shallow"),
    "Fish - Boreal Shell": DredgeLocationData("Twisted Strand", "Encyclopedia", "IronRig", "Mangrove"),
    "Fish - Boreaspis": DredgeLocationData("Twisted Strand", "Encyclopedia", "IronRig", "Mangrove"),
    "Fish - Broken Arapaima": DredgeLocationData("Twisted Strand", "Encyclopedia", "IronRig", "Mangrove"),
    "Fish - Bronze Whaler": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Oceanic", can_catch_net=True),
    "Fish - Brood Squid": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Brute's Crux": DredgeLocationData("Twisted Strand", "Encyclopedia", "Base", "Mangrove"),
    "Fish - Bubbling Char": DredgeLocationData("The Pale Reach", "Encyclopedia", "Base", "Coastal"),
    "Fish - Bulbous Toothfish": DredgeLocationData("Open Ocean", "Encyclopedia", "PaleReach", "Coastal"),
    "Fish - Bursting Anglerfish": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Abyssal"),
    "Fish - Calcified Snailfish": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Hadal"),
    "Fish - Catfish": DredgeLocationData("Twisted Strand", "Encyclopedia", "Base", "Mangrove", can_catch_net=True),
    "Fish - Cerebral Crab": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Crab"),
    "Fish - Char": DredgeLocationData("The Pale Reach", "Encyclopedia", "PaleReach", "Coastal"),
    "Fish - Charred Sunfish": DredgeLocationData("Open Ocean", "Encyclopedia", "Base", "Oceanic"),
    "Fish - Clawfin Gar": DredgeLocationData("Twisted Strand", "Encyclopedia", "Base", "Mangrove", can_catch_net=True),
    "Fish - Cleft-mouth Shark": DredgeLocationData(
        "The Marrows", "Encyclopedia", "Base", "Oceanic", can_catch_net=True
    ),
    "Fish - Clutching Nautilus": DredgeLocationData("Gale Cliffs", "Encyclopedia", "IronRig", "Oceanic"),
    "Fish - Cod": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Coelacanth": DredgeLocationData("Devil's Spine", "Encyclopedia", "Base", "Abyssal"),
    "Fish - Collapsed Viperfish": DredgeLocationData("Open Ocean", "Encyclopedia", "Base", "Abyssal"),
    "Fish - Colossal Squid": DredgeLocationData(
        "The Pale Reach", "Encyclopedia", "PaleReach", "Ice", can_catch_rod=False, can_catch_net=True
    ),
    "Fish - Common Crab": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Crab"),
    "Fish - Concertina Barracuda": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Shallow"),
    "Fish - Congealed Rattail": DredgeLocationData("Open Ocean", "Encyclopedia", "Base", "Hadal"),
    "Fish - Conger Eel": DredgeLocationData("Gale Cliffs", "Encyclopedia", "Base", "Shallow"),
    "Fish - Consumed Grouper": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Shallow"),
    "Fish - Coral Grouper": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Shallow"),
    "Fish - Cortex Decorator": DredgeLocationData("Gale Cliffs", "Encyclopedia", "Base", "Crab"),
    "Fish - Craterous Seer": DredgeLocationData(
        "The Pale Reach", "Encyclopedia", "PaleReach", "Ice", can_catch_rod=False, can_catch_net=True
    ),
    "Fish - Crawling Instar": DredgeLocationData("Twisted Strand", "Encyclopedia", "IronRig", "Shallow"),
    "Fish - Crown of Nadir": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Crab"),
    "Fish - Crown of Thorns": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Crab"),
    "Fish - Cursed Fangtooth": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Abyssal"),
    "Fish - Cusk Eel": DredgeLocationData("Devil's Spine", "Encyclopedia", "Base", "Volcanic", can_catch_net=True),
    "Fish - Cyclopean Flounder": DredgeLocationData(
        "The Marrows", "Encyclopedia", "Base", "Shallow", can_catch_net=True
    ),
    "Fish - Cystic Trilobite": DredgeLocationData("Gale Cliffs", "Encyclopedia", "IronRig", "Crab"),
    "Fish - Decaying Blackmouth": DredgeLocationData(
        "Gale Cliffs", "Encyclopedia", "Base", "Coastal", can_catch_net=True
    ),
    "Fish - Decorator Crab": DredgeLocationData("Gale Cliffs", "Encyclopedia", "Base", "Crab"),
    "Fish - Decrepit Viperfish": DredgeLocationData("Open Ocean", "Encyclopedia", "Base", "Abyssal"),
    "Fish - Defaced Skate": DredgeLocationData("Devil's Spine", "Encyclopedia", "Base", "Volcanic", can_catch_net=True),
    "Fish - Devil Ray": DredgeLocationData("Gale Cliffs", "Encyclopedia", "Base", "Oceanic", can_catch_net=True),
    "Fish - Drifting Chrysalis": DredgeLocationData("Stellar Basin", "Encyclopedia", "IronRig", "Hadal"),
    "Fish - Dunkleosteus": DredgeLocationData("Devil's Spine", "Encyclopedia", "IronRig", "Volcanic"),
    "Fish - Eagle Shark": DredgeLocationData("Stellar Basin", "Encyclopedia", "IronRig", "Oceanic"),
    "Fish - Effigy Crab": DredgeLocationData("Twisted Strand", "Encyclopedia", "Base", "Crab"),
    "Fish - Entangled Crab": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Crab"),
    "Fish - Enthralled Stonefish": DredgeLocationData(
        "Gale Cliffs", "Encyclopedia", "Base", "Shallow", can_catch_net=True
    ),
    "Fish - Entwined Mullet": DredgeLocationData(
        "Twisted Strand", "Encyclopedia", "Base", "Coastal", can_catch_net=True
    ),
    "Fish - Erupting Scorpion": DredgeLocationData("Devil's Spine", "Encyclopedia", "IronRig", "Crab"),
    "Fish - Excoriated Fiend": DredgeLocationData("Devil's Spine", "Encyclopedia", "IronRig", "Volcanic"),
    "Fish - Fallen Stars": DredgeLocationData("The Pale Reach", "Encyclopedia", "PaleReach", "Crab"),
    "Fish - Famine's End": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Hadal"),
    "Fish - Fanged Cod": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Fangtooth": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Abyssal"),
    "Fish - Feral Lizardfish": DredgeLocationData(
        "The Pale Reach", "Encyclopedia", "PaleReach", "Ice", can_catch_net=True
    ),
    "Fish - Fiddler Crab": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Crab"),
    "Fish - Firefly Squid": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Flayed Mackerel": DredgeLocationData("Open Ocean", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Fractalline Icefish": DredgeLocationData(
        "The Pale Reach", "Encyclopedia", "PaleReach", "Ice", can_catch_net=True
    ),
    "Fish - Frilled Shark": DredgeLocationData("Devil's Spine", "Encyclopedia", "Base", "Volcanic"),
    "Fish - Gar": DredgeLocationData("Twisted Strand", "Encyclopedia", "Base", "Mangrove", can_catch_net=True),
    "Fish - Gazing Shark": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Oceanic"),
    "Fish - Gelatinous Stonefish": DredgeLocationData(
        "Gale Cliffs", "Encyclopedia", "Base", "Shallow", can_catch_net=True
    ),
    "Fish - Ghost Shark": DredgeLocationData("Devil's Spine", "Encyclopedia", "Base", "Abyssal"),
    "Fish - Giant Amphipod": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Hadal"),
    "Fish - Giant Dragonfish": DredgeLocationData("Devil's Spine", "Encyclopedia", "Base", "Hadal"),
    "Fish - Giant Mud Crab": DredgeLocationData("Twisted Strand", "Encyclopedia", "Base", "Crab"),
    "Fish - Glaring Sunfish": DredgeLocationData("Open Ocean", "Encyclopedia", "Base", "Oceanic"),
    "Fish - Gleaming Mullet": DredgeLocationData(
        "Twisted Strand", "Encyclopedia", "Base", "Coastal", can_catch_net=True
    ),
    "Fish - Glowing Octopus": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Shallow"),
    "Fish - Gnashing Perch": DredgeLocationData("Gale Cliffs", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Goblin Shark": DredgeLocationData("The Pale Reach", "Encyclopedia", "PaleReach", "Ice"),
    "Fish - Goliath Tigerfish": DredgeLocationData("Twisted Strand", "Encyclopedia", "Base", "Mangrove"),
    "Fish - Grasping Snail": DredgeLocationData("Devil's Spine", "Encyclopedia", "Base", "Crab"),
    "Fish - Grey Eel": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Shallow", can_catch_net=True),
    "Fish - Grey Mullet": DredgeLocationData("Twisted Strand", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Grinning Gar": DredgeLocationData("Twisted Strand", "Encyclopedia", "Base", "Mangrove", can_catch_net=True),
    "Fish - Grisly Shark": DredgeLocationData("The Pale Reach", "Encyclopedia", "PaleReach", "Ice"),
    "Fish - Grotesque Mackerel": DredgeLocationData(
        "The Marrows", "Encyclopedia", "Base", "Coastal", can_catch_net=True
    ),
    "Fish - Gulf Flounder": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Shallow", can_catch_net=True),
    "Fish - Gulper Eel": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Hadal"),
    "Fish - Hammerhead Shark": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Oceanic"),
    "Fish - Hinged Wolffish": DredgeLocationData("The Pale Reach", "Encyclopedia", "PaleReach", "Ice"),
    "Fish - Hooked Sailfish": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Oceanic", can_catch_net=True),
    "Fish - Horseshoe Crab": DredgeLocationData("Twisted Strand", "Encyclopedia", "Base", "Crab"),
    "Fish - Host Eel": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Shallow", can_catch_net=True),
    "Fish - Icefish": DredgeLocationData("The Pale Reach", "Encyclopedia", "PaleReach", "Ice", can_catch_net=True),
    "Fish - Imperious Lobster": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Crab"),
    "Fish - Infernal Eel": DredgeLocationData("Devil's Spine", "Encyclopedia", "Base", "Volcanic", can_catch_net=True),
    "Fish - Inverted Husk": DredgeLocationData("The Marrows", "Encyclopedia", "IronRig", "Crab"),
    "Fish - Ivory Impaler": DredgeLocationData("The Marrows", "Encyclopedia", "IronRig", "Oceanic"),
    "Fish - Kerygmachela": DredgeLocationData("Stellar Basin", "Encyclopedia", "IronRig", "Hadal"),
    "Fish - King Crab": DredgeLocationData("The Pale Reach", "Encyclopedia", "PaleReach", "Crab"),
    "Fish - King's Wreath": DredgeLocationData("The Pale Reach", "Encyclopedia", "PaleReach", "Crab"),
    "Fish - Lancetfish": DredgeLocationData("Gale Cliffs", "Encyclopedia", "IronRig", "Coastal"),
    "Fish - Latching Snapper": DredgeLocationData(
        "Stellar Basin", "Encyclopedia", "Base", "Coastal", can_catch_net=True
    ),
    "Fish - Leeching Prawn": DredgeLocationData(
        "Open Ocean", "Encyclopedia", "Base", "Oceanic", can_catch_rod=False, can_catch_net=True
    ),
    "Fish - Lizardfish": DredgeLocationData("The Pale Reach", "Encyclopedia", "PaleReach", "Ice", can_catch_net=True),
    "Fish - Longfin Eel": DredgeLocationData("Twisted Strand", "Encyclopedia", "Base", "Mangrove"),
    "Fish - Loosejaw": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Abyssal"),
    "Fish - Lumpy Mackerel": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Mahi Mahi": DredgeLocationData("Stellar Basin", "Encyclopedia", "IronRig", "Oceanic"),
    "Fish - Malignant Pincer": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Crab"),
    "Fish - Many-Eyed Mackerel": DredgeLocationData(
        "The Marrows", "Encyclopedia", "Base", "Coastal", can_catch_net=True
    ),
    "Fish - Medusa Octopus": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Shallow"),
    "Fish - Mimic Slug": DredgeLocationData("Stellar Basin", "Encyclopedia", "IronRig", "Crab"),
    "Fish - Mire Screecher": DredgeLocationData("Twisted Strand", "Encyclopedia", "Base", "Crab"),
    "Fish - Moonfish": DredgeLocationData("Open Ocean", "Encyclopedia", "Base", "Oceanic"),
    "Fish - Nautilus": DredgeLocationData("Gale Cliffs", "Encyclopedia", "IronRig", "Oceanic"),
    "Fish - Nightwing Catfish": DredgeLocationData(
        "Twisted Strand", "Encyclopedia", "Base", "Mangrove", can_catch_net=True
    ),
    "Fish - Nipponites": DredgeLocationData("Twisted Strand", "Encyclopedia", "IronRig", "Crab"),
    "Fish - Oarfish": DredgeLocationData("Gale Cliffs", "Encyclopedia", "Base", "Abyssal"),
    "Fish - Ocean Sunfish": DredgeLocationData("Open Ocean", "Encyclopedia", "Base", "Oceanic"),
    "Fish - Oceanic Perch": DredgeLocationData("Gale Cliffs", "Encyclopedia", "Base", "Coastal"),
    "Fish - Opabinia": DredgeLocationData("Twisted Strand", "Encyclopedia", "IronRig", "Shallow"),
    "Fish - Ossified Searobin": DredgeLocationData(
        "Devil's Spine", "Encyclopedia", "Base", "Shallow", can_catch_net=True
    ),
    "Fish - Osteostracan": DredgeLocationData("The Marrows", "Encyclopedia", "IronRig", "Shallow"),
    "Fish - Paddlefish": DredgeLocationData("The Marrows", "Encyclopedia", "IronRig", "Coastal"),
    "Fish - Pale Grasper": DredgeLocationData(
        "The Pale Reach", "Encyclopedia", "PaleReach", "Ice", can_catch_rod=False, can_catch_net=True
    ),
    "Fish - Pale Skate": DredgeLocationData("Devil's Spine", "Encyclopedia", "Base", "Volcanic", can_catch_net=True),
    "Fish - Parhelion Jellyfish": DredgeLocationData(
        "Stellar Basin", "Encyclopedia", "Base", "Coastal", can_catch_rod=False, can_catch_net=True
    ),
    "Fish - Perished Loosejaw": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Abyssal"),
    "Fish - Plated Barbjaw": DredgeLocationData("Devil's Spine", "Encyclopedia", "IronRig", "Shallow"),
    "Fish - Plated Osteostracan": DredgeLocationData("The Marrows", "Encyclopedia", "IronRig", "Shallow"),
    "Fish - Primordial Shadow": DredgeLocationData("Twisted Strand", "Encyclopedia", "IronRig", "Mangrove"),
    "Fish - Radiant Squid": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Rapt Shark": DredgeLocationData("Devil's Spine", "Encyclopedia", "Base", "Abyssal"),
    "Fish - Rattail": DredgeLocationData("Open Ocean", "Encyclopedia", "Base", "Hadal"),
    "Fish - Razormouth Tuna": DredgeLocationData("Open Ocean", "Encyclopedia", "Base", "Oceanic", can_catch_net=True),
    "Fish - Red Snapper": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Riddled Flounder": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Shallow", can_catch_net=True),
    "Fish - Rock Crab": DredgeLocationData("Gale Cliffs", "Encyclopedia", "Base", "Crab"),
    "Fish - Ruptured Vessel": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Hadal"),
    "Fish - Sable Reacher": DredgeLocationData("Devil's Spine", "Encyclopedia", "Base", "Crab"),
    "Fish - Sailfish": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Oceanic", can_catch_net=True),
    "Fish - Sallow Sailfish": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Oceanic", can_catch_net=True),
    "Fish - Sanguine Shark": DredgeLocationData("Stellar Basin", "Encyclopedia", "IronRig", "Oceanic"),
    "Fish - Savage Barracuda": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Shallow"),
    "Fish - Sawfish": DredgeLocationData("Devil's Spine", "Encyclopedia", "IronRig", "Shallow"),
    "Fish - Scarlet Prawn": DredgeLocationData(
        "Open Ocean", "Encyclopedia", "Base", "Oceanic", can_catch_rod=False, can_catch_net=True
    ),
    "Fish - Scouring Bass": DredgeLocationData("Gale Cliffs", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Sea Cucumber": DredgeLocationData("The Marrows", "Encyclopedia", "IronRig", "Crab"),
    "Fish - Sea Scorpion": DredgeLocationData("Devil's Spine", "Encyclopedia", "IronRig", "Crab"),
    "Fish - Sea Slug": DredgeLocationData("Stellar Basin", "Encyclopedia", "IronRig", "Crab"),
    "Fish - Sea Stars": DredgeLocationData("The Pale Reach", "Encyclopedia", "PaleReach", "Crab"),
    "Fish - Seizing Snailfish": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Hadal"),
    "Fish - Sergeant Fish": DredgeLocationData(
        "Twisted Strand", "Encyclopedia", "Base", "Mangrove", can_catch_net=True
    ),
    "Fish - Serpentine Mackerel": DredgeLocationData(
        "Devil's Spine", "Encyclopedia", "Base", "Coastal", can_catch_net=True
    ),
    "Fish - Shaper's Prime": DredgeLocationData("Devil's Spine", "Encyclopedia", "Base", "Abyssal"),
    "Fish - Shard Ray": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Shallow"),
    "Fish - Shattered Wreckfish": DredgeLocationData("Gale Cliffs", "Encyclopedia", "Base", "Shallow"),
    "Fish - Silvering Lancetfish": DredgeLocationData("Gale Cliffs", "Encyclopedia", "IronRig", "Coastal"),
    "Fish - Skeletal Moonfish": DredgeLocationData("Open Ocean", "Encyclopedia", "Base", "Oceanic"),
    "Fish - Sleeper Shark": DredgeLocationData("The Pale Reach", "Encyclopedia", "PaleReach", "Ice"),
    "Fish - Sleeper's Torment": DredgeLocationData("The Pale Reach", "Encyclopedia", "PaleReach", "Ice"),
    "Fish - Snag Squid": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Snailfish": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Hadal"),
    "Fish - Snake Mackerel": DredgeLocationData("Devil's Spine", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Sollasina": DredgeLocationData("Gale Cliffs", "Encyclopedia", "IronRig", "Shallow"),
    "Fish - Spider Crab": DredgeLocationData("Devil's Spine", "Encyclopedia", "Base", "Crab"),
    "Fish - Spiny Lobster": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Crab"),
    "Fish - Splintered Crab": DredgeLocationData("Gale Cliffs", "Encyclopedia", "Base", "Crab"),
    "Fish - Sprouting Eel": DredgeLocationData("Gale Cliffs", "Encyclopedia", "Base", "Shallow"),
    "Fish - Squat Lobster": DredgeLocationData("Devil's Spine", "Encyclopedia", "Base", "Crab"),
    "Fish - Stalking Spiderfish": DredgeLocationData("Stellar Basin", "Encyclopedia", "IronRig", "Abyssal"),
    "Fish - Stargazer": DredgeLocationData(
        "The Pale Reach", "Encyclopedia", "PaleReach", "Ice", can_catch_rod=False, can_catch_net=True
    ),
    "Fish - Stingray": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Shallow"),
    "Fish - Stonefish": DredgeLocationData("Gale Cliffs", "Encyclopedia", "Base", "Shallow", can_catch_net=True),
    "Fish - Sturgeon": DredgeLocationData("Gale Cliffs", "Encyclopedia", "Base", "Oceanic", can_catch_net=True),
    "Fish - Swordfish": DredgeLocationData("The Marrows", "Encyclopedia", "IronRig", "Oceanic"),
    "Fish - Tarpon": DredgeLocationData("Twisted Strand", "Encyclopedia", "Base", "Shallow", can_catch_net=True),
    "Fish - Tattered Mackerel": DredgeLocationData(
        "Devil's Spine", "Encyclopedia", "Base", "Coastal", can_catch_net=True
    ),
    "Fish - Thawed Icefish": DredgeLocationData(
        "The Pale Reach", "Encyclopedia", "PaleReach", "Ice", can_catch_net=True
    ),
    "Fish - Three-Headed Cod": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Tiger Mackerel": DredgeLocationData("Open Ocean", "Encyclopedia", "Base", "Coastal", can_catch_net=True),
    "Fish - Toothfish": DredgeLocationData("Open Ocean", "Encyclopedia", "PaleReach", "Coastal"),
    "Fish - Translucent Sturgeon": DredgeLocationData(
        "Gale Cliffs", "Encyclopedia", "Base", "Oceanic", can_catch_net=True
    ),
    "Fish - Trilobite": DredgeLocationData("Gale Cliffs", "Encyclopedia", "IronRig", "Crab"),
    "Fish - Tripod Spiderfish": DredgeLocationData("Stellar Basin", "Encyclopedia", "IronRig", "Abyssal"),
    "Fish - Tullimonstrum": DredgeLocationData("The Marrows", "Encyclopedia", "IronRig", "Coastal"),
    "Fish - Tusked Grouper": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Shallow", can_catch_net=True),
    "Fish - Twinned Eels": DredgeLocationData("Twisted Strand", "Encyclopedia", "Base", "Mangrove"),
    "Fish - Twisted Shark": DredgeLocationData("Devil's Spine", "Encyclopedia", "Base", "Volcanic"),
    "Fish - Umbral Puppet": DredgeLocationData("Devil's Spine", "Encyclopedia", "Base", "Crab"),
    "Fish - Untouchable Wyrmfish": DredgeLocationData("Devil's Spine", "Encyclopedia", "Base", "Hadal"),
    "Fish - Unveiled Vetulicolia": DredgeLocationData("Devil's Spine", "Encyclopedia", "IronRig", "Volcanic"),
    "Fish - Vagrant Sollasina": DredgeLocationData("Gale Cliffs", "Encyclopedia", "IronRig", "Shallow"),
    "Fish - Vetulicolia": DredgeLocationData("Devil's Spine", "Encyclopedia", "IronRig", "Volcanic"),
    "Fish - Viperfish": DredgeLocationData("Open Ocean", "Encyclopedia", "Base", "Abyssal"),
    "Fish - Voideye": DredgeLocationData("Stellar Basin", "Encyclopedia", "Base", "Abyssal"),
    "Fish - Volcano Snail": DredgeLocationData("Devil's Spine", "Encyclopedia", "Base", "Crab"),
    "Fish - Voltaic Grouper": DredgeLocationData("The Marrows", "Encyclopedia", "Base", "Shallow", can_catch_net=True),
    "Fish - Vortex Interloper": DredgeLocationData(
        "Twisted Strand", "Encyclopedia", "Base", "Mangrove", can_catch_net=True
    ),
    "Fish - Withered Ray": DredgeLocationData("Gale Cliffs", "Encyclopedia", "Base", "Oceanic", can_catch_net=True),
    "Fish - Wolffish": DredgeLocationData("The Pale Reach", "Encyclopedia", "PaleReach", "Ice"),
    "Fish - Wreckfish": DredgeLocationData("Gale Cliffs", "Encyclopedia", "Base", "Shallow"),
    "Fish - Wretched Nipper": DredgeLocationData("Twisted Strand", "Encyclopedia", "IronRig", "Crab"),
    "Fish - Xeno Xeno": DredgeLocationData("Stellar Basin", "Encyclopedia", "IronRig", "Oceanic"),
    "Fish - Xiphactinus": DredgeLocationData("Twisted Strand", "Encyclopedia", "IronRig", "Mangrove"),
    "Research - Hydraulic Rod": DredgeLocationData("Open Ocean", "Research", "Base"),
    "Research - Flexible Fishing Pole": DredgeLocationData("Open Ocean", "Research", "Base"),
    "Research - Heat-Resistant Line": DredgeLocationData("Open Ocean", "Research", "Base", "Early"),
    "Research - Anti-Tangle Line": DredgeLocationData("Open Ocean", "Research", "Base", "Early"),
    "Research - Versatile Rod": DredgeLocationData("Open Ocean", "Research", "Base", "Mid"),
    "Research - Harvesting Platform": DredgeLocationData("Open Ocean", "Research", "Base", "All"),
    "Research - Bottomless Lines": DredgeLocationData("Open Ocean", "Research", "Base", "Early"),
    "Research - Fathomless Winch": DredgeLocationData("Open Ocean", "Research", "Base", "Mid"),
    "Research - Improved Outboard Engine": DredgeLocationData("Open Ocean", "Research", "Base"),
    "Research - Jet Drive Engine": DredgeLocationData("Open Ocean", "Research", "Base", "Mid"),
    "Research - Refined Outboard Engine": DredgeLocationData("Open Ocean", "Research", "Base", "Early"),
    "Research - Twin Prop Engine": DredgeLocationData("Open Ocean", "Research", "Base", "Early"),
    "Research - Twin Jet Drive Engine": DredgeLocationData("Open Ocean", "Research", "Base", "Late"),
    "Research - Engine Stack": DredgeLocationData("Open Ocean", "Research", "Base", "All"),
    "Research - Efficient Crab Pot": DredgeLocationData("Open Ocean", "Research", "Base"),
    "Research - Hardy Crab Pot": DredgeLocationData("Open Ocean", "Research", "Base"),
    "Research - Large Crab Pot": DredgeLocationData("Open Ocean", "Research", "Base"),
    "Research - Complex Crab Pot": DredgeLocationData("Open Ocean", "Research", "Base", "Early"),
    "Research - Massive Crab Pot": DredgeLocationData("Open Ocean", "Research", "Base", "Early"),
    "Research - Reinforced Crab Pot": DredgeLocationData("Open Ocean", "Research", "Base", "Late"),
    "Research - Improved Trawl Net": DredgeLocationData("Open Ocean", "Research", "Base"),
    "Research - Silt Filtering Trawl Net": DredgeLocationData("Open Ocean", "Research", "Base", "Early"),
    "Research - Large Trawl Net": DredgeLocationData("Open Ocean", "Research", "Base", "Early"),
    "Research - Tempered Mesh Net": DredgeLocationData("Open Ocean", "Research", "Base", "Early"),
    "Research - Heavy-Duty Trawl Net": DredgeLocationData("Open Ocean", "Research", "Base", "Mid"),
    "Relic - Ornate Key": DredgeLocationData("Open Ocean", "Relic", "Base"),
    "Relic - Rusted Music Box": DredgeLocationData("Open Ocean", "Relic", "Base"),
    "Relic - Jewel Encrusted Band": DredgeLocationData("Open Ocean", "Relic", "Base"),
    "Relic - Shimmering Necklace": DredgeLocationData("Open Ocean", "Relic", "Base"),
    "Relic - Antique Pocket Watch": DredgeLocationData("Open Ocean", "Relic", "Base"),
    "Quest - Sampling Device": DredgeLocationData("Open Ocean", "Quest", "Base"),
    "Shop - Simple Skimmer": DredgeLocationData("Open Ocean", "Shop", "Base"),
    "Shop - Weighted Line": DredgeLocationData("Open Ocean", "Shop", "Base"),
    "Shop - Barbed Ice Rod": DredgeLocationData("Open Ocean", "Shop", "PaleReach"),
    "Shop - Glacial Lance": DredgeLocationData("Open Ocean", "Shop", "PaleReach"),
    "Shop - Infused Rod": DredgeLocationData("Open Ocean", "Shop", "IronRig"),
    "Shop - Infused Winch": DredgeLocationData("Open Ocean", "Shop", "IronRig"),
    "Shop - Infused Hoist": DredgeLocationData("Open Ocean", "Shop", "IronRig"),
    "Shop - Infused Coiling Rod": DredgeLocationData("Open Ocean", "Shop", "IronRig"),
    "Shop - Infused Fireproof Rod": DredgeLocationData("Open Ocean", "Shop", "IronRig"),
    "World - Sinew Spindle": DredgeLocationData("Open Ocean", "World", "Base"),
    "World - Viscera Crane": DredgeLocationData("Open Ocean", "World", "Base"),
    "World - Tendon Rod": DredgeLocationData("Open Ocean", "World", "Base"),
    "World - Encrusted Talisman": DredgeLocationData("Open Ocean", "World", "Base"),
    "World - Basic Fishing Pole": DredgeLocationData("Open Ocean", "World", "Base"),
}

location_name_to_id: Dict[str, int] = {name: location_base_id + index for index, name in enumerate(location_table)}

def get_player_location_table(options: DredgeOptions) -> Dict[str, int]:
    all_locations: Dict[str, int] = {}
    base_locations = {name: location_base_id + index for index, (name, location)
                      in enumerate(location_table.items()) if location.expansion == "Base"}
    iron_rig_locations = {name: location_base_id + index for index, (name, location)
                      in enumerate(location_table.items()) if location.expansion == "IronRig"}
    pale_reach_locations = {name: location_base_id + index for index, (name, location)
                      in enumerate(location_table.items()) if location.expansion == "PaleReach"}

    all_locations.update(base_locations)

    if options.include_iron_rig_dlc:
        all_locations.update(iron_rig_locations)
    if options.include_pale_reach_dlc:
        all_locations.update(pale_reach_locations)

    # removing these checks while waiting for fix from mod
    excluded_groups = {"Shop", "Quest", "World", "Relic"}
    all_locations = {
        name: id
        for name, id in all_locations.items()
        if location_table[name].location_group not in excluded_groups
    }

    return all_locations

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    loc_group_name = loc_name.split(" - ", 1)[0]
    location_name_groups.setdefault(loc_group_name, set()).add(loc_name)
    if loc_data.location_group:
        location_name_groups.setdefault(loc_data.location_group, set()).add(loc_name)
