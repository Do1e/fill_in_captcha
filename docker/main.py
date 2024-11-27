import base64
import os
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import PlainTextResponse
import uvicorn
from captchaOCR import CaptchaOCR

ocr = CaptchaOCR()
app = FastAPI(debug=False, docs_url=None, redoc_url=None)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/")
async def readcaptcha(request: Request) -> Response:
    try:
        image = dict(await request.form())["captcha"]
        image = base64.b64decode(image)
        return PlainTextResponse(ocr.get_text(image))
    except KeyError as e:
        return Response(status_code=400, content=str(e))
    except Exception as e:
        return Response(status_code=500, content=str(e))


@app.get("/")
async def index() -> Response:
    return PlainTextResponse("Post your captcha image to this url.")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port, reload=False)
