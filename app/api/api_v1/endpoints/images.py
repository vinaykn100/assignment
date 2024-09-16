import boto3
import os, json, io
from fastapi import APIRouter, UploadFile, File, Response
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel
from uuid import uuid4
router = APIRouter()

class Image(BaseModel):
    id: int
    name: str
    size: int
    extension: str
    createdBy: str

session = boto3.session.Session()
images_bucket = os.environ.get('imagesBucket', 'images-bucket')

s3_client=session.client(
    service_name='s3',
    aws_access_key_id='S3RVER',
    aws_secret_access_key='S3RVER',
    endpoint_url='http://localhost:4569')



@router.get('/hello')
def home_page():
    return {
        'message': 'Hello, world!!'
    }


@router.post("/upload/{image_name}")
async def upload_image(image_name: str, file: UploadFile = File(...)):
    try:
        file.filename = f"{image_name}.jpg"
        contents = await file.read()

        response = s3_client.put_object(
            Bucket=images_bucket,
            Key=file.filename,
            Body=contents
        )

        return {
            'message': f'images uploaded successfully with name {file.filename}'
        }
    except Exception as e:
        print('Error:', e)
        return {
            "error": e
        }




@router.get("/list-images")
async def list_images():
    all_images=list()
    try:
        image_objects = s3_client.list_objects(Bucket=images_bucket)
        for image in image_objects.get('Contents', []):
            all_images.append(image)
        return {
            "images": all_images
        }
    except Exception as e:
        print('Error:', e)
        return {
            "error": e
        }

@router.get("/get-image/{image_name}")
async def get_image(image_name):
    try:
        image_object = s3_client.get_object(Bucket=images_bucket,Key=f"{image_name}.jpg")
        body = image_object["Body"].read()

        return Response(
            content=body,
            headers={
                'Content-Disposition': 'attachment; filename=f{image_name}.jpg'
            }
        )
    except Exception as e:
        print('Error:', e)
        return {
            "error": e
        }


@router.delete("/delete-image/{image_name}")
async def delete_image(image_name: str):
    try:
        s3_client.delete_object(Bucket=images_bucket,Key=f"{image_name}.jpg")
        return {
            "mesage": f"Deleted image:: {image_name}.jpg successfully"
        }
    except Exception as e:
        print('Error:', e)
        return {
            "error": e
        }