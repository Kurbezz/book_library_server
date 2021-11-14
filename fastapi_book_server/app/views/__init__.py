from app.views.source import source_router

from app.views.author import author_router
from app.views.author_annotation import author_annotation_router

from app.views.book import book_router
from app.views.book_annotation import book_annotation_router

from app.views.translation import translation_router

from app.views.sequence import sequence_router
from app.views.sequence_info import sequence_info_router


routers = [
    source_router,
    author_router,
    author_annotation_router,
    book_router,
    book_annotation_router,
    translation_router,
    sequence_router,
    sequence_info_router,
]
