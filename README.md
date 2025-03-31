# Automated Daily Git Pusher

A simple Python script that automatically creates a commit and pushes to GitHub every day when your computer starts.

## Features
- Creates a `hello.html` file with the current date
- Automatically commits and pushes changes to your repository
- Runs silently in the background on system startup

## Installation

### 1. Prerequisites
- Python 3 installed
- Git installed and configured
- GitHub repository set up with proper remote

### 2. Setup
1. Clone this repository or save the script to your desired location
2. Edit these variables in the script:
   ```python
   repo_directory = "/home/teknikal/Desktop/orbital simulator/autopush/"
   git_remote = "origin"
   git_branch = "main"

