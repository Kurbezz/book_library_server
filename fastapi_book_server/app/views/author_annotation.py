from fastapi import APIRouter, Depends, HTTPException, status

from fastapi_pagination import Params, Page
from fastapi_pagination.ext.ormar import paginate

from app.models import AuthorAnnotation as AuthorAnnotationDB
from app.serializers.author_annotation import AuthorAnnotation, CreateAuthorAnnotation, UpdateAuthorAnnotation


author_annotation_router = APIRouter(
    prefix="/api/v1/author_annotations",
    tags=["author_annotation"]
)


@author_annotation_router.get("/", response_model=Page[AuthorAnnotation], dependencies=[Depends(Params)])
async def get_author_annotations():
    return await paginate(
        AuthorAnnotationDB.objects
    )


@author_annotation_router.post("/", response_model=AuthorAnnotation)
async def create_author_annotation(data: CreateAuthorAnnotation):
    return await AuthorAnnotationDB.objects.create(
        **data.dict()
    )


@author_annotation_router.get("/{id}", response_model=AuthorAnnotation)
async def get_author_annotation(id: int):
    annotation = await AuthorAnnotationDB.objects.get_or_none(id=id)

    if annotation is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    return annotation


@author_annotation_router.put("/{id}", response_model=AuthorAnnotation)
async def update_author_annotation(id: int, data: UpdateAuthorAnnotation):
    annotation = await AuthorAnnotationDB.objects.get_or_none(id=id)

    if annotation is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    annotation.update_from_dict(data.dict())

    return await annotation.save()
