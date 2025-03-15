import httpx
import os
import asyncio

urlpath = os.getenv('GITHUB_REPOSITORY')


async def fetch_url_issues():
    params = {
        "state": "open",
        "per_page": 100,
        "sort": "updated-desc",
        "direction": "desc"
    }
    async with httpx.AsyncClient(timeout=30.0) as client:
        apiurl = f"https://api.github.com/repos/{urlpath}/issues"
        response = await client.get(apiurl, params=params)
        response.raise_for_status()
        issues = response.json()
        articles_titles = []
        for issue in issues:
            if issue["title"].strip().startswith('http'):
                number = issue["number"]
                title = issue["title"].strip()
                articles_titles.append((number, title))
        return articles_titles


def apiwithmarkdown(url):
    title, md_txt = '处理失败', url
    try:
        mdurl = f"https://r.jina.ai/{url}"
        headers = {"X-Return-Format": "markdown", }
        response = httpx.get(mdurl, headers=headers, timeout=30.0)
        response.raise_for_status()  # 检查状态码，如果不是 200 OK，则抛出异常
        md_txt = response.text
        title = md_txt.splitlines()[0]
    except Exception as e:
        print(e)
        title = url
    return title, md_txt


# 添加修改 issue 的函数
async def update_issue(issue_number, title, body):
    headers = {"Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}"}
    data = {"title": title, "body": body}
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            apiurl = f"https://api.github.com/repos/{urlpath}/issues/{issue_number}"
            response = await client.patch(apiurl, headers=headers, json=data)
            print(response.text)
    #        response.raise_for_status()
            print(f"添加成功 {title} ")
    except Exception as e:
        print(f"添加失败 {issue_number}: {e}")


async def main():
    """主函数"""
    print("查找http路径...")
    articles = await fetch_url_issues()
    if articles:
        for urlinfo in articles:
            title, md_txt = apiwithmarkdown(urlinfo[1])
            issue_number = urlinfo[0]
            await update_issue(issue_number, title, md_txt)
            print(f"更新{title}")
    else:
        print("没有http ,跳过")


if __name__ == "__main__":
    asyncio.run(main())
