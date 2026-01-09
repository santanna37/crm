"""criação do seed

Revision ID: e6b8318425d4
Revises: 598a964a82dd
Create Date: 2026-01-08 21:41:29.234333

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e6b8318425d4'
down_revision: Union[str, Sequence[str], None] = '598a964a82dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    connection = op.get_bind()

    themes = [
        ("educacao", "Educação"),
        ("saude", "Saúde"),
        ("trabalho_renda", "Trabalho e Renda"),
        ("moradia", "Moradia"),
        ("seguranca_publica", "Segurança Pública"),
        ("reforma_agraria", "Reforma Agrária"),
        ("igualdade_genero", "Igualdade de Gênero"),
        ("justica_social", "Justiça Social"),
        ("direitos_lgbt", "Direitos LGBT"),
        ("igualdade_racial", "Igualdade Racial"),
        ("militancia_digital", "Militância Digital"),
        ("cultura", "Cultura"),
        ("politica", "Política"),
        ("meio_ambiente", "Meio Ambiente"),
        ("outros", "Outros"),
    ]

    for code, description in themes:
        connection.execute(
            sa.text("""
                INSERT INTO themes (code, description)
                VALUES (:code, :description)
                ON DUPLICATE KEY UPDATE
                    description = VALUES(description)
            """),
            {"code": code, "description": description}
        )



def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DELETE FROM themes")