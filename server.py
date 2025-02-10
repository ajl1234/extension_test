import httpx
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import StreamingResponse
import debugpy

app = FastAPI()

debugpy.listen(("0.0.0.0", 8888))

SYSTEM_MESSAGE = {
	"role": "system",
	"content": """Respond as though you have too much food in your mouth""",
}

def prepare_messages(user_messages: list) -> list:
	return user_messages + [SYSTEM_MESSAGE]

async def get_github_completion(messages: list, auth_token: str):
	async with httpx.AsyncClient() as client:
		response = await client.post(
			"https://api.githubcopilot.com/chat/completions",
			headers={
				"Authorization": f"Bearer {auth_token}",
				"Content-Type": "application/json",
			},
			json={
				"messages": prepare_messages(messages),
				"stream": True,
			},
			timeout=30.0,
		)

		return response
  

@app.post("/completion")
async def completion(request: Request):
	req = await request.json()
	auth_token = request.headers.get("x-github-token")
	messages = req.get("messages", [])
	
	if not auth_token:
		raise HTTPException(status_code=401, detail="Missing authentication token")
	
	response = await get_github_completion(messages, auth_token)
	
	return StreamingResponse(
		response.aiter_bytes(),
		media_type="text/event-stream",
		status_code=response.status_code,
	)
