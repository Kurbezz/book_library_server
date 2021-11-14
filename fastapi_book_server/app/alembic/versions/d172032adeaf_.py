"""empty message

Revision ID: d172032adeaf
Revises: 
Create Date: 2021-11-05 17:22:11.717389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd172032adeaf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sources',
    sa.Column('id', sa.SmallInteger(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source', sa.SmallInteger(), nullable=False),
    sa.Column('remote_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=256), nullable=False),
    sa.Column('last_name', sa.String(length=256), nullable=False),
    sa.Column('middle_name', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['source'], ['sources.id'], name='fk_authors_sources_id_source'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('source', 'remote_id', name='uc_authors_source_remote_id')
    )
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source', sa.SmallInteger(), nullable=False),
    sa.Column('remote_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('lang', sa.String(length=2), nullable=False),
    sa.Column('file_type', sa.String(length=4), nullable=False),
    sa.Column('uploaded', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['source'], ['sources.id'], name='fk_books_sources_id_source'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('source', 'remote_id', name='uc_books_source_remote_id')
    )
    op.create_table('sequences',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source', sa.SmallInteger(), nullable=False),
    sa.Column('remote_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.ForeignKeyConstraint(['source'], ['sources.id'], name='fk_sequences_sources_id_source'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('source', 'remote_id', name='uc_sequences_source_remote_id')
    )
    op.create_table('author_annotations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('file', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['authors.id'], name='fk_author_annotations_authors_id_author'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('author')
    )
    op.create_table('book_annotations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('file', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['book'], ['books.id'], name='fk_book_annotations_books_id_book'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('book')
    )
    op.create_table('sequence_infos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book', sa.Integer(), nullable=False),
    sa.Column('sequence', sa.Integer(), nullable=False),
    sa.Column('position', sa.SmallInteger(), nullable=False),
    sa.ForeignKeyConstraint(['book'], ['books.id'], name='fk_sequence_infos_books_id_book'),
    sa.ForeignKeyConstraint(['sequence'], ['sequences.id'], name='fk_sequence_infos_sequences_id_sequence'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('book', 'sequence', name='uc_sequence_infos_book_sequence')
    )
    op.create_table('translations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book', sa.Integer(), nullable=False),
    sa.Column('translator', sa.Integer(), nullable=False),
    sa.Column('position', sa.SmallInteger(), nullable=False),
    sa.ForeignKeyConstraint(['book'], ['books.id'], name='fk_translations_books_id_book'),
    sa.ForeignKeyConstraint(['translator'], ['authors.id'], name='fk_translations_authors_id_translator'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('book', 'translator', name='uc_translations_book_translator')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('translations')
    op.drop_table('sequence_infos')
    op.drop_table('book_annotations')
    op.drop_table('author_annotations')
    op.drop_table('sequences')
    op.drop_table('books')
    op.drop_table('authors')
    op.drop_table('sources')
    # ### end Alembic commands ###
