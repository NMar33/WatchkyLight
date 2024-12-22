import json
import os

# Файл для сохранения настроек
SETTINGS_FILE = "settings/settings.json"

# Дефолтные настройки
default_settings = {
    "device": {
        "SmartTV": {
            "initial_playback_delay_ms": {
                "good": 5_000,
                "average": 10_000,
                "bad": 60_000,
                "reverse": True
            },
            "rebuffer_count": {
                "good": 1,
                "average": 2,
                "bad": 3,
                "reverse": True
            },
            "average_bitrate_kbps": {
                "good": 4000,
                "average": 3000,
                "bad": 2000,
                "reverse": False
            }
        },
        "Desktop": {
            "initial_playback_delay_ms": {
                "good": 3_000,
                "average": 7_000,
                "bad": 20_000,
                "reverse": True
            },
            "rebuffer_count": {
                "good": 1,
                "average": 2,
                "bad": 3,
                "reverse": True
            },
            "average_bitrate_kbps": {
                "good": 4000,
                "average": 3000,
                "bad": 2000,
                "reverse": False
            }
        },
        "Mobile": {
            "initial_playback_delay_ms": {
                "good": 3_000,
                "average": 7_000,
                "bad": 20_000,
                "reverse": True
            },
            "rebuffer_count": {
                "good": 2,
                "average": 5,
                "bad": 8,
                "reverse": True
            },
            "average_bitrate_kbps": {
                "good": 1_500,
                "average": 1_000,
                "bad": 500,
                "reverse": False
            }
        },
        "Tablet": {
            "initial_playback_delay_ms": {
                "good": 3_000,
                "average": 7_000,
                "bad": 20_000,
                "reverse": True
            },
            "rebuffer_count": {
                "good": 1,
                "average": 2,
                "bad": 3,
                "reverse": True
            },
            "average_bitrate_kbps": {
                "good": 2_000,
                "average": 1_500,
                "bad": 1_000,
                "reverse": False
            }
        }
    },
    "duration": {
        "short": {
            "initial_playback_delay_ms": {
                "good": 2_000,
                "average": 3_000,
                "bad": 7_000,
                "reverse": True
            },
            "rebuffer_count": {
                "good": 2,
                "average": 3,
                "bad": 6,
                "reverse": True
            },
            "average_bitrate_kbps": {
                "good": 1900,
                "average": 1600,
                "bad": 1000,
                "reverse": False
            }
        },
        "medium": {
            "initial_playback_delay_ms": {
                "good": 3_000,
                "average": 7_000,
                "bad": 15_000,
                "reverse": True
            },
            "rebuffer_count": {
                "good": 1,
                "average": 3,
                "bad": 5,
                "reverse": True
            },
            "average_bitrate_kbps": {
                "good": 3000,
                "average": 2000,
                "bad": 1000,
                "reverse": False
            }
        },
        "long": {
            "initial_playback_delay_ms": {
                "good": 3_000,
                "average": 7_000,
                "bad": 20_000,
                "reverse": True
            },
            "rebuffer_count": {
                "good": 0,
                "average": 1,
                "bad": 2,
                "reverse": True
            },
            "average_bitrate_kbps": {
                "good": 4000,
                "average": 3000,
                "bad": 2000,
                "reverse": False
            }
        }
    }
}
# {
#     "device": {
#         "SmartTV": {
#             "initial_playback_delay_ms": {"good": 2000, "average": 4000, "bad": 6000},
#             "rebuffer_count": {"good": 1, "average": 2, "bad": 3},
#             "average_bitrate_kbps": {"good": 3000, "average": 2000, "bad": 1000}
#         },
#         "Desktop": {
#             "initial_playback_delay_ms": {"good": 1000, "average": 2000, "bad": 4000},
#             "rebuffer_count": {"good": 0, "average": 1, "bad": 2},
#             "average_bitrate_kbps": {"good": 4000, "average": 3000, "bad": 2000}
#         },
#         "Mobile": {
#             "initial_playback_delay_ms": {"good": 3000, "average": 5000, "bad": 7000},
#             "rebuffer_count": {"good": 2, "average": 5, "bad": 8},
#             "average_bitrate_kbps": {"good": 1500, "average": 1000, "bad": 500}
#         },
#         "Tablet": {
#             "initial_playback_delay_ms": {"good": 2500, "average": 4000, "bad": 6000},
#             "rebuffer_count": {"good": 1, "average": 2, "bad": 3},
#             "average_bitrate_kbps": {"good": 2000, "average": 1500, "bad": 1000}
#         },
#     },
#     "duration": {
#         "short": {
#             "initial_playback_delay_ms": {"good": 2500, "average": 4000, "bad": 6000},
#             "rebuffer_count": {"good": 1, "average": 2, "bad": 3},
#             "average_bitrate_kbps": {"good": 2000, "average": 1500, "bad": 1000}
#         },
#         "medium": {
#             "initial_playback_delay_ms": {"good": 2000, "average": 4000, "bad": 6000},
#             "rebuffer_count": {"good": 1, "average": 3, "bad": 5},
#             "average_bitrate_kbps": {"good": 3000, "average": 2000, "bad": 1000}
#         },
#         "long": {
#             "initial_playback_delay_ms": {"good": 1500, "average": 3000, "bad": 5000},
#             "rebuffer_count": {"good": 0, "average": 1, "bad": 2},
#             "average_bitrate_kbps": {"good": 4000, "average": 3000, "bad": 2000}
#         },
#     }
# }

# Функция загрузки настроек
def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    return default_settings

# Функция сохранения настроек
def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)

# Функция сброса настроек
def reset_settings():
    save_settings(default_settings)

# Генерация диапазонов для отображения в таблице
def format_ranges(thresholds, reverse=False):
    if reverse:
        return f"< {thresholds['good']}", f"{thresholds['good']}–{thresholds['average']}", f"{thresholds['average']}–{thresholds['bad']}", f"> {thresholds['bad']}"
    else:
        return f"> {thresholds['good']}", f"{thresholds['average']}–{thresholds['good']}", f"{thresholds['bad']}–{thresholds['average']}", f"< {thresholds['bad']}"
