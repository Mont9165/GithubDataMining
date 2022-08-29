# This is a sample Python script.
import json
import pprint

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import git

def get_diff(repo_path):
    repo = git.Repo(repo_path)
    print(git.Repo(repo_path))
    print(repo.iter_commits())
    commit_list = []
    j_w = open("test.json", "w")
    for commit_id in repo.iter_commits():
        commit_list.append(commit_id)
        repo.git.checkout(commit_id)
        hcommit = repo.head.commit
        json.dump(hcommit.stats.files, j_w, indent=4)
        json.dump(hcommit.stats.total, j_w, indent=4)
        pass
    repo.git.checkout(commit_list[0])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_diff('./naist_intern20220824')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
