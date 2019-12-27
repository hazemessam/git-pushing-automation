import os
import sys


def ck_where_to_push(auto):
    global repo, branch
    if auto.lower() == 'n':
        repo = input('repo: ')
        branch = input('branch: ')

def ck_args():
    if len(sys.argv) == 2:
        if sys.argv[1] == '-r':
            auto = input('Pushing to origin/master? (y or n): ')
            ck_where_to_push(auto)

repo = 'origin'
branch = 'master'

commit_msg = input('commit msg: ')

print('Staging...')
os.system('git add .')
os.system('git status')

print('Committing...')
os.system(f'git commit -m "{commit_msg}"')

ck_args()

print('\nPushing...')
os.system(f'git push {repo} {branch}')
print('All done')