"""create img_info table

Revision ID: c4e9a20687ae
Revises: 
Create Date: 2020-03-26 18:22:45.907487

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = 'c4e9a20687ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    img_info_table = op.create_table('img_info',
                                     sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                                     sa.Column('title', sa.String(length=80), nullable=False),
                                     sa.Column('location', sa.String(), nullable=False),
                                     sa.Column('category', sa.String(), nullable=False),
                                     sa.Column('created', sa.Date(), nullable=False)
                                     )

    op.bulk_insert(
        img_info_table,
        [
            {'title': 'img1', 'location': 'loc1', 'category': 'cat1', 'created': datetime.date.today()},
            {'title': 'img2', 'location': 'loc2', 'category': 'cat1', 'created': datetime.date.today()},
            {'title': 'img3', 'location': 'loc3', 'category': 'cat2', 'created': datetime.date.today()},
            {'title': 'img4', 'location': 'loc4', 'category': 'cat2', 'created': datetime.date.today()},
            {'title': 'img5', 'location': 'loc5', 'category': 'cat1', 'created': datetime.date.today()},
            {'title': 'img6', 'location': 'loc6', 'category': 'cat2', 'created': datetime.date.today()},
            {'title': 'img7', 'location': 'loc7', 'category': 'cat1', 'created': datetime.date.today()},
        ]
    )


def downgrade():
    op.drop_table('img_info')
