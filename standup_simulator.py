#!/usr/bin/env python3
"""
Standup Simulator: The Pre-Meeting Rehearsal
Because pretending to be productive is half the job.
"""

import random
import datetime
from typing import List, Dict

# Because who actually remembers what they did yesterday?
YESTERDAY_ACTIVITIES = [
    "Refactored some legacy code (read: stared at screen)",
    "Investigated a bug (it was a typo)",
    "Updated documentation (added a TODO comment)",
    "Pair programmed (watched someone else code)",
    "Optimized performance (removed one print statement)",
    "Reviewed PRs (scrolled through diffs)",
    "Set up development environment (googled error messages)",
    "Wrote tests (copied from Stack Overflow)"
]

# The art of sounding blocked without causing panic
BLOCKERS = [
    "Waiting on API documentation that may or may not exist",
    "Environment issue - works on my machine™",
    "Need clarification on requirements (they keep changing)",
    "Dependency version conflict (npm/yarn/pip said no)",
    "Meeting with stakeholders (they cancelled)",
    "Researching best practices (reading Reddit)",
    "CI/CD pipeline is broken (again)",
    "Need access to a service (sent 3 emails, no response)"
]

# Today's ambitious plans that will become tomorrow's 'yesterday activities'
TODAY_PLANS = [
    "Continue working on current task (whatever that is)",
    "Fix that bug from yesterday (the new one I just created)",
    "Write more tests (to reach coverage metrics)",
    "Update the README (add more TODOs)",
    "Refactor the refactor (infinite loop)",
    "Investigate performance issues (add more logging)",
    "Prepare for demo (panic)",
    "Learn new framework (watch YouTube tutorials)"
]


def generate_standup_report() -> Dict[str, List[str]]:
    """Generate a perfectly mediocre standup report."""
    
    # Random but believable selection
    yesterday = random.sample(YESTERDAY_ACTIVITIES, random.randint(1, 3))
    today = random.sample(TODAY_PLANS, random.randint(1, 2))
    
    # 30% chance of having a blocker - just enough to seem engaged
    blockers = []
    if random.random() < 0.3:
        blockers = random.sample(BLOCKERS, 1)
    
    return {
        "yesterday": yesterday,
        "today": today,
        "blockers": blockers
    }


def main():
    """The main event - your daily dose of standup preparation."""
    print("\n=== STANDUP SIMULATOR ===")
    print(f"Date: {datetime.date.today()}\n")
    
    report = generate_standup_report()
    
    print("Yesterday I:")
    for item in report["yesterday"]:
        print(f"  • {item}")
    
    print("\nToday I will:")
    for item in report["today"]:
        print(f"  • {item}")
    
    if report["blockers"]:
        print("\nBlockers:")
        for blocker in report["blockers"]:
            print(f"  • {blocker}")
    else:
        print("\nNo blockers! (probably lying)")
    
    print("\nGood luck in the actual meeting! 🎭\n")


if __name__ == "__main__":
    main()
