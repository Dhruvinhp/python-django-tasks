from datetime import datetime


def meeting_request():
    return {
        "teams": [
            {
                "members": [
                    {
                        "name": "John",
                        "calendar": {
                            "timezone": "America/Los_Angeles",
                            "days": [
                                {
                                    "start_time": datetime(
                                        year=2024, month=3, day=1, hour=9, minute=0
                                    ),
                                    "end_time": datetime(
                                        year=2024, month=3, day=1, hour=17, minute=0
                                    ),
                                },
                            ],
                            "meetings": [
                                {
                                    "start_time": datetime(
                                        year=2024, month=3, day=1, hour=10, minute=0
                                    ),
                                    "end_time": datetime(
                                        year=2024, month=3, day=1, hour=11, minute=0
                                    ),
                                },
                            ],
                        },
                    },
                ]
            },
        ],
        "duration": 30,
    }
