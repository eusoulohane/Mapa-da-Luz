# -*- coding: utf-8 -*-
"""
MOTOR DE CÁLCULO - NUMEROLOGIA
Mapa da Luz - Loh do @LuzdeLoh

Esse script calcula os 3 números (Destino, Alma, Personalidade)
a partir do nome completo e data de nascimento da cliente.

Não precisa de internet nem de nenhuma biblioteca externa.
"""

from biblioteca_numerologia import DESTINO, ALMA, PERSONALIDADE

# Tabela de conversão letra -> número (padrão pitagórico)
TABELA_PITAGORICA = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
    'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
    'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
}

VOGAIS = set('AEIOU')

# Letras com acento -> letra sem acento (simplificação para nomes em português)
MAPA_ACENTOS = {
    'Á': 'A', 'À': 'A', 'Â': 'A', 'Ã': 'A',
    'É': 'E', 'È': 'E', 'Ê': 'E',
    'Í': 'I', 'Ì': 'I',
    'Ó': 'O', 'Ò': 'O', 'Ô': 'O', 'Õ': 'O',
    'Ú': 'U', 'Ù': 'U',
    'Ç': 'C',
}


def normalizar_nome(nome: str) -> str:
    """Remove acentos e deixa só letras maiúsculas, sem espaços."""
    nome = nome.upper()
    nome_limpo = ''
    for letra in nome:
        letra = MAPA_ACENTOS.get(letra, letra)
        if letra.isalpha():
            nome_limpo += letra
    return nome_limpo


def reduzir_numero(numero: int) -> int:
    """
    Reduz um número somando seus dígitos, até chegar a um único dígito
    -- EXCETO se a soma intermediária for 11 ou 22 (números mestres).
    """
    while numero > 9 and numero not in (11, 22):
        numero = sum(int(d) for d in str(numero))
    return numero


def calcular_destino(dia: int, mes: int, ano: int) -> int:
    """Soma todos os dígitos da data de nascimento e reduz."""
    todos_digitos = f"{dia}{mes}{ano}"
    soma = sum(int(d) for d in todos_digitos)
    return reduzir_numero(soma)


def calcular_alma(nome_completo: str) -> int:
    """Soma o valor das vogais do nome completo e reduz."""
    nome_limpo = normalizar_nome(nome_completo)
    soma = sum(TABELA_PITAGORICA[letra] for letra in nome_limpo if letra in VOGAIS)
    return reduzir_numero(soma)


def calcular_personalidade(nome_completo: str) -> int:
    """Soma o valor das consoantes do nome completo e reduz."""
    nome_limpo = normalizar_nome(nome_completo)
    soma = sum(TABELA_PITAGORICA[letra] for letra in nome_limpo if letra not in VOGAIS)
    return reduzir_numero(soma)


def gerar_bloco_numerologia(nome_completo: str, dia: int, mes: int, ano: int) -> dict:
    """
    Função principal: recebe os dados da cliente e devolve o bloco
    completo de numerologia já com os textos certos da biblioteca.
    """
    numero_destino = calcular_destino(dia, mes, ano)
    numero_alma = calcular_alma(nome_completo)
    numero_personalidade = calcular_personalidade(nome_completo)

    return {
        "numero_destino": numero_destino,
        "destino": DESTINO[numero_destino],
        "numero_alma": numero_alma,
        "alma": ALMA[numero_alma],
        "numero_personalidade": numero_personalidade,
        "personalidade": PERSONALIDADE[numero_personalidade],
    }


# ---------------------------------------------------------
# TESTE COM OS DADOS DA PRÓPRIA LOH (do e-book original)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("TESTE DO MOTOR DE NUMEROLOGIA — dados da Loh")
    print("=" * 60)

    resultado = gerar_bloco_numerologia(
        nome_completo="Lohane",  # idealmente o nome completo de registro
        dia=17, mes=8, ano=1985
    )

    print(f"\n🔢 Número do Destino: {resultado['numero_destino']} — {resultado['destino']['nome']}")
    print(f"   {resultado['destino']['texto']}")

    print(f"\n❤️  Número da Alma: {resultado['numero_alma']}")
    print(f"   {resultado['alma']['texto']}")

    print(f"\n🤝 Número da Personalidade: {resultado['numero_personalidade']}")
    print(f"   {resultado['personalidade']['texto']}")

    print("\n" + "=" * 60)
    print("Esperado (do e-book original): Destino 3, Alma 9, Personalidade 11/2")
    print("=" * 60)
