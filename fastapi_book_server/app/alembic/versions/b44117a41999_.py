"""empty message

Revision ID: b44117a41999
Revises: 08193b547a80
Create Date: 2021-11-18 18:25:06.921287

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import UniqueConstraint


# revision identifiers, used by Alembic.
revision = "b44117a41999"
down_revision = "08193b547a80"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("books", sa.Column("pages", sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("books", "pages")
    # ### end Alembic commands ###
