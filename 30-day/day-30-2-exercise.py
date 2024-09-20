facebook_post = [
    {"likes": 21, "comments": 2},
    {"likes": 2, "comments": 2, "shares": 2},
    {"likes": 33, "comments": 8, "shares": 3},
    {"comments": 4, "shares": 2},
    {"comments": 1, "shares": 1},
    {"likes": 19, "comments": 3},
]

total_likes = 0

for post in facebook_post:
    try:
        total_likes += post["likes"]
    except KeyError:
        pass

print(total_likes)
