from fastapi import FastAPI,Form,UploadFile,File
from backend.src.extractor import extract
import uvicorn
import uuid
import os

app = FastAPI()

@app.post("/extract_from_doc")
def extract_from_doc(
    file_format: str = Form(),
    file: UploadFile = File()
):
    contents = file.file.read()
    file_path = r"C:\Users\manik\OneDrive\Documents\S\Ps\Medical_Data_Extraction_Project\backend\uploads"+str(uuid.uuid4())+".pdf"
    with open(file_path,"wb") as f:
        f.write(contents)
    try:
        data = extract(file_path,file_format)
    except Exception as e:
        date ={
            'error':str(e)
        }
    if os.path.exists(file_path):
        os.remove(file_path)

    return data


if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)

