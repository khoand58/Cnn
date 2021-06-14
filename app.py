import uvicorn
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.get("/files/")
async def test():
    return {"file_size": "test_khoa"}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}


if __name__ == "__app__":
    uvicorn.run(app, host="35.35.35.10", port=8098)
