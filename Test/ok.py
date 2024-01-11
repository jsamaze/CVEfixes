from pydriller import Repository

repo_url="https://github.com/jcollie/asterisk.git"
hashes=['a8b180875b037b8da26f6a3bcc8e5e98b8c904d2', '60de4fbbdf3ede49f158e23a9e3b679f2e519c1e']
single_hash=None

repo = Repository(path_to_repo=repo_url,
                             only_commits=hashes,
                             single=single_hash,
                             num_workers=4).traverse_commits()

print (list(repo))

for commit in repo:
    print(f'Processing {commit.hash}')