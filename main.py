import os
from datetime import datetime

repo_directory = "/home/teknikal/Desktop/orbital simulator/autopush/"
git_remote = "origin"
git_branch = "main"

with open(os.path.join(repo_directory, "hello.html"), "w") as f:
        f.write(f"<html><body><h1>Hello World!</h1><p>{datetime.now().strftime('%Y-%m-%d')}</p></body></html>")

os.chdir(repo_directory)
os.system("git add hello.html")
os.system(f'git commit -m "Daily commit: {datetime.now().strftime("%Y-%m-%d")}"')
os.system(f"git push {git_remote} {git_branch}")

