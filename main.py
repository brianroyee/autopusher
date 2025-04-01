import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

repo_directory = os.getenv('repo_directory')
git_remote = os.getenv('git_remote')
git_branch = os.getenv('git_branch')
current_time = datetime.now().strftime('%A, %B %d, %Y at %I:%M %p')

html_content = f"""
<htmL
<body>
    <div">
        <h1>Hello World!</h1>
        <p>Brother, this push happened on <span class="time">{current_time}"</span></p>
        <p>Keep that streak going! 💪</p>
    </div>

    <div>
        <h1>Ninte thantha alla ente thantha</h1>
    </div>
</body>
</html>
"""


with open(os.path.join(repo_directory, "hello.html"), "w") as f:
        f.write(html_content)

os.chdir(repo_directory)
os.system("git add hello.html")
os.system(f'git commit -m "Daily commit: {datetime.now().strftime("%Y-%m-%d")}"')
os.system(f"git push {git_remote} {git_branch}")

