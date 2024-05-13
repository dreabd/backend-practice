"""empty message

Revision ID: 5f49280e2f3e
Revises: bcc9987d987c
Create Date: 2024-05-12 21:40:21.608296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f49280e2f3e'
down_revision = 'bcc9987d987c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cereals', schema=None) as batch_op:
        batch_op.alter_column('calories',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(precision=5, scale=1),
               existing_nullable=True)
        batch_op.alter_column('protein',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(precision=5, scale=1),
               existing_nullable=True)
        batch_op.alter_column('fat',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(precision=5, scale=1),
               existing_nullable=True)
        batch_op.alter_column('sodium',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(precision=5, scale=1),
               existing_nullable=True)
        batch_op.alter_column('fiber',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(precision=5, scale=1),
               existing_nullable=True)
        batch_op.alter_column('carbo',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(precision=5, scale=1),
               existing_nullable=True)
        batch_op.alter_column('sugars',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(precision=5, scale=1),
               existing_nullable=True)
        batch_op.alter_column('potass',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(precision=5, scale=1),
               existing_nullable=True)
        batch_op.alter_column('vitamins',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(precision=5, scale=1),
               existing_nullable=True)
        batch_op.alter_column('shelf',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(precision=5, scale=1),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cereals', schema=None) as batch_op:
        batch_op.alter_column('shelf',
               existing_type=sa.Numeric(precision=5, scale=1),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('vitamins',
               existing_type=sa.Numeric(precision=5, scale=1),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('potass',
               existing_type=sa.Numeric(precision=5, scale=1),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('sugars',
               existing_type=sa.Numeric(precision=5, scale=1),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('carbo',
               existing_type=sa.Numeric(precision=5, scale=1),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('fiber',
               existing_type=sa.Numeric(precision=5, scale=1),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('sodium',
               existing_type=sa.Numeric(precision=5, scale=1),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('fat',
               existing_type=sa.Numeric(precision=5, scale=1),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('protein',
               existing_type=sa.Numeric(precision=5, scale=1),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('calories',
               existing_type=sa.Numeric(precision=5, scale=1),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###
