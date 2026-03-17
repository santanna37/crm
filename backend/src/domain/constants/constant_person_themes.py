"""
TEMAS DE INTERESSE DA CAMPANHA 
"""

from enum import IntEnum



class ThemesCode(IntEnum):
    EDUCACAO = 1
    SAUDE = 2
    ASSISTENCIA_SOCIAL = 3
    CULTURA = 4
    ESPORTE_LAZER = 5
    DIREITOS_HUMANOS = 6
    MULHERES = 7
    IGUALDADE_RACIAL = 8
    JUVENTUDE = 9
    PESSOA_COM_DEFICIENCIA = 10 
    PESSOA_IDOSA = 11
    MEIO_AMBIENTE = 12
    DESENVOLVIMENTO_ECONOMICO = 13
    SEGURANCA_ALIMENTAR = 14
    SEGURANCA_PUBLICA = 15  
    OUTROS = 16 

    @classmethod
    def get_theme(cls, theme_name:str) -> int:
        mapping = {
            "Educação": cls.EDUCACAO,
            "Saúde": cls.SAUDE,
            "Assistência Social": cls.ASSISTENCIA_SOCIAL,
            "Cultura": cls.CULTURA,
            "Esporte e Lazer": cls.ESPORTE_LAZER,
            "Direitos Humanos": cls.DIREITOS_HUMANOS,
            "Mulheres": cls.MULHERES,
            "Igualdade Racial": cls.IGUALDADE_RACIAL,
            "Juventude": cls.JUVENTUDE,
            "Pessoa com Deficiência": cls.PESSOA_COM_DEFICIENCIA,
            "Pessoa Idosa": cls.PESSOA_IDOSA,
            "Meio Ambiente": cls.MEIO_AMBIENTE,
            "Desenvolvimento Econômico": cls.DESENVOLVIMENTO_ECONOMICO,
            "Segurança Alimentar": cls.SEGURANCA_ALIMENTAR,
            "Segurança Publica": cls.SEGURANCA_PUBLICA,
            "Outros": cls.OUTROS
        }

        theme_enum = mapping.get(theme_name)

        if theme_enum:
            return theme_enum.value
            
        return cls.OUTROS.value