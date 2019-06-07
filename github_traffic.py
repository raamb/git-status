from github import Github
from constant import REPO_TOPIC, GITHUB_TOKEN, GITHUB_ORG
from utils import report_slack
from datetime import datetime, timedelta


def _process_issues(repo, since_date):
    issue_string = ""
    issues = repo.get_issues(state="closed", since=since_date)
    for issue in issues:
        issue_string += str(repo.full_name) + " " + str(issue) + " " + str(issue.closed_at) + "\n"
    return issue_string


def _collect(token, since_date):
    gh = Github(token)
    repositories = gh.search_repositories(query='org:' + GITHUB_ORG)
    issue_string = "Issues fixed since " + str(since_date) + "\n```"
    issue_string += "\n"
    for repo in repositories:
        repo = gh.get_repo(repo.full_name)
        topics = repo.get_topics()
        if REPO_TOPIC in topics:
            issue_string += _process_issues(repo, since_date)
    issue_string += "```"
    return issue_string


def print_closed_issues():
    today = datetime.today()
    last_monday = today - timedelta(days=today.weekday())
    issue_string = _collect(GITHUB_TOKEN, last_monday)
    print(issue_string)
    report_slack(issue_string)


print_closed_issues()
