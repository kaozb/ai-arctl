import json
import requests

import os

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76"
}
output_file = '../frontend/src/data/articles.json'

urlpath =os.getenv('GITHUB_REPOSITORY')



def get_loacl_number():
    loaclsnumbers = []
    with open(output_file, 'r', encoding='utf-8') as f:
        x = f.read()
        all_arctl = json.loads(x)
        for issue in all_arctl:
            loaclsnumbers.append(issue.get("id"))
    return loaclsnumbers,all_arctl

def geturl():
    loaclsnumbers,all_arctls = get_loacl_number()
    params = {
        "state": "open",
        "per_page": 20,
        "sort": "updated-desc",
        "direction": "desc"
    }
    response = requests.get(f"https://api.github.com/repos/{urlpath}/issues",params=params)
    issues = response.json()
    add_arctl = []
    for issue in issues:
        number = issue.get("number")
        article = {
            "id": number,
            "title": issue["title"],
            "content": issue["body"],
            "created_at": issue["created_at"],
            "updated_at": issue["updated_at"],
            "labels": [label["name"] for label in issue["labels"]],
            "url": issue["html_url"]
        }
        if number in loaclsnumbers:
            all_arctls[loaclsnumbers.index(number)] = article
        else:
            add_arctl.append(article)
    all_arctls+=add_arctl
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(sorted(all_arctls, key=lambda x: x["updated_at"], reverse=True), f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    urlxx = geturl()
