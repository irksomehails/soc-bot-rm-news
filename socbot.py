import praw

keywords = ["manchester", "chelsea","arsenal","psg"]

def main():
    reddit = praw.Reddit(client_id='8XQLqSIAIT6l3Q',
        client_secret='DcmsrFlVoF94vW2eDFj-3yM1P1E',
        user_agent='socbot',
        username='soc-bot-RM-news',
        password='nimbus2000',
    )
                     


    subreddit = reddit.subreddit('soccer')
    for submission in subreddit.stream.submissions():
        process_submission(submission)

def process_submission(submission): 

    normalized_title = submission.title.lower()
    for word in keywords:
        if word in normalized_title:
             print(submission.title)
             break
        
if __name__ == "__main__":
    main()
