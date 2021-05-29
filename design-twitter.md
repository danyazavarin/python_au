# Design

+ [Design Twitter](#design-twitter)

## Design Twitter

https://leetcode.com/problems/design-twitter/

``` python
def __init__(self):
    """
    Initialize your data structure here.
    """
    self.users = {}
    self.followers = {}
    self.post = 0
    
def postTweet(self, userId, tweetId):
    """
    Compose a new tweet.
    :type userId: int
    :type tweetId: int
    :rtype: None
    """
    self.post += 1
    if userId in self.users:
        self.users[userId].append((tweetId, self.post))
    else: self.users[userId] = [(tweetId,self.post)]
    
def get_tweet(self,userId):
    tweets = []
    if userId in self.users:
        tweets += self.users[userId]
    if userId in self.followers:
        followees = self.followers[userId]
        for u_id in followees:
            if u_id in self.users:
                tweets += self.users[u_id]
    tweets = sorted(tweets, key = lambda posts: posts[1],reverse=True)
    return tweets[0:10]

def getNewsFeed(self, userId):
    """
    Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
    :type userId: int
    :rtype: List[int]
    """
    recent_Tweets = self.get_tweet(userId)
    return [post[0] for post in recent_Tweets] 

def follow(self, followerId, followeeId):
    """
    Follower follows a followee. If the operation is invalid, it should be a no-op.
    :type followerId: int
    :type followeeId: int
    :rtype: None
    """
    if followerId != followeeId:
        if followerId in self.followers :
            self.followers[followerId].add(followeeId)
        else: self.followers[followerId] = {followeeId}

def unfollow(self, followerId, followeeId):
    """
    Follower unfollows a followee. If the operation is invalid, it should be a no-op.
    :type followerId: int
    :type followeeId: int
    :rtype: None
    """
    if followerId in self.followers:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
```
