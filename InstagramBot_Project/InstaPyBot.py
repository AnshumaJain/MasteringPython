from instapy import InstaPy
import random

my_comments = [
    "So cool :grinning_face_with_big_eyes:",
    "Superb :grinning_face_with_big_eyes:",
    "Wow",
    "Cool!",
    "Nice! :thumbsup:",
    "Sweet! :grinning_face_with_big_eyes:",
    "Beautiful!",
    "awesome :heartbeat:",
    "Beautiful :green_heart:",
    "Pretty :red_heart:",
    "greetings! :pray:",
    "Whoa :fire:",
]

my_tags = [
    "namaste",
    "headstand",
    "handstand",
    "crowpose",
    "bakasana",
    "acro",
    "yoga",
    "acroyogalife",
    "acrocouple"
    "wheelpose",
    "chakrasana",
    "yogapose",
    "coupleworkout",
    "acroyoga",
    "bodyweighttraining",
    "streetworkout",
    "traveling",
    "travelinggram",
    "travelingcouple",
    "acroduo",
    "lsit",
    "pullup",
    "gymnastics",
    "crossfit",
    "planche",
    "calisthenicsworkout",
]

f = open("./account.txt", "r")
lines = f.readlines()
username = lines[0]
password = lines[1]
f.close()

session = InstaPy(username, password)
session.login()
# session.set_user_interact(amount=5, randomize=True, percentage=100, media='Photo')

session.set_comments(my_comments)
session.set_do_follow(enabled=True, percentage=5)  # follow a subset of the browsed posts
# session.set_dont_like(["naked", "nsfw"])
session.set_do_like(enabled=True, percentage=90)  # like a subset of the browsed posts
session.set_do_comment(enabled=True, percentage=90)  # comment on a subset of the browsed posts

# session.interact_user_followers(['acroyoga'], amount=25, randomize=True)
session.like_by_tags(random.choices(my_tags, k=10), amount=90)  # go thru 'k' random tags and do 'amount' likes each

session.end()
