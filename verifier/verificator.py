import requests
import json


TOKEN = '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'
PREFIXES = ['GENERATOR', 'LEETCODE', 'HEXNUMBER','ITERATOR', 'TRIANGLE', 'REQUESTS']
GROUPS = ['1021','1022']
ACTION = ['Added','Deleted','Refactored','Fixed']


def prepare_headers():
    return {
      'Authorization': 'Token {}'.format(TOKEN),
      'Content-Type': "application/json"
      'Accept': "application/vnd.github.v3+json"
    }
    

def prepare_body(pull, comment):
    return {
        'body': f"{comment}",
        'path': requests.get(pull['url'] + '/files', headers=prepare_headers()).json()[0]['filename'],
        'position': 1,
        'commit_id': pull['head']['sha']
    }


def check_prefixes(title):
    comments = ''
    action = title.split()[1]
    group = title.split('-')[1].split()[0]
    prefix = title.split('-')[0]
    if not prefix in PREFIX:
        comments += "Prefix must be one of the following {}.\n".format(PREFIX)
    if not group in GROUP:
        comments += "Group must be one of the following {}. \n".format(GROUP)
    if not action in ACTION:
        comments += "Action must be on of the following {}. \n".format(ACTION)
    return comments


def get_all_user_prs(user_login, repo_name, pr_state): 
   pulls = requests.get('https://api.github.com/repos/{}/{}/pulls?state={}'.format(user_login, repo_name, pr_state), 
                         headers = prepare_headers())
   return pulls
   
   
def get_all_pr_commits(pr):
    all_pr_commits = requests.get(pr['commits_url'], headers=prepare_headers())
    return all_pr_commits


def send_pr_comment(pr, comment):
    response = requests.post(pr['url']+'/comments', 
                      headers = prepare_headers(), 
                      json = prepare_body(pr, comment))
    print(response.json())
    print(response.status_code)

    
def get_last_commit_date(pull):
    commitpage = requests.get(pull["commits_url"], headers = prepare_headers())  
    return commitpage.json()[-1]["commit"]["author"]["date"]


def get_last_comment_date(pull):
  comments = requests.get(pull["review_comments_url"], headers = prepare_headers())
  if len(comments.json()) > 0:
    return comments.json()[-1]["created_at"]
  return "0000-00-00T00:00:00Z"


def verify_pr(pr):
    comment = ''
    all_pr_commits = get_all_pr_commits(pr)
    last_commit_date = get_last_commit_date(pr)
    last_comment_date = get_last_comment_date(pr)
    if last_comment_date != "0000-00-00T00:00:00Z" and last_commit_date > last_comment_date:
      for commit in all_pr_commits:
        comment += check_prefixes(commit['message'])
      if len(comment) > 0:
        send_pr_comment(pr, '\n\n'.join(comment))  
        


def main ():
    user_login = 'danyazavarin'
    repos_name = 'python_au'
    pr_state = 'open'
    for pr in (get_all_user_prs(user_login, repos_name, pr_state)).json():
        verify_pr (pr)
        
        
