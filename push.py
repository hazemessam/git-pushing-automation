import os
import sys


def ck_where_to_push(auto):
    global repo, branch
    if auto.lower() == 'n':
        repo = input('repo: ')
        branch = input('branch: ')

def ck_args():
    if len(sys.argv) > 1:
        if sys.argv[1] == '-h':
            print('Usgae:\n\tpush to origin/master: push\n\tpush to remote/branch: push [-r]')
            sys.exit()
        elif sys.argv[1] == '-r':
            auto = input('Pushing to origin/master? (y or n): ')
            ck_where_to_push(auto)


repo = 'origin'
branch = 'master'

ck_args()
commit_msg = input('commit msg: ')

print('Staging...')
os.system('git add .')
os.system('git status')

print('Committing...')
os.system(f'git commit -m "{commit_msg}"')

print('\nPushing...')
os.system(f'git push {repo} {branch}')
print('All done')