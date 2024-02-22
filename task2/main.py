import sqlite3
from datetime import datetime


class MeetingScheduler:
    def __init__(self):
        self.conn = sqlite3.connect("meeting_scheduler.db")
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS teams (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL
                        )"""
        )
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS members (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            team_id INTEGER,
                            FOREIGN KEY (team_id) REFERENCES teams(id)
                        )"""
        )
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS meetings (
                            id INTEGER PRIMARY KEY,
                            start_time TEXT NOT NULL,
                            duration_minutes INTEGER NOT NULL,
                            team_id INTEGER,
                            FOREIGN KEY (team_id) REFERENCES teams(id)
                        )"""
        )
        self.conn.commit()

    def add_team(self, team_name, members):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO teams (name) VALUES (?)", (team_name,))
        team_id = cursor.lastrowid
        for member_name in members:
            cursor.execute(
                "INSERT INTO members (name, team_id) VALUES (?, ?)",
                (member_name, team_id),
            )
        self.conn.commit()

    def get_teams(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM teams")
        return cursor.fetchone()[0]

    def get_team_members(self, team_name):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT members.name FROM members JOIN teams ON members.team_id = teams.id WHERE teams.name = ?",
            (team_name,),
        )
        return [row[0] for row in cursor.fetchall()]

    def schedule_meeting(self, start_time, duration_minutes, team_name):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO meetings (start_time, duration_minutes, team_id) VALUES (?, ?, (SELECT id FROM teams WHERE name = ?))",
            (start_time.strftime("%Y-%m-%d %H:%M"), duration_minutes, team_name),
        )
        self.conn.commit()

    def close(self):
        self.conn.close()


def get_user_datetime(prompt):
    while True:
        try:
            date_string = input(prompt)
            date = datetime.strptime(date_string, "%Y-%m-%d %H:%M")
            return date
        except ValueError:
            print(
                "Invalid date/time format. Please enter date/time in the format YYYY-MM-DD HH:MM."
            )


def main():
    scheduler = MeetingScheduler()

    print("Welcome to the Meeting Scheduler!")

    while True:
        add_team_option = input("Would you like to add a team? (yes/no): ").lower()
        if add_team_option == "yes":
            team_name = input("Enter team name: ")
            members = {}
            while True:
                member_name = input(
                    "Enter member name (or leave blank to finish adding members): "
                )
                if not member_name:
                    break
                members[member_name] = []
            scheduler.add_team(team_name, members)
        elif add_team_option == "no":
            if scheduler.get_teams():
                break
            else:
                print("No teams added. Please add at least one team.")
        else:
            print("Invalid option. Please enter 'yes' or 'no'.")

    while True:
        team_name = input("Enter the team involved in the meeting: ")
        if scheduler.get_team_members(team_name):
            break
        else:
            print("Team does not exist. Please enter a valid team name.")

    meeting_start = get_user_datetime(
        "Enter meeting start date and time (YYYY-MM-DD HH:MM): "
    )
    duration_minutes = int(input("Enter meeting duration in minutes: "))

    scheduler.schedule_meeting(meeting_start, duration_minutes, team_name)
    print("Meeting scheduled successfully.")

    scheduler.close()


if __name__ == "__main__":
    main()
