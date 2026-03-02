from django.core.management.base import BaseCommand
from pymongo import MongoClient

USERS = [
    {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
    {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
    {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
    {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
    {"name": "Spider-Man", "email": "spiderman@marvel.com", "team": "Marvel"},
    {"name": "Captain Marvel", "email": "captainmarvel@marvel.com", "team": "Marvel"},
]

TEAMS = [
    {"name": "Marvel"},
    {"name": "DC"},
]

ACTIVITIES = [
    {"user_email": "superman@dc.com", "activity": "Flying", "duration": 120},
    {"user_email": "batman@dc.com", "activity": "Martial Arts", "duration": 90},
    {"user_email": "ironman@marvel.com", "activity": "Flight Suit Training", "duration": 60},
]

LEADERBOARD = [
    {"user_email": "superman@dc.com", "points": 1000},
    {"user_email": "ironman@marvel.com", "points": 950},
]

WORKOUTS = [
    {"name": "Strength Training", "suggested_for": "DC"},
    {"name": "Agility Drills", "suggested_for": "Marvel"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)

        db.users.create_index([("email", 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))