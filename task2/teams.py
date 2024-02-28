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
                                        year=2024, month=3, day=30, hour=9, minute=0
                                    ),
                                    "end_time": datetime(
                                        year=2024, month=3, day=30, hour=17, minute=0
                                    ),
                                },
                            ],
                            "meetings": [
                                {
                                    "start_time": datetime(
                                        year=2024, month=2, day=28, hour=10, minute=0
                                    ),
                                    "end_time": datetime(
                                        year=2024, month=2, day=28, hour=11, minute=0
                                    ),
                                },
                                {
                                    "start_time": datetime(
                                        year=2024, month=2, day=29, hour=1, minute=0
                                    ),
                                    "end_time": datetime(
                                        year=2024, month=2, day=29, hour=23, minute=0
                                    ),
                                },
                                {
                                    "start_time": datetime(
                                        year=2024, month=3, day=1, hour=10, minute=0
                                    ),
                                    "end_time": datetime(
                                        year=2024, month=3, day=1, hour=11, minute=0
                                    ),
                                },
                                {
                                    "start_time": datetime(
                                        year=2024, month=3, day=2, hour=10, minute=0
                                    ),
                                    "end_time": datetime(
                                        year=2024, month=3, day=2, hour=11, minute=0
                                    ),
                                },
                                {
                                    "start_time": datetime(
                                        year=2024, month=3, day=3, hour=10, minute=0
                                    ),
                                    "end_time": datetime(
                                        year=2024, month=3, day=3, hour=11, minute=0
                                    ),
                                },
                                {
                                    "start_time": datetime(
                                        year=2024, month=3, day=4, hour=10, minute=0
                                    ),
                                    "end_time": datetime(
                                        year=2024, month=3, day=4, hour=11, minute=0
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
