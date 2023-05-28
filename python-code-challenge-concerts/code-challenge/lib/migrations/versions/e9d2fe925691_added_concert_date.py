"""Added Concert date

Revision ID: e9d2fe925691
Revises: 467ee933dfe0
Create Date: 2023-05-26 19:05:49.949144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9d2fe925691'
down_revision = '467ee933dfe0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('concerts', sa.Column('date', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('concerts', 'date')
    # ### end Alembic commands ###