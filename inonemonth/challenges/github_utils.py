import requests

###############################################################################
#                            Github api utilities                             #
###############################################################################

# http://developer.github.com/guides/getting-started/

API_ROOT_URL = "https://api.github.com"
SITE_ROOT_URL = "https://github.com"


# http://developer.github.com/v3/repos/#get
def get_api_repo_url(owner, repo):
    return "{0}/repos/{1}/{2}".format(API_ROOT_URL, owner, repo)


# http://developer.github.com/v3/repos/#list-user-repositories
def get_api_repos_url(owner):
    return "{0}/users/{1}/repos".format(API_ROOT_URL, owner, repo)


# http://developer.github.com/v3/repos/#list-branches
def get_api_repo_branches_url(owner, repo):
    return "{0}/repos/{1}/{2}/branches".format(API_ROOT_URL, owner, repo)


# http://developer.github.com/v3/repos/#get-branch
def get_api_repo_branch_url(owner, repo, branch):
    return "{0}/repos/{1}/{2}/branches/{3}".format(API_ROOT_URL, owner, repo, branch)


###############################################################################
#                       Other Github related utilities                        #
###############################################################################

def get_repo_and_branch_from_repo_path(repo_path):
    if "/" not in repo_path:
        return repo_path, "master"
    else:
        return tuple(repo_path.split("/", 1))


def get_main_branch_url(owner, repo, branch):
    return "{0}/{1}/{2}/tree/{3}".format(SITE_ROOT_URL, owner, repo, branch)


def get_last_commit_on_branch(owner, repo, branch):
    repo_branch_url = get_api_repo_branch_url(owner, repo, branch)
    req = requests.get(repo_branch_url)
    return req.json()["commit"]["sha"]


def get_commit_comparison_url(owner, repo, start_commit, end_commit):
    return "{0}/{1}/{2}/compare/{3}...{4}".format(SITE_ROOT_URL, owner,
                                                  repo, start_commit,
                                                  end_commit)


'''
1. On challenge/create/ call get_branch_last_commit and save this to Branch.start_commit.
(in Challenge: branch = OneToOneField(Branch)).
2. On challenge period end (using celery)(but also at the end of each day during challenge period so jurors can see progress),
 call get_branch_last_commit again and save to Branch.end_commit.
3. Use get_github_comparison_url in challenge/detail/1/ view to generate comparison url to see current state of challenge.
'''
