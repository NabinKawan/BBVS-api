import os
from fastapi import APIRouter, UploadFile, HTTPException, Depends
from app.auth.jwt_bearer import JWTBearer
from app.settings import api_settings
import secrets

router = APIRouter(prefix='/api/file',
                   tags=['File'], dependencies=[Depends(JWTBearer())])


@router.post('/uploadImage')
async def upload_image(file: UploadFile):
    filename = file.filename
    extension = filename.split('.')[1]
    token_name = f"{secrets.token_hex(10)}.{extension}"
    FILEPATH = f"static/images/{token_name}"

    if extension not in ['png', 'jpg', 'jpeg']:
        raise HTTPException(
            status_code=400, detail="Extension not supported")
    else:
        # reading file content
        # coroutine returns promise
        file_content = await file.read()

        # saving the file
        with open(FILEPATH, 'wb') as filePointer:
            filePointer.write(file_content)
        file.close()
        url = f"{FILEPATH}"
        print(url)
        return url
