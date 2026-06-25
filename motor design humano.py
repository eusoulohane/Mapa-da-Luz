# -*- coding: utf-8 -*-
"""
MOTOR DE CÁLCULO - DESIGN HUMANO
Mapa da Luz - Loh do @LuzdeLoh

⚠️ ESTE SCRIPT PRECISA DE 2 PASSOS DE INSTALAÇÃO NO GOOGLE COLAB,
ANTES de rodar este código (rode cada linha numa célula separada):

    !pip install pyswisseph
    !git clone https://github.com/geodetheseeker/human-design-py

Depois, esse script precisa estar na MESMA pasta que o arquivo
"chart.py" que vem dentro da pasta clonada "human-design-py".
No Colab, a forma mais simples é:

    import sys
    sys.path.append('/content/human-design-py')

NO STREAMLIT CLOUD: a pasta "human-design-py" precisa estar dentro
do mesmo repositório do GitHub, na raiz do projeto. O caminho abaixo
já está ajustado para funcionar nesse ambiente (pasta relativa,
não absoluta como no Colab).

Esse script calcula Tipo, Estratégia, Autoridade e Perfil
a partir de data, hora e fuso horário de nascimento da cliente,
e já devolve com o texto certo da biblioteca do Mapa da Luz.

IMPORTANTE SOBRE 'utc_offset':
Esse número é a diferença entre o horário de nascimento e o
horário de Greenwich (UTC). No Brasil:
  - Horário de Brasília (a maioria do Brasil): utc_offset = -3
  - Caso o nascimento tenha sido em horário de verão (não existe
    mais desde 2019, mas se a pessoa nasceu antes, confirme a data)
"""

import sys
import os

# Caminho relativo: funciona tanto no Colab (se a pasta estiver em /content)
# quanto no Streamlit Cloud (se a pasta estiver na raiz do repositório)
_pasta_atual = os.path.dirname(os.path.abspath(__file__))
_caminho_human_design = os.path.join(_pasta_atual, "human-design-py")
if os.path.exists(_caminho_human_design):
    sys.path.append(_caminho_human_design)
else:
    sys.path.append('/content/human-design-py')  # fallback para Colab

from chart import calculate_chart

# ---------------------------------------------------------
# BIBLIOTECA DE TEXTOS - DESIGN HUMANO
# (extraída do documento Mapa_da_Luz_Design_Humano.md)
# ---------------------------------------------------------

TIPO_ESTRATEGIA = {
    "Generator": {
        "nome_pt": "Geradora",
        "estrategia_pt": "Responder",
        "texto": "Você tem energia vital abundante e constante — seu corpo é feito para o trabalho que te entusiasma de verdade. Sua forma de navegar o mundo não é correndo atrás, é respondendo ao que a vida te apresenta. O sinal de que está no caminho certo é o entusiasmo genuíno; o sinal de alerta é a frustração de fazer algo só por obrigação.",
        "pratica": "Antes de criar algo do zero, espere a vida te trazer um convite, uma pergunta ou uma oportunidade — e sinta no corpo se é um \"sim\" ou um \"não\" antes de decidir."
    },
    "Manifestor": {
        "nome_pt": "Manifestadora",
        "estrategia_pt": "Informar",
        "texto": "Você tem a capacidade rara de iniciar o que ainda não existe. Sua energia é independente e impactante — você não precisa de permissão pra começar algo. O desafio do seu tipo é que esse impacto pode ser sentido como invasão pelos outros, se vier sem aviso.",
        "pratica": "Antes de agir, informe quem será afetado pela sua decisão. Isso não é pedir permissão, é abrir caminho para que seu impacto seja recebido como dom."
    },
    "Projector": {
        "nome_pt": "Projetora",
        "estrategia_pt": "Esperar o convite",
        "texto": "Você não tem energia constante para sustentar ação o tempo todo, e está tudo bem — sua força não está na quantidade, está na qualidade da visão. Você vê o que os outros não veem e sabe guiar com precisão cirúrgica. O desafio é querer provar valor fazendo mais, quando seu valor já está em ver melhor.",
        "pratica": "Em decisões importantes (trabalho, parcerias, relacionamentos), espere ser reconhecida e convidada antes de se oferecer. O convite valida que sua energia será bem recebida."
    },
    "Reflector": {
        "nome_pt": "Refletora",
        "estrategia_pt": "Esperar um ciclo lunar",
        "texto": "Você é rara e profundamente sensível ao ambiente ao seu redor — sua aura absorve e reflete o que está perto de você como nenhum outro tipo. Decisões tomadas rápido raramente são as certas pra você. O desafio é a pressão (própria ou externa) por respostas imediatas.",
        "pratica": "Para decisões grandes, dê a si mesma um ciclo lunar completo (cerca de 28 dias) antes de decidir. Observe como a decisão \"se sente\" em diferentes dias."
    },
    "Manifesting Generator": {
        "nome_pt": "Geradora Manifestante",
        "estrategia_pt": "Responder, depois informar",
        "texto": "Você é movimento e resposta ao mesmo tempo — tem energia abundante como a Geradora, mas também a capacidade de iniciar como a Manifestadora. Sua velocidade pode parecer inquietação, mas na verdade é seu jeito natural de operar. O desafio é pular etapas (das pessoas, dos processos) na pressa de agir.",
        "pratica": "Espere o entusiasmo genuíno chegar antes de agir (como a Geradora), mas, uma vez decidida, informe quem for impactado pela sua rapidez."
    },
}

