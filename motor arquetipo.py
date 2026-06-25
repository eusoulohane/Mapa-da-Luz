# -*- coding: utf-8 -*-
"""
MOTOR DE CÁLCULO - ARQUÉTIPO-SÍNTESE
Mapa da Luz - Loh do @LuzdeLoh

Esse script combina o resultado de Astrologia (elemento do Sol) com
o resultado de Design Humano (Tipo) para gerar o Arquétipo-síntese
final, incluindo a missão em uma linha.

Não precisa de nenhuma instalação nova — usa os resultados que já
vêm dos motores de astrologia e design humano.
"""

# ---------------------------------------------------------
# MAPA: signo do Sol -> elemento -> nome-base do arquétipo
# ---------------------------------------------------------

ELEMENTO_POR_SIGNO = {
    "Ari": "Fogo", "Leo": "Fogo", "Sag": "Fogo",
    "Tau": "Terra", "Vir": "Terra", "Cap": "Terra",
    "Gem": "Ar", "Lib": "Ar", "Aqu": "Ar",
    "Can": "Água", "Sco": "Água", "Pis": "Água",
}

NOME_BASE_POR_ELEMENTO = {
    "Fogo": "Sacerdotisa",
    "Terra": "Guardiã",
    "Ar": "Oradora",
    "Água": "Curadora",
}

TEXTO_BASE_POR_ELEMENTO = {
    "Fogo": "Você nasceu para brilhar e liderar com o coração. Sua energia é solar, generosa e cheia de coragem — você não apenas atravessa desafios, você os transforma em luz para quem está ao seu redor. Seu jeito de existir já é, por si só, um convite para os outros se permitirem mais.",
    "Terra": "Você nasceu com a missão de construir o que é sólido e duradouro. Sua presença transmite segurança, e sua força está em transformar sonhos em realidade concreta, passo a passo. Onde você está, as coisas ganham estrutura, raiz e permanência.",
    "Ar": "Você nasceu para conectar mundos através da palavra e da ideia. Sua mente é rápida, curiosa e tem o dom raro de traduzir o complexo em algo que todos entendem. Sua voz — falada ou escrita — é a ferramenta que usa para unir pessoas e despertar consciências.",
    "Água": "Você nasceu com uma sensibilidade que percebe o que está por trás das palavras. Sua intuição é seu superpoder, e sua maior força nasce justamente onde antes havia dor — você transforma o que viveu em cura para quem cruza seu caminho.",
}

# ---------------------------------------------------------
# MAPA: tipo de Design Humano -> qualificador do arquétipo
# ---------------------------------------------------------

QUALIFICADOR_POR_TIPO = {
    "Generator": "Construtora",
    "Manifestor": "Visionária",
    "Projector": "Guia",
    "Reflector": "Espelho",
    "Manifesting Generator": "Criativa",
}

TEXTO_COMPLEMENTO_POR_TIPO = {
    "Generator": "Sua energia vital é constante e poderosa — você tem combustível para ir até o fim do que se compromete. Seu caminho de poder é responder ao que genuinamente te entusiasma, e não forçar o que não é seu. Quando você se envolve de coração, nada a detém.",
    "Manifestor": "Você tem a capacidade rara de iniciar o que ainda não existe. Sua energia abre portas e impacta o ambiente à sua volta, mesmo sem esforço consciente. Seu desafio é aprender a informar antes de agir, para que seu impacto seja recebido como dom, não como invasão.",
    "Projector": "Você não nasceu para fazer tudo sozinha, nasceu para ver o que os outros não veem e guiar com precisão. Sua energia não é constante como a de um Gerador — e está tudo bem, porque seu poder está na clareza da visão, não na quantidade de ação.",
    "Reflector": "Você é rara e profundamente sensível ao ambiente que a rodeia — sua aura absorve e reflete o que está à sua volta como nenhum outro tipo. Seu tempo de decisão é mais longo, e isso não é fraqueza: é a sua forma de honrar um ciclo inteiro antes de agir.",
    "Manifesting Generator": "Você é movimento e resposta ao mesmo tempo. Sua energia é magnética e múltipla — você inicia e sustenta com a mesma intensidade. Seu caminho de poder é responder primeiro ao que a entusiasma, e só então agir com toda a sua força criativa.",
}

# ---------------------------------------------------------
# MISSÃO EM UMA LINHA - as 20 combinações (Elemento x Tipo)
# ---------------------------------------------------------

