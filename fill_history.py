import os
import random
from datetime import datetime, timedelta

# --- CONFIGURATION ---
DAYS_BACK = 265  # How many days to go back
GH_EMAIL = "2020e159@eng.jfn.ac.lk"
GH_NAME = "Tharusha Sachinthana"
# ---------------------

def make_commit(date_str):
    with open("log.txt", "a") as f:
        f.write(f"Contribution on {date_str}\n")
    
    os.system(f'git add log.txt')
    # This command sets the "Time" for the commit
    os.environ['GIT_AUTHOR_DATE'] = date_str
    os.environ['GIT_COMMITTER_DATE'] = date_str
    os.system(f'git commit -m "Update project logs and documentation"')

# Set identity
os.system(f'git config user.email "{GH_EMAIL}"')
os.system(f'git config user.name "{GH_NAME}"')

start_date = datetime.now() - timedelta(days=DAYS_BACK)

for i in range(DAYS_BACK + 1):
    current_date = start_date + timedelta(days=i)
    
    # Skip some days (e.g., 15% chance to skip) to make it look realistic
    if random.random() < 0.15:
        continue
        
    # On "work" days, commit 1 to 5 times (creates different shades of green)
    num_commits = random.randint(1, 5)
    for _ in range(num_commits):
        # Randomize the hour/minute so it's not the same time every day
        hour = random.randint(9, 22)
        minute = random.randint(10, 59)
        formatted_date = current_date.replace(hour=hour, minute=minute).strftime('%Y-%m-%d %H:%M:%S')
        
        make_commit(formatted_date)

print("--- FINISHED: All commits created locally! ---")