AUTORIDADE = {
    "Sacral": "Sua decisão mais alinhada vem de uma resposta do corpo, não de uma análise mental — uma sensação de \"sim\" energético ou \"não\" que se retrai. Decisões pensadas demais te afastam da resposta certa. Na prática: faça a pergunta em voz alta pra você mesma e perceba a primeira reação do corpo, antes que a mente comece a justificar.",
    "Emotional": "Sua clareza não chega no calor do momento — ela chega depois de um ciclo emocional completo. Decisão tomada em pico de emoção, positiva ou negativa, tende a não ser definitiva. Na prática: nunca decida algo importante na primeira conversa. Durma, espere a onda emocional passar, e veja se a mesma clareza continua no dia seguinte.",
    "Splenic": "Sua intuição fala uma vez, rápida e silenciosa — sem repetir o aviso. Diferente da emoção, ela não é dramática, é uma percepção sutil no presente. Na prática: preste atenção ao primeiro instinto sutil que aparece, antes de você racionalizar ou ignorá-lo.",
    "Ego": "Sua clareza vem de uma pergunta simples: \"eu quero isso de verdade, com força de vontade?\" Não é sobre o que parece certo pros outros, é sobre o que você genuinamente se compromete a fazer valer. Na prática: pergunte-se em voz alta \"eu realmente quero fazer isso?\".",
    "Self-Projected": "Sua clareza chega quando você fala sobre a decisão em voz alta, para alguém de confiança que só escuta, sem opinar. Na prática: busque alguém (ou até grave um áudio sozinha) e fale sobre a decisão em voz alta.",
    "Mental": "Sua clareza depende do ambiente certo e de boas conversas — você pensa melhor em diálogo, num espaço onde se sente segura. Na prática: leve decisões importantes para conversar em ambientes confortáveis, com pessoas neutras e de confiança.",
    "Lunar": "Sua clareza segue o ciclo da lua — quase um mês inteiro de observação antes da decisão amadurecer. Na prática: anote como a decisão \"parece\" em diferentes fases da lua, e só decida de fato ao fechar o ciclo completo.",
}

