import praw

keywords = ["real madrid","ramos","marcelo","varane","bale","vinicius","brahim","courtois","navas","carvajal","decima","isco","ascensio","modric","kroos","zidane","benzema","raul","odegaard","vallejo"]


def main():
    global reddit

    reddit = praw.Reddit(client_id='8XQLqSIAIT6l3Q',
        client_secret='DcmsrFlVoF94vW2eDFj-3yM1P1E',
        user_agent='socbot',
        username='soc-bot-RM-news',
        password='nimbus2000',
    )

    subreddit = reddit.subreddit('soccer')
    
   
    for submission in subreddit.new(limit=20):
        process_submission(submission)

def process_submission(submission): 
    
    normalized_title = submission.title.lower()
    for word in keywords:
        if word in normalized_title:
            print(submission.title)
            a=submission.title
            b=submission.url
            reddit.redditor('irksomehails').message(a[:98],b)
            break
        

if __name__ == "__main__":
    main()
