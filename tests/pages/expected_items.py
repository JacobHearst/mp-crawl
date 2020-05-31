from mp_scraper.items import Area, Route

expected_items = {
    "areas": {
        "north-dakota": Area(
            _id=106598130,
            name="North Dakota",
            coords={
                "type": "Point",
                "coordinates": [-100.433, 47.14]
            },
            elevation=1000,
            link="https://www.mountainproject.com/area/106598130/north-dakota",
            temp_avgs={
                "1": { "avg_high": 18, "avg_low": 0 },
                "2": { "avg_high": 26, "avg_low": 9 },
                "3": { "avg_high": 36, "avg_low": 18 },
                "4": { "avg_high": 53, "avg_low": 30 },
                "5": { "avg_high": 68, "avg_low": 43 },
                "6": { "avg_high": 75, "avg_low": 52 },
                "7": { "avg_high": 80, "avg_low": 56 },
                "8": { "avg_high": 82, "avg_low": 55 },
                "9": { "avg_high": 72, "avg_low": 46 },
                "10": { "avg_high": 57, "avg_low": 32 },
                "11": { "avg_high": 33, "avg_low": 16 },
                "12": { "avg_high": 22, "avg_low": 4 },
            },
            precip_avgs={
                "1": { "avg_low": 0.5, "avg_high": 3},
                "2": { "avg_low": 0.3, "avg_high": 3},
                "3": { "avg_low": 1.0, "avg_high": 4},
                "4": { "avg_low": 1.4, "avg_high": 5},
                "5": { "avg_low": 2.5, "avg_high": 8},
                "6": { "avg_low": 3.2, "avg_high": 10},
                "7": { "avg_low": 3.6, "avg_high": 9},
                "8": { "avg_low": 1.6, "avg_high": 5},
                "9": { "avg_low": 1.6, "avg_high": 5},
                "10": { "avg_low": 1.5, "avg_high": 3},
                "11": { "avg_low": 0.8, "avg_high": 4},
                "12": { "avg_low": 0.4, "avg_high": 3}
            },
            climb_season={}
        ),
        "three-oclock-rock": Area(
            _id=108543607,
            ancestors=[105708966, 108471385, 106006698],
            name="Three O'clock Rock",
            link="https://www.mountainproject.com/area/108543607/three-oclock-rock",
            coords={
                "type": "Point",
                "coordinates": [-121.617, 48.159]
            },
            elevation=2652,
            temp_avgs={
                "1": {"avg_high": 41, "avg_low": 28},
                "2": {"avg_high": 46, "avg_low": 30},
                "3": {"avg_high": 52, "avg_low": 33},
                "4": {"avg_high": 60, "avg_low": 37},
                "5": {"avg_high": 66, "avg_low": 42},
                "6": {"avg_high": 71, "avg_low": 47},
                "7": {"avg_high": 78, "avg_low": 50},
                "8": {"avg_high": 77, "avg_low": 50},
                "9": {"avg_high": 71, "avg_low": 45},
                "10": {"avg_high": 60, "avg_low": 39},
                "11": {"avg_high": 48, "avg_low": 33},
                "12": {"avg_high": 42, "avg_low": 30}
            },
            precip_avgs={
                "1": {"avg_low": 11.7, "avg_high": 17},
                "2": {"avg_low": 8.7, "avg_high": 14},
                "3": {"avg_low": 8.2, "avg_high": 16},
                "4": {"avg_low": 5.1, "avg_high": 13},
                "5": {"avg_low": 3.6, "avg_high": 12},
                "6": {"avg_low": 2.8, "avg_high": 11},
                "7": {"avg_low": 1.4, "avg_high": 6},
                "8": {"avg_low": 1.6, "avg_high": 7},
                "9": {"avg_low": 3.6, "avg_high": 9},
                "10": {"avg_low": 7.4, "avg_high": 13},
                "11": {"avg_low": 11.8, "avg_high": 16},
                "12": {"avg_low": 12.9, "avg_high": 17}
            },
            climb_season={
                "1": 5,
                "2": 3,
                "3": 2,
                "4": 14,
                "5": 83,
                "6": 91,
                "7": 77,
                "8": 104,
                "9": 75,
                "10": 34,
                "11": 31,
                "12": 15,
            }
        ),
        "ooh-la-la": Area(
            _id=105746817,
            ancestors=[105708956, 105744466, 105802014],
            name="\"Ooh La La!\"",
            link="https://www.mountainproject.com/area/105746817/ooh-la-la",
            coords={
                "type": "Point",
                "coordinates": [-105.668, 40.162]
            },
            elevation=12945,
            temp_avgs={
                "1": { "avg_low": 3, "avg_high": 38},
                "2": { "avg_low": 6, "avg_high": 42},
                "3": { "avg_low": 15, "avg_high": 48},
                "4": { "avg_low": 25, "avg_high": 58},
                "5": { "avg_low": 33, "avg_high": 67},
                "6": { "avg_low": 41, "avg_high": 77},
                "7": { "avg_low": 48, "avg_high": 82},
                "8": { "avg_low": 45, "avg_high": 79},
                "9": { "avg_low": 37, "avg_high": 76},
                "10": { "avg_low": 26, "avg_high": 65},
                "11": { "avg_low": 12, "avg_high": 49},
                "12": { "avg_low": 3, "avg_high": 39}
            },
            precip_avgs={
                "1": { "avg_low": 1.6, "avg_high": 3},
                "2": { "avg_low": 1.5, "avg_high": 2},
                "3": { "avg_low": 1.7, "avg_high": 2},
                "4": { "avg_low": 2, "avg_high": 4},
                "5": { "avg_low": 1.7, "avg_high": 6},
                "6": { "avg_low": 1.5, "avg_high": 4},
                "7": { "avg_low": 1.9, "avg_high": 10},
                "8": { "avg_low": 1.7, "avg_high": 10},
                "9": { "avg_low": 1.4, "avg_high": 6},
                "10": { "avg_low": 1.3, "avg_high": 4},
                "11": { "avg_low": 1.2, "avg_high": 2},
                "12": { "avg_low": 1.4, "avg_high": 2}
            },
            climb_season={
                "1": 2,
                "2": 3,
                "3": 7,
                "4": 15,
                "5": 36,
                "6": 84,
                "7": 249,
                "8": 187,
                "9": 100,
                "10": 23,
                "11": 3,
                "12": 2
            }
        ),
    },
    "routes": {
        "ooh-la-la-express": Route(
            _id=105764061,
            ancestors=[105708956, 105744466, 105802014, 105746817],
            name="Ooh La La Express",
            types=["Trad", "Snow", "Alpine"],
            rating=2,
            link="https://www.mountainproject.com/route/105764061/ooh-la-la-express",
            length="II",
            height=500,
            grades={
                "snow": { "grade": "Mod. Snow", "sort_index": 1 }
            }
        ),
        "liberty-ridge": Route(
            _id=106459197,
            ancestors=[105708966, 108471329, 105877031],
            name="Liberty Ridge",
            types=["Ice", "Snow", "Alpine"],
            rating=3.8,
            link="https://www.mountainproject.com/route/106459197/liberty-ridge",
            length="IV",
            height=10500,
            grades={
                "ice": { "grade": "AI2-3", "sort_index": 5 },
                "snow": { "grade": "Steep Snow", "sort_index": 2 }
            }
        ),
        "upper-exum-ridge": Route(
            _id=105933562,
            ancestors=[105708960, 105802912, 105803123],
            name="Upper Exum Ridge",
            types=["Trad", "Alpine"],
            rating=3.6,
            link="https://www.mountainproject.com/route/105933562/upper-exum-ridge",
            length="II",
            height=1700,
            pitches=12,
            grades={
                "yds": { "grade": "5.5", "sort_index": 19 }
            }
        ),
        "the-moonlight-buttress-free": Route(
            _id=106138026,
            ancestors=[105708957, 105716799, 105717003],
            name="The Moonlight Buttress (Free)",
            types=["Trad"],
            rating=3.9,
            link="https://www.mountainproject.com/route/106138026/the-moonlight-buttress-free",
            height=1200,
            pitches=10,
            grades={
                "yds": { "grade": "5.12c", "sort_index": 51 }
            }
        ),
        "the-original-route": Route(
            _id=105732410,
            ancestors=[105708961, 113755154, 105731932, 105731974, 105732183],
            name="The Original Route",
            types=["Trad"],
            rating=4,
            link="https://www.mountainproject.com/route/105732410/the-original-route",
            height=1000,
            pitches=14,
            grades={
                "yds": { "grade": "5.12-", "sort_index": 48 },
            }
        ),
        "regular-northwest-face-of-half-dome": Route(
            _id=105912416,
            ancestors=[
                105708959,
                105833381,
                105833388,
                118097922,
                105833395,
                114557650
            ],
            name="Regular Northwest Face of Half Dome",
            types=["Trad", "Aid"],
            rating=3.9,
            link="https://www.mountainproject.com/route/105912416/regular-northwest-face-of-half-dome",
            height=2200,
            length="VI",
            pitches=23,
            grades={
                "yds": { "grade": "5.9", "sort_index": 31 },
                "aid": { "grade": "C1", "sort_index": 4 },
            }
        ),
        "moby-grape": Route(
            _id=105884815,
            ancestors=[105872225, 107340274, 107340355],
            name="Moby Grape",
            types=["Trad", "Alpine"],
            rating=3.8,
            link="https://www.mountainproject.com/route/105884815/moby-grape",
            height=800,
            length="III",
            pitches=7,
            grades={
                "yds": { "grade": "5.8", "sort_index": 28 },
                "danger": { "grade": "PG13", "sort_index": 0 },
            }
        ),
        "invisible-touch": Route(
            _id=109513995,
            ancestors=[105812481, 109253227, 110040864, 109255860],
            name="Invisible Touch",
            types=["Boulder"],
            rating=4,
            link="https://www.mountainproject.com/route/109513995/invisible-touch",
            grades={
                "hueco": { "grade": "V8", "sort_index": 26 }
            }
        ),
        "planet-of-the-apes": Route(
            _id=106318953,
            ancestors=[105708957, 105880382, 105880388, 105880707],
            name="Planet of the Apes",
            types=["Boulder"],
            height=12,
            rating=3.8,
            link="https://www.mountainproject.com/route/106318953/planet-of-the-apes",
            grades={
                "hueco": { "grade": "V7-", "sort_index": 22 }
            }
        ),
        "the-red-house-extension": Route(
            _id=108027966,
            ancestors=[105887760, 106031921],
            name="The Red House Extension",
            types=["Boulder"],
            height=15,
            rating=3.5,
            link="https://www.mountainproject.com/route/108027966/the-red-house-extension",
            grades={
                "hueco": { "grade": "V7+", "sort_index": 24 }
            }
        ),
        "feels-like-grit": Route(
            _id=105938571,
            ancestors=[105708957, 105880382, 105880391, 105880408],
            name="Feels Like Grit",
            types=["Boulder"],
            height=15,
            rating=3.2,
            link="https://www.mountainproject.com/route/105938571/feels-like-grit",
            grades={
                "hueco": { "grade": "V6-7", "sort_index": 21 }
            }
        ),
        "black-dike": Route(
            _id=105890633,
            ancestors=[105872225, 106099658, 114088875, 106099665],
            name="Black Dike",
            types=["Mixed", "Ice"],
            height=500,
            pitches=3,
            length="IV",
            rating=3.9,
            link="https://www.mountainproject.com/route/105890633/black-dike",
            grades={
                "yds": { "grade": "5.6", "sort_index": 22 },
                "ice": { "grade": "WI4-5", "sort_index": 11 },
                "mixed": { "grade": "M3", "sort_index": 7 }
            }
        ),
        "ames-ice-hose": Route(
            _id=105747549,
            ancestors=[105708956, 105807296, 105744518, 105747000],
            name="Ames Ice Hose",
            types=["Trad", "Mixed", "Ice"],
            height=520,
            pitches=3,
            length="III",
            rating=4.0,
            link="https://www.mountainproject.com/route/105747549/ames-ice-hose",
            grades={
                "ice": { "grade": "WI5", "sort_index": 13 },
                "danger": { "grade": "R", "sort_index": 1 },
                "mixed": { "grade": "M6", "sort_index": 16 },
            }
        ),
        "cosmiques-arete": Route(
            _id=107497087,
            ancestors=[
                105907743,
                106660030,
                106192575,
                110824749,
                110824830,
                110824971
            ],
            name="Cosmiques Arête",
            types=["Trad", "Mixed", "Ice", "Snow", "Alpine"],
            height=1000,
            pitches=2,
            length="II",
            rating=3.8,
            link="https://www.mountainproject.com/route/107497087/cosmiques-arete",
            grades={
                "yds": { "grade": "5.6", "sort_index": 22 },
                "ice": { "grade": "AI2", "sort_index": 4 },
                "mixed": { "grade": "M4", "sort_index": 10 },
                "snow": { "grade": "Mod. Snow", "sort_index": 1 },
            }
        ),
        "skylight": Route(
            _id=105747482,
            ancestors=[105708956, 105807296, 105744521, 105746985],
            name="Skylight",
            types=["Trad", "Mixed", "Ice"],
            pitches=3,
            length="II",
            rating=3.8,
            link="https://www.mountainproject.com/route/105747482/skylight",
            grades={
                "ice": { "grade": "WI4+", "sort_index": 11 },
                "mixed": { "grade": "M4-5", "sort_index": 11 },
            }
        ),
        "rock": Route(
            _id=107350537,
            ancestors=[
                105852400,
                110848199,
                106477419,
                107281942,
                107281993,
                107282156
            ],
            name="Rock",
            types=["Boulder"],
            height=8,
            rating=1.0,
            link="https://www.mountainproject.com/route/107350537/rock",
            grades={
                "hueco": { "grade": "V-easy", "sort_index": 0 }
            }
        )
    }
}
