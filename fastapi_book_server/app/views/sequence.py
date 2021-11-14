from fastapi import APIRouter, Depends

from fastapi_pagination import Params
from fastapi_pagination.ext.ormar import paginate
from app.utils.pagination import CustomPage

from app.models import Sequence as SequenceDB
from app.serializers.sequence import Sequence, CreateSequence
from app.services.sequence import SequenceTGRMSearchService


sequence_router = APIRouter(
    prefix="/api/v1/sequences",
    tags=["sequence"]
)


@sequence_router.get("/", response_model=CustomPage[Sequence], dependencies=[Depends(Params)])
async def get_sequences():
    return await paginate(
        SequenceDB.objects
    )


@sequence_router.get("/{id}", response_model=Sequence)
async def get_sequence(id: int):
    return await SequenceDB.objects.get(id=id)


@sequence_router.post("/", response_model=Sequence)
async def create_sequence(data: CreateSequence):
    return await SequenceDB.objects.create(
        **data.dict()
    )


@sequence_router.get("/search/{query}", response_model=CustomPage[Sequence], dependencies=[Depends(Params)])
async def search_sequences(query: str):
    return await SequenceTGRMSearchService.get(query)
