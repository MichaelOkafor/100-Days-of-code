facebook_posts = [
    {"likes": 21, "comments": 2},
    {"likes": 13, "comments": 2, "shares": 1},
    {"likes": 33, "comments": 8, "shares": 3},
    {"comments": 4, "shares": 2},
    {"comments": 1, "shares": 1},
    {"likes": 19, "shares": 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post["likes"]
    except KeyError:
        total_likes += 0  # Or you can also use pass

print(total_likes)
