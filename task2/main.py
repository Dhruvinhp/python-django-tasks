from datetime import datetime, timedelta, timezone
from pytz import timezone as tz
from collections import defaultdict
from teams import meeting_request


def is_available(member_calendar, start_time, end_time):
    """Checks if a member is available for a given time slot."""
    for meeting in member_calendar:
        if start_time.astimezone(timezone.utc) < meeting["end_time"].astimezone(
            timezone.utc
        ) and end_time.astimezone(timezone.utc) > meeting["start_time"].astimezone(
            timezone.utc
        ):
            return False
    return True


def find_common_availability(team_calendars, duration):
    """Finds common availability across team members considering time zones."""
    availability = defaultdict(list)
    current_time = datetime.now(timezone.utc)

    for member_name, calendar_list in team_calendars.items():
        for calendar in calendar_list:
            member_timezone = tz(calendar.get("timezone"))
            for day in calendar["days"]:
                if day["start_time"].astimezone(member_timezone) < current_time:
                    continue
                start_time = day["start_time"]
                end_time = day["end_time"]
                start_time_utc = start_time.astimezone(timezone.utc)
                end_time_utc = end_time.astimezone(timezone.utc)
                for i in range(
                    (end_time_utc - start_time_utc).seconds // 60 // duration
                ):
                    local_start_time = (
                        start_time_utc + timedelta(minutes=i * duration)
                    ).astimezone(member_timezone)
                    local_end_time = local_start_time + timedelta(minutes=duration)
                    if is_available(
                        calendar["meetings"], local_start_time, local_end_time
                    ):
                        availability[member_timezone].append(local_start_time)

    common_availability = []
    for _, slots in availability.items():
        for slot in slots:
            if all(
                slot not in other_slots
                for other_slots in availability.values()
                if other_slots != slots
            ):
                common_availability.append(slot)

    return common_availability


def schedule_meeting(meeting_request):
    """Schedules a meeting for a list of teams, considering constraints and time zones."""
    teams = meeting_request["teams"]
    duration = meeting_request["duration"]

    team_calendars = {}
    for team in teams:
        for member in team["members"]:
            calendar = member["calendar"]
            if isinstance(calendar, dict):
                team_calendars.setdefault(member["name"], []).append(member["calendar"])
            else:
                raise ValueError("Invalid calendar format")

    common_availability = find_common_availability(team_calendars, duration)
    if common_availability:
        return common_availability[0]
    else:
        return "No suitable time slot found for the meeting."


meeting_request = meeting_request()
start_time = schedule_meeting(meeting_request)
if isinstance(start_time, datetime):
    print(f"Meeting can be scheduled at {start_time}")
else:
    print(start_time)
