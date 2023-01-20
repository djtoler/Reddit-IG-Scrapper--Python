import requests
import praw

reddit = praw.Reddit(
    client_id='', 
    client_secret='', 
    user_agent=''
)

chiraqology = reddit.subreddit('chiraqology')
# chiraqology = reddit.subreddit('CrimeInTheD')
# chiraqology = reddit.subreddit('DaDumbWay')
# chiraqology = reddit.subreddit('Atlantology')
# chiraqology = reddit.subreddit('CaliBanging')

for submission in reddit.subreddit("chiraqology").new():
    print(submission.title)
    print(submission.id)
    print(submission.url)
    print(submission.score, "score")
    print(submission.num_comments)

# url = "https://www.reddit.com/r/Chiraqology/comments/10eq3gf/fbg_duck_full_murder_report/"
# submission = reddit.submission(url=url)

# submission.comments.replace_more(limit=None)
# for top_level_comment in submission.comments:
#     print(top_level_comment.body)

# print(chiraqology.description)