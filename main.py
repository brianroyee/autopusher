import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

repo_directory = os.getenv('repo_directory')
git_remote = os.getenv('git_remote')
git_branch = os.getenv('git_branch')

with open(os.path.join(repo_directory, "hello.html"), "w") as f:
        f.write(f"<html><body><h1>Hello World!</h1><p>{datetime.now().strftime('%Y-%m-%d')}</p></body></html>")

os.chdir(repo_directory)
os.system("git add hello.html")
os.system(f'git commit -m "Daily commit: {datetime.now().strftime("%Y-%m-%d")}"')
os.system(f"git push {git_remote} {git_branch}")

