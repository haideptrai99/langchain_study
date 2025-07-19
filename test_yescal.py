import http.client
import json

conn = http.client.HTTPSConnection("api.yescale.io")
payload = json.dumps(
    {
        "model": "gemini-2.0-flash",
        "messages": [{"role": "user", "content": "Say hi!"}],
    }
)
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer sk-84D6rZqyq7Ck4K4T4Zlo5oV8848jXtWacB8kAHtEAt2Pp3zI",
    "Content-Type": "application/json",
}
conn.request("POST", "/v1/chat/completions", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
