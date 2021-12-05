from app.models import Sequence

from app.services.common import TRGMSearchService


GET_OBJECTS_IDS_QUERY = """
EXPLAIN ANALYZE SELECT ARRAY (
    WITH filtered_sequences AS (
        SELECT 
            id,
            similarity(name, :query) as sml,
            (
                SELECT count(*) FROM book_sequences
                LEFT JOIN books ON books.id = book
                WHERE sequence = sequences.id AND books.is_deleted = 'f'
            ) as books_count
        FROM sequences
        WHERE name % :query AND
        EXISTS (
            SELECT * FROM book_sequences
            LEFT JOIN books ON books.id = book
            WHERE sequence = sequences.id AND books.is_deleted = 'f'
        )
    )
    SELECT fsequences.id FROM filtered_sequences as fsequences
    ORDER BY fsequences.sml DESC, fsequences.books_count DESC
);
"""


class SequenceTGRMSearchService(TRGMSearchService):
    MODEL_CLASS = Sequence
    PREFETCH_RELATED = ["source"]
    GET_OBJECTS_IDS_QUERY = GET_OBJECTS_IDS_QUERY
