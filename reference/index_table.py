# REFERENCE_TABLE = {
#     'human': 13 - 1,
#     'car': 21 - 1,
#     'bus': 81 - 1,
#     'truck': 84 - 1,
#     'sky': 3 - 1,
#     'wall': 1 - 1,
#     'skyscraper': 49 - 1,
#     'building': 2 - 1,
#     'fence': 33 - 1,
#     'railing': 39 - 1,
#     'bannister': 96 - 1,
#     'tree': 5 - 1,
#     'grass': 10 - 1,
#     'plant': 18 - 1,
#     'flower': 67 - 1,
#     'palm': 73 - 1,
#     'chair': 20 - 1,
#     'armchair': 31 - 1,
#     'desk': 34 - 1,
#     'pillar': 43 - 1,
#     'signboard': 44 - 1,
#     'path': 53 - 1,
#     'stairway': 60 - 1,
#     'bench': 70 - 1,
#     'swivel': 76 - 1,
#     'lamp': 88 - 1,
#     'escalator': 97 - 1,
#     'trafficlight': 137 - 1,
#     'road': 7 - 1,
#     'sidewalk': 12 - 1,
#     'stairs': 54 - 1,
#     'runway': 55 - 1,
# }
REFERENCE_TABLE = {
    # Person
    "Person": 13 - 1,
    # Bike
    "Bike": 128 - 1,
    "MotorBike": 117 - 1,
    # Heavy V
    "Heavy Vehicle": 84 - 1,
    # Light V
    "Van": 103 - 1,
    "Car": 21 - 1,
    "Bus": 81 - 1,
    # Facade
    "Wall": 1 - 1,
    "House": 26 - 1,
    "Building": 2 - 1,
    "Skyscraper": 49 - 1,
    "Hovel": 80 - 1,
    # Window&Opening
    "Window": 9 - 1,
    "Door": 15 - 1,
    # Road
    "Road": 7 - 1,
    # Sidewalk
    "Sidewalk": 12 - 1,
    # StreetFurniture
    "Streetlight": 88 - 1,
    "Bench": 70 - 1,
    "Chair": 76 - 1,
    "Seat": 32 - 1,
    "Awning": 87 - 1,
    "Booth": 89 - 1,
    "Sign": 44 - 1,
    # Greenery-Tree
    "Tree": 5 - 1,
    "Palm": 73 - 1,
    # Greenery-Grass&Shrubs
    "Grass": 10 - 1,
    "Plant": 18 - 1,
    "Flower": 67 - 1,
    # Sky
    "Sky": 3 - 1,
    # Nature
    "Hill": 69 - 1,
    "Lake": 129 - 1,
    "Waterfall": 114 - 1,
    "Mountain": 17 - 1,
    "Water": 22 - 1,
    "River": 61 - 1,
    "Sea": 27 - 1,
    "Rock": 35 - 1
}
GROUPS = {
    "Person": ['Person'],
    "Bike": ['Bike', 'MotorBike'],
    "HeavyV": ['Heavy Vehicle'],
    "LightV": ['Van', 'Car', 'Bus'],
    "Facade": ['Wall', 'House', 'Building', 'Skyscraper', 'Hovel'],
    "WindowOpening": ['Window', 'Door'],
    "Road": ['Road'],
    "Sidewalk": ['Sidewalk'],
    "StreetFurniture":
    ['Streetlight', 'Bench', 'Chair', 'Seat', 'Awning', 'Booth', 'Sign'],
    "GreeneryTree": ['Tree', 'Palm'],
    "GreeneryGrass": ['Grass', 'Plant', 'Flower'],
    "Sky": ['Sky'],
    "Nature":
    ['Hill', 'Lake', 'Waterfall', 'Mountain', 'Water', 'River', 'Sea', 'Rock']
}
# GROUPS = {
#     'human': ['human'],
#     'car': ['car', 'bus', 'truck'],
#     'sky': ['sky'],
#     'green': ['tree', 'grass', 'plant', 'flower', 'palm'],
#     'boundary': ['fence', 'railing', 'wall', 'bannister'],
#     'building': ['skyscraper', 'building'],
#     'constructor': ['pillar'],
#     'lighting': ['lamp'],
#     'pinterest': ['chair', 'armchair', 'desk', 'bench', 'swivel'],
#     'sign': ['signboard', 'trafficlight'],
#     'walkpath':
#     ['escalator', 'sidewalk', 'stairs', 'runway', 'stairway', 'path'],
#     'road': ['road']
# }

# INDEX_GROUPS_Numerator = {
#     'SBI': ['boundary'],
#     'SLI': ['lighting'],
#     'SVI': ['constructor'],
#     'TFI': ['human', 'car'],
#     'PSI': ['walkpath'],
#     'SI': ['sky'],
#     'GVI': ['green'],
#     'SAI': ['pinterest'],
#     'EPI': ['building', 'green', 'boundary'],
#     'EPI_D': ['walkpath', 'road'],
#     'AI': ['walkpath', 'road'],
#     'AI_D': ['boundary']
# }
INDEX_GROUPS_Numerator = {
    "Person": ['Person'],
    "Bike": ['Bike'],
    "HeavyV": ['HeavyV'],
    "LightV": ["LightV"],
    "Facade": ["Facade"],
    "WindowOpening": ['WindowOpening'],
    "Road": ['Road'],
    "Sidewalk": ['Sidewalk'],
    "StreetFurniture": ["StreetFurniture"],
    "GreeneryTree": ['GreeneryTree'],
    "GreeneryGrass": ['GreeneryGrass'],
    "Sky": ['Sky'],
    "Nature": ["Nature"]
}