LINHA_PERFIL = {
    1: "Investigadora — Você precisa se sentir segura através do conhecimento: pesquisa, estuda e busca entender a fundo antes de agir. Sua estabilidade vem de ter uma base sólida de informação.",
    2: "Eremita — Você precisa de tempo sozinha para recarregar, mesmo que tenha talentos naturais que os outros notam antes de você mesma. Ser \"chamada\" para agir funciona melhor do que se forçar a aparecer.",
    3: "Mártir (Experimentadora) — Você aprende na prática, através de tentativa, erro e recomeço. A vida te ensina pela experiência direta — e isso não é fracasso, é seu método natural de aprendizado.",
    4: "Oportunista (Rede de apoio) — Você constrói através de relações próximas e de uma rede de pessoas de confiança. Suas oportunidades chegam através de quem você já conhece.",
    5: "Herética (Salvadora) — Você é vista pelos outros como alguém que tem soluções práticas, mesmo quando não pediu esse papel. Parte do seu aprendizado é administrar essa projeção sem se perder nela.",
    6: "Modelo (Vida em três fases) — Você vive sua vida em três fases distintas: experimentação intensa, depois observação de cima, e por fim se torna exemplo vivo de sabedoria para os outros.",
}


def gerar_bloco_design_humano(ano: int, mes: int, dia: int,
                                 hora: int, minuto: int, utc_offset: float) -> dict:
    """
    Função principal: recebe os dados de nascimento da cliente e devolve
    o bloco completo de Design Humano (Tipo, Estratégia, Autoridade, Perfil)
    já com os textos certos da biblioteca.
    """
    resultado = calculate_chart(
        birth_year=ano, birth_month=mes, birth_day=dia,
        birth_hour=hora, birth_minute=minuto,
        utc_offset=utc_offset
    )

    tipo_en = resultado.get("type")
    autoridade_en = resultado.get("authority")
    perfil = resultado.get("profile")  # formato esperado: "1/3", "2/4", etc.

    tipo_info = TIPO_ESTRATEGIA.get(tipo_en, {})
    autoridade_texto = AUTORIDADE.get(autoridade_en, "Texto não encontrado para esta autoridade.")

    linha1_texto, linha2_texto = "", ""
    if perfil and "/" in str(perfil):
        try:
            l1, l2 = str(perfil).split("/")
            linha1_texto = LINHA_PERFIL.get(int(l1), "")
            linha2_texto = LINHA_PERFIL.get(int(l2), "")
        except (ValueError, IndexError):
            pass

    return {
        "tipo_original": tipo_en,
        "tipo_nome": tipo_info.get("nome_pt", tipo_en),
        "estrategia": tipo_info.get("estrategia_pt", ""),
        "tipo_texto": tipo_info.get("texto", ""),
        "tipo_pratica": tipo_info.get("pratica", ""),
        "autoridade_original": autoridade_en,
        "autoridade_texto": autoridade_texto,
        "perfil": perfil,
        "perfil_linha1_texto": linha1_texto,
        "perfil_linha2_texto": linha2_texto,
        "resultado_completo_bruto": resultado,  # guardado para conferência/depuração
    }


# ---------------------------------------------------------
# TESTE COM OS DADOS DA PRÓPRIA LOH
# Edite hora, minuto e utc_offset antes de rodar
# ---------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("TESTE DO MOTOR DE DESIGN HUMANO — dados da Loh")
    print("=" * 60)

    resultado = gerar_bloco_design_humano(
        ano=1985, mes=8, dia=17,
        hora=8, minuto=50,        # <-- já usando a hora real informada
        utc_offset=-3              # horário de Brasília
    )

    print(f"\n🌟 Tipo: {resultado['tipo_nome']} ({resultado['tipo_original']})")
    print(f"   Estratégia: {resultado['estrategia']}")
    print(f"   {resultado['tipo_texto']}")
    print(f"   👉 {resultado['tipo_pratica']}\n")

    print(f"🔥 Autoridade: {resultado['autoridade_original']}")
    print(f"   {resultado['autoridade_texto']}\n")

    print(f"🧬 Perfil: {resultado['perfil']}")
    print(f"   Linha 1: {resultado['perfil_linha1_texto']}")
    print(f"   Linha 2: {resultado['perfil_linha2_texto']}\n")

    print("=" * 60)
    print("Esperado (do e-book original): Tipo Gerador Manifestante,")
    print("Autoridade Sacral, Perfil 1/3")
    print("=" * 60)

    print("\n📋 Resultado bruto completo (para conferência técnica):")
    print(resultado["resultado_completo_bruto"])
