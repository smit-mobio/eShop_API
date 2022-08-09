"""empty message

Revision ID: 1428c087aeb3
Revises: 0dd272dc2955
Create Date: 2022-08-09 12:20:01.467305

"""
from datetime import datetime
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'ac420ef3fa7a'
down_revision = '0dd272dc2955'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    product_status = [
        ('Out of Stock', "Out of Stock"),
        ('Instock', 'Instock')
    ],
    product_category = [
        ('Man', "Man"),
        ('Women', 'Women'),
        ('Kids', "Kids")
    ]
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('detail', sa.String(length=200), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('brand', sa.String(length=50), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('image', sa.String(length=300), nullable=True),
    sa.Column('status', sqlalchemy_utils.types.choice.ChoiceType(product_status), nullable=False),
    sa.Column('category', sqlalchemy_utils.types.choice.ChoiceType(product_category), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(),default = datetime.now(), nullable=True),
    sa.Column('updated_on', sa.DateTime(),default = datetime.now(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###
