from mp_scraper.items import Area, Route

expected_items = {
    "areas": {
        "north-dakota": Area(
            _id=106598130,
            name="North Dakota",
            latitude=47.14,
            longitude=-100.433,
            elevation=1000,
            link="https://www.mountainproject.com/area/106598130/north-dakota",
            temp_avgs=[
                {"month": 1, "avg_high": 18, "avg_low": 0},
                {"month": 2, "avg_high": 26, "avg_low": 9},
                {"month": 3, "avg_high": 36, "avg_low": 18},
                {"month": 4, "avg_high": 53, "avg_low": 30},
                {"month": 5, "avg_high": 68, "avg_low": 43},
                {"month": 6, "avg_high": 75, "avg_low": 52},
                {"month": 7, "avg_high": 80, "avg_low": 56},
                {"month": 8, "avg_high": 82, "avg_low": 55},
                {"month": 9, "avg_high": 72, "avg_low": 46},
                {"month": 10, "avg_high": 57, "avg_low": 32},
                {"month": 11, "avg_high": 33, "avg_low": 16},
                {"month": 12, "avg_high": 22, "avg_low": 4},
            ],
            precip_avgs=[
                {"month": 1, "avg_low": 0.5, "avg_high": 3},
                {"month": 2, "avg_low": 0.3, "avg_high": 3},
                {"month": 3, "avg_low": 1.0, "avg_high": 4},
                {"month": 4, "avg_low": 1.4, "avg_high": 5},
                {"month": 5, "avg_low": 2.5, "avg_high": 8},
                {"month": 6, "avg_low": 3.2, "avg_high": 10},
                {"month": 7, "avg_low": 3.6, "avg_high": 9},
                {"month": 8, "avg_low": 1.6, "avg_high": 5},
                {"month": 9, "avg_low": 1.6, "avg_high": 5},
                {"month": 10, "avg_low": 1.5, "avg_high": 3},
                {"month": 11, "avg_low": 0.8, "avg_high": 4},
                {"month": 12, "avg_low": 0.4, "avg_high": 3}
            ]
        ),
        "three-oclock-rock": Area(
            _id=108543607,
            parent_id=106006698,
            name="Three O'clock Rock",
            link="https://www.mountainproject.com/area/108543607/three-oclock-rock",
            latitude=48.159,
            longitude=-121.617,
            elevation=2652,
            temp_avgs=[
                {"month": 1, "avg_high": 41, "avg_low": 28},
                {"month": 2, "avg_high": 46, "avg_low": 30},
                {"month": 3, "avg_high": 52, "avg_low": 33},
                {"month": 4, "avg_high": 60, "avg_low": 37},
                {"month": 5, "avg_high": 66, "avg_low": 42},
                {"month": 6, "avg_high": 71, "avg_low": 47},
                {"month": 7, "avg_high": 78, "avg_low": 50},
                {"month": 8, "avg_high": 77, "avg_low": 50},
                {"month": 9, "avg_high": 71, "avg_low": 45},
                {"month": 10, "avg_high": 60, "avg_low": 39},
                {"month": 11, "avg_high": 48, "avg_low": 33},
                {"month": 12, "avg_high": 42, "avg_low": 30}
            ],
            precip_avgs=[
                {"month": 1, "avg_low": 11.7, "avg_high": 17},
                {"month": 2, "avg_low": 8.7, "avg_high": 14},
                {"month": 3, "avg_low": 8.2, "avg_high": 16},
                {"month": 4, "avg_low": 5.1, "avg_high": 13},
                {"month": 5, "avg_low": 3.6, "avg_high": 12},
                {"month": 6, "avg_low": 2.8, "avg_high": 11},
                {"month": 7, "avg_low": 1.4, "avg_high": 6},
                {"month": 8, "avg_low": 1.6, "avg_high": 7},
                {"month": 9, "avg_low": 3.6, "avg_high": 9},
                {"month": 10, "avg_low": 7.4, "avg_high": 13},
                {"month": 11, "avg_low": 11.8, "avg_high": 16},
                {"month": 12, "avg_low": 12.9, "avg_high": 17}
            ],
            climb_season=[
                {"month": 1, "popularity": 5},
                {"month": 2, "popularity": 3},
                {"month": 3, "popularity": 2},
                {"month": 4, "popularity": 14},
                {"month": 5, "popularity": 83},
                {"month": 6, "popularity": 91},
                {"month": 7, "popularity": 77},
                {"month": 8, "popularity": 104},
                {"month": 9, "popularity": 75},
                {"month": 10, "popularity": 34},
                {"month": 11, "popularity": 31},
                {"month": 12, "popularity": 15},
            ]
        ),
        "ooh-la-la": Area(
            _id=105746817,
            parent_id=105802014,
            name="\"Ooh La La!\"",
            link="https://www.mountainproject.com/area/105746817/ooh-la-la",
            latitude=40.162,
            longitude=-105.668,
            elevation=12945,
            temp_avgs=[
                {"month": 1, "avg_low": 3, "avg_high": 38},
                {"month": 2, "avg_low": 6, "avg_high": 42},
                {"month": 3, "avg_low": 15, "avg_high": 48},
                {"month": 4, "avg_low": 25, "avg_high": 58},
                {"month": 5, "avg_low": 33, "avg_high": 67},
                {"month": 6, "avg_low": 41, "avg_high": 77},
                {"month": 7, "avg_low": 48, "avg_high": 82},
                {"month": 8, "avg_low": 45, "avg_high": 79},
                {"month": 9, "avg_low": 37, "avg_high": 76},
                {"month": 10, "avg_low": 26, "avg_high": 65},
                {"month": 11, "avg_low": 12, "avg_high": 49},
                {"month": 12, "avg_low": 3, "avg_high": 39}
            ],
            precip_avgs=[
                {"month": 1, "avg_low": 1.6, "avg_high": 3},
                {"month": 2, "avg_low": 1.5, "avg_high": 2},
                {"month": 3, "avg_low": 1.7, "avg_high": 2},
                {"month": 4, "avg_low": 2, "avg_high": 4},
                {"month": 5, "avg_low": 1.7, "avg_high": 6},
                {"month": 6, "avg_low": 1.5, "avg_high": 4},
                {"month": 7, "avg_low": 1.9, "avg_high": 10},
                {"month": 8, "avg_low": 1.7, "avg_high": 10},
                {"month": 9, "avg_low": 1.4, "avg_high": 6},
                {"month": 10, "avg_low": 1.3, "avg_high": 4},
                {"month": 11, "avg_low": 1.2, "avg_high": 2},
                {"month": 12, "avg_low": 1.4, "avg_high": 2}
            ],
            climb_season=[
                {"month": 1, "popularity": 2},
                {"month": 2, "popularity": 3},
                {"month": 3, "popularity": 7},
                {"month": 4, "popularity": 15},
                {"month": 5, "popularity": 36},
                {"month": 6, "popularity": 84},
                {"month": 7, "popularity": 249},
                {"month": 8, "popularity": 187},
                {"month": 9, "popularity": 100},
                {"month": 10, "popularity": 23},
                {"month": 11, "popularity": 3},
                {"month": 12, "popularity": 2},
            ]
        ),
    },
    "routes": {
        "ooh-la-la-express": Route(
            _id=105764061,
            parent_id=105746817,
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
            parent_id=105877031,
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
            parent_id=105803123,
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
            parent_id=105717003,
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
            parent_id=105732183,
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
            parent_id=114557650,
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
            parent_id=107340355,
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
            parent_id=109255860,
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
            parent_id=105880707,
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
            parent_id=106031921,
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
            parent_id=105880408,
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
            parent_id=106099665,
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
            parent_id=105747000,
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
            parent_id=110824971,
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
            parent_id=105746985,
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
            parent_id=107282156,
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
