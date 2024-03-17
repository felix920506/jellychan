import github
import os

ISSUE_PREFIX = '[Issue]: ' # The space is intentional

# Read token
TOKEN = os.getenv("GH_TOKEN")
auth = github.Auth.Token(TOKEN)
gh = github.Github(auth=auth)

# Get input
ISSUE = int(os.getenv("ISSUE"))
REPO = os.getenv("GH_REPO")
COMMENT = int(os.getenv("COMMENT_ID"))

repo = gh.get_repo(REPO)
issue = repo.get_issue(ISSUE)
comment = issue.get_comment(COMMENT)

# Comment Format
# @<bot account> rename <name>

command_prefix = f'@{gh.get_user().login} rename'

if comment.body.startswith(command_prefix):
    new_name = comment.body[len(command_prefix)+1:].strip()
    if new_name:
        if not new_name.startswith(ISSUE_PREFIX):
            new_name = ISSUE_PREFIX + new_name
        issue.edit(title=new_name)

