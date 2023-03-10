import requests
import json

url = "https://api.github.com/user/repos"

payload = json.dumps({
  "name": "github_api_testing",
  "description": "Testing repo",
  "homepage": "https://github.com",
  "private": False,
  "is_template": True
})
headers = {
  'Accept': 'application/vnd.github+json',
  'X-GitHub-Api-Version': '2022-11-28',
  'Authorization': 'Bearer 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',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
