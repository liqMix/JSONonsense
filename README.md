# JSONonsense
A generator for creating arbitrary JSON objects from various sources.

## Configured values
##### MIN_KEY_PER_OBJECT | MAX_KEY_PER_OBJECT
The minimum and maximum number of keys per object.

##### MAX_DEPTH
The maximum depth generated. Maximum allowed is 20 until optimization.

##### OBJ_CHANCE
The percent chance for a generated value to be an obj instead of a literal.
    
## Default Generation
Generates objects with string, integer, float, and null values, with a max depth of 5.

### Example
What does the default JSONonsense look like you might ask? Feast your eyes upon it's beauty.

```    
{
    "WnBXizwzKS": {
        "iJDJrgTWjl": {
            "NjDOGrOHXX": "DgreyFAhod",
            "RiFSblYCwJ": {
                "ScnQvjCTkY": {
                    "DaDaYnUIPg": 41.2,
                    "XRyLtyeMoE": "ficcZrgKpH",
                    "YBNTqxWkSs": 123
                },
                "YZdewaWCrP": {
                    "HhKvNyBqVe": "rKYaBLnqlT",
                    "HurHjcRDiZ": 63.7,
                    "OhvfrvKdXj": "hsseuJYiCq",
                    "hXhudRZlUZ": {
                        "BpITjFJzUB": "KYFGZaLFSd",
                        "YerphUSfSa": {
                            "flHcPGEsyE": null,
                            "jrTOadjlAy": 6756
                        },
                        "hpYCdRKsnT": 18.89,
                        "hzjSPKVnca": "jHNbyajITf"
                    },
                    "oVZHdbjtqt": 89.246
                },
                "ezrJvTRJNo": 55.7773
            },
            "SSrnSfdNeI": 97.3622,
            "TfYZioIzoF": {
                "dJWqEPuEcu": {
                    "KBNyVXVHcr": 73.512,
                    "siqmqWKPxx": {
                        "MGHyWbwGte": "lySUGHhYWQ",
                        "hJNgJxFKSU": {
                            "cUJgiLKvrA": 4411,
                            "erTrnORuVm": 8619,
                            "pGqVnCwLbR": "UekNyktRQd",
                            "vZthcQgKjx": null
                        },
                        "jqPxKvhKVO": 4409
                    },
                    "vDdVJvdFAE": 7462,
                    "xrqWLFVXCD": 5.3,
                    "ziXVzyFyRG": 84
                },
                "ueVowJXVgv": 8552,
                "ujCuQFWuBE": 8585
            },
            "YeHrqoBlUe": 68.7,
            "nigVuoFanz": "baKcWcFUDc"
        },
        "kULRnblDnN": {
            "DODVAiptJL": {
                "GdaPdLxBaW": {
                    "RZJYYlPCow": {
                        "aZkERBjWcA": {
                            "agBaFgtusn": null,
                            "foOdontQoU": 38.867,
                            "iXmpKMaCQd": "jrnBFpHDet",
                            "yyFUesaSVF": 82.1007
                        },
                        "cGpTZNNKJG": "qbBlyKKtXN",
                        "caDgVHsBUG": 4713,
                        "ljYGaVSEum": 82.7174,
                        "qGSqlPoGwD": 15.02
                    },
                    "cbgZfMHUiO": 2697,
                    "iaFCFakAGX": 7444,
                    "jCjgdVemxY": "mgniwpybMw"
                },
                "PfGnGqtoEj": 2977,
                "eXCtJsXgvL": 73.663,
                "fRACJTtYuB": "AhRBWSpNNs",
                "jySWlCtPFI": 47.4,
                "zVoQJesYxs": {
                    "TlxuRhNHkc": {
                        "YZPHQApPNY": 33.3,
                        "cEmGhlaYiQ": {
                            "EIBZgaRLUy": 8323,
                            "cyjhofRqBX": null,
                            "llUzrpwXFz": "ZzhormDhWg"
                        },
                        "ddgAKhosUL": {
                            "HMEEIJKbik": 6647,
                            "IqcHQYCwvo": "auUhwmmUrn",
                            "cqWeciVpqo": null,
                            "kRJhzexHAT": null,
                            "vKXQCifQek": 20.108,
                            "zIpbUljvwi": "ljqiLhVxJe"
                        },
                        "msgSEaJCGd": 18.4543,
                        "pmVaGORPGp": 749,
                        "xBZIHdKNEa": "cxdyXhWbzQ"
                    },
                    "lzSxWwyPPX": "BniYctVWkl"
                }
            },
            "VjhRUXQmIq": 98.84,
            "lFGVFpAjtQ": "zpKeAFXhLT",
            "pcFxwFDwZa": {
                "GjZrXcnxLg": {
                    "LRsCqtiYfx": 77.98,
                    "NbZOngnztj": 8.1962,
                    "bEFZpOQOPz": {
                        "SBfempcpwm": 3254,
                        "bNlScdvYPw": {
                            "XMNwsVftXk": 9233,
                            "tzUrMIBMaR": null,
                            "udqducTQWj": "amBJpDrrVV"
                        },
                        "dKLkmXZMmY": 62.045,
                        "kfAZPQFzMH": 78.63
                    }
                },
                "KXYLaJEQWH": 1415,
                "ayHpMOfHmG": "NTPiGQXWnQ"
            },
            "sCXKmdzsef": 78.6636,
            "srhmvHslmq": 1773
        }
    },
    "dNKStVMWuv": "hKEvjuQgXl",
    "fikAopYCfM": 66.6184,
    "jcejdkBxTk": "UtvOSbpFfe"
}
```

Mmmm... what a <strong>*beaut*</strong>.
