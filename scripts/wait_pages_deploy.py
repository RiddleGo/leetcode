#!/usr/bin/env python3
import subprocess, json, urllib.request, time

proc = subprocess.run(
    ["git", "credential", "fill"],
    input="protocol=https\nhost=github.com\n\n",
    capture_output=True,
    text=True,
    check=True,
)
token = dict(line.split("=", 1) for line in proc.stdout.splitlines() if "=" in line)["password"]
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json",
    "Content-Type": "application/json",
}
urllib.request.urlopen(
    urllib.request.Request(
        "https://api.github.com/repos/RiddleGo/leetcode/pages",
        data=json.dumps({"build_type": "workflow"}).encode(),
        headers=headers,
        method="PUT",
    )
)
for i in range(24):
    runs = json.loads(
        urllib.request.urlopen(
            urllib.request.Request(
                "https://api.github.com/repos/RiddleGo/leetcode/actions/runs?per_page=1",
                headers=headers,
            )
        ).read()
    )
    if runs["workflow_runs"]:
        r = runs["workflow_runs"][0]
        print(f"{i+1}: {r['name']} {r['status']} {r.get('conclusion')}")
        if r["status"] == "completed":
            break
    else:
        print(f"{i+1}: no runs yet")
    time.sleep(10)

pages = json.loads(
    urllib.request.urlopen(
        urllib.request.Request(
            "https://api.github.com/repos/RiddleGo/leetcode/pages", headers=headers
        )
    ).read()
)
print("pages:", pages.get("status"), pages.get("html_url"))