MISSAO_EM_UMA_LINHA = {
    ("Fogo", "Generator"): "Minha missão é transformar desafios em luz e constância em legado. Eu não desisto, eu sustento!",
    ("Fogo", "Manifestor"): "Minha missão é transformar desafios em luz e visão em caminho novo. Eu não espero abrirem a porta, eu abro!",
    ("Fogo", "Projector"): "Minha missão é transformar desafios em luz e clareza em direção. Eu não decido por você, eu te mostro o caminho!",
    ("Fogo", "Reflector"): "Minha missão é transformar desafios em luz e sensibilidade em verdade. Eu não escondo o que vejo, eu reflito!",
    ("Fogo", "Manifesting Generator"): "Minha missão é transformar desafios em luz e entusiasmo em ação. Eu não espero o momento perfeito, eu crio!",

    ("Terra", "Generator"): "Minha missão é transformar sonho em estrutura e constância em resultado. Eu não improviso, eu construo!",
    ("Terra", "Manifestor"): "Minha missão é transformar sonho em estrutura e visão em fundação. Eu não espero o terreno pronto, eu o preparo!",
    ("Terra", "Projector"): "Minha missão é transformar sonho em estrutura e clareza em próximo passo. Eu não carrego por você, eu te aponto o chão!",
    ("Terra", "Reflector"): "Minha missão é transformar sonho em estrutura e sensibilidade em base segura. Eu não finjo solidez, eu a sinto e a dou!",
    ("Terra", "Manifesting Generator"): "Minha missão é transformar sonho em estrutura e entusiasmo em construção real. Eu não esboço, eu edifico!",

    ("Ar", "Generator"): "Minha missão é transformar ideia em palavra que conecta e constância em repertório. Eu não falo uma vez, eu repito até tocar!",
    ("Ar", "Manifestor"): "Minha missão é transformar ideia em palavra que conecta e visão em discurso novo. Eu não espero ser convidada a falar, eu digo!",
    ("Ar", "Projector"): "Minha missão é transformar ideia em palavra que conecta e clareza em direção. Eu não compito, eu traduzo o caminho!",
    ("Ar", "Reflector"): "Minha missão é transformar ideia em palavra que conecta e sensibilidade em escuta certeira. Eu não falo primeiro, eu ouço e devolvo!",
    ("Ar", "Manifesting Generator"): "Minha missão é transformar ideia em palavra que conecta e entusiasmo em conteúdo vivo. Eu não guardo a ideia, eu coloco no mundo!",

    ("Água", "Generator"): "Minha missão é transformar dor em cura e constância em transformação real. Eu não abandono no meio, eu acompanho até virar raiz!",
    ("Água", "Manifestor"): "Minha missão é transformar dor em cura e visão em primeiro passo de saída. Eu não espero a ferida cicatrizar sozinha, eu abro caminho!",
    ("Água", "Projector"): "Minha missão é transformar dor em cura e clareza em direção segura. Eu não vivi em vão, minha história é bússola pra você!",
    ("Água", "Reflector"): "Minha missão é transformar dor em cura e sensibilidade em pergunta certa. Eu não ignoro o não dito, eu sinto e devolvo!",
    ("Água", "Manifesting Generator"): "Minha missão é transformar dor em cura e entusiasmo em método vivo. Eu não guardo minha história, eu transformo ela em ponte!",
}


def gerar_arquetipo_sintese(sol_signo: str, tipo_design_humano: str) -> dict:
    """
    Função principal: recebe o signo do Sol (formato Kerykeion, ex: "Leo")
    e o tipo de Design Humano (formato human-design-py, ex: "Manifesting Generator")
    e devolve o Arquétipo-síntese completo: nome, textos e missão.
    """
    elemento = ELEMENTO_POR_SIGNO.get(sol_signo)
    if elemento is None:
        return {"erro": f"Signo solar '{sol_signo}' não reconhecido."}

    nome_base = NOME_BASE_POR_ELEMENTO[elemento]
    qualificador = QUALIFICADOR_POR_TIPO.get(tipo_design_humano)
    if qualificador is None:
        return {"erro": f"Tipo de Design Humano '{tipo_design_humano}' não reconhecido."}

    nome_completo = f"{nome_base} {qualificador}"
    texto_base = TEXTO_BASE_POR_ELEMENTO[elemento]
    texto_complemento = TEXTO_COMPLEMENTO_POR_TIPO[tipo_design_humano]
    missao = MISSAO_EM_UMA_LINHA.get((elemento, tipo_design_humano), "")

    return {
        "elemento": elemento,
        "nome_arquetipo": nome_completo,
        "texto_base": texto_base,
        "texto_complemento": texto_complemento,
        "missao_em_uma_linha": missao,
    }


# ---------------------------------------------------------
# TESTE COM OS DADOS DA PRÓPRIA LOH
# (usa os resultados já validados de Sol=Leo e Tipo=Manifesting Generator)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("TESTE DO MOTOR DE ARQUÉTIPO-SÍNTESE — dados da Loh")
    print("=" * 60)

    resultado = gerar_arquetipo_sintese(
        sol_signo="Leo",
        tipo_design_humano="Manifesting Generator"
    )

    print(f"\n✨ ARQUÉTIPO: A {resultado['nome_arquetipo'].upper()}\n")
    print(f"{resultado['texto_base']}\n")
    print(f"{resultado['texto_complemento']}\n")
    print(f"💫 Missão: \"{resultado['missao_em_uma_linha']}\"\n")

    print("=" * 60)
    print("Esperado: A Sacerdotisa Criativa")
    print("=" * 60)
