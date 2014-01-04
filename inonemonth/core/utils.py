def get_github_branch_url(github_account_name, repo_name, branch_name):
    """
    >>> get_github_branch_url("RobrechtDR", "clac", "challenge2")
    'https://github.com/RobrechtDR/clac/tree/challenge2'
    """
    return "https://github.com/{0}/{1}/tree/{2}".format(github_account_name,
                                                        repo_name,
                                                        branch_name)


def get_branch_last_commit(github_account_name, repo_name, branch_name):
    """
    >>> get_branch_last_commit("RobrechtDR", "clac", "challenge2")
    'e0227880aaa548022f670576ee4408144d515f0c'

    Purely by using a webparser such as beatifulsoup or better: use a public api call.
    """
    pass


def get_github_commit_comparison_url(github_account_name, repo_name, start_commit, end_commit):
    """
    # Use inonemonth account to create test repo
    >>> get_github_commit_comparison_url("RobrechtDR", "clac", "f7860ff8fc",
    ...                                  "5035bd5dbf")
    'https://github.com/RobrechtDR/clac/compare/f7860ff8fc...5035bd5dbf'

    Comparison between 2 commit states:
    https://github.com/github/linguist/compare/96d29b7662f148842486d46117786ccb7fcc8018...a20631af040b4901b7341839d9e76e31994adda3

    Comparison between time states: (e.g. 1 month)
    https://github.com/github/linguist/compare/master@{1month}...master
    """
    return "https://github.com/{0}/{1}/compare/{2}...{3}".format(github_account_name,
                                                                 repo_name,
                                                                 start_commit,
                                                                 end_commit)





'''
1. On challenge/create/ call get_branch_last_commit and save this to Branch.start_commit.
(in Challenge: branch = OneToOneField(Branch)).
2. On challenge period end (using celery)(but also at the end of each day during challenge period so jurors can see progress),
 call get_branch_last_commit again and save to Branch.end_commit.
3. Use get_github_comparison_url in challenge/detail/1/ view to generate comparison url to see current state of challenge.
'''


if __name__ == "__main__":
    import doctest
    doctest.testmod()
