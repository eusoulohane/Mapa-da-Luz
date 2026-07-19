# -*- coding: utf-8 -*-
"""
MOTOR DE CÁLCULO - ASTROLOGIA
Mapa da Luz - Loh do @LuzdeLoh

⚠️ ESTE SCRIPT PRECISA DA BIBLIOTECA "kerykeion" INSTALADA.
No Google Colab, rode esta linha numa célula ANTES de usar este script:

    !pip install kerykeion

Esse script calcula Sol, Lua, Ascendente, Casa 2 e Casa 9
a partir de nome, data, hora e local de nascimento da cliente,
e já devolve com o texto certo da biblioteca do Mapa da Luz.
"""

from kerykeion import AstrologicalSubject

# ---------------------------------------------------------
# BIBLIOTECA DE TEXTOS - ASTROLOGIA
# (extraída dos documentos Mapa_da_Luz_Astrologia_Parte1 e Parte2)
# ---------------------------------------------------------

SOL = {
    "Ari": "Você existe com intensidade desde o primeiro segundo de qualquer situação. Sua identidade central é a coragem de começar — você não espera o momento ideal, você cria o momento agindo. O desafio é a impaciência: nem tudo floresce no ritmo que você gostaria.",
    "Tau": "Você existe com presença sólida e ritmo próprio. Sua identidade central é a constância — você constrói valor através do tempo, não da pressa. O desafio é a resistência à mudança: às vezes segurar demais impede o novo de entrar.",
    "Gem": "Você existe em movimento mental constante. Sua identidade central é a curiosidade — você precisa entender, conectar ideias, conversar sobre tudo. O desafio é a dispersão: nem todo assunto precisa da sua atenção ao mesmo tempo.",
    "Can": "Você existe através do vínculo emocional. Sua identidade central é o cuidado — proteger, nutrir e criar pertencimento são parte de quem você é, não um papel que você assume. O desafio é o apego ao passado: nem toda mágoa precisa ser carregada pra sempre.",
    "Leo": "Você existe para ser vista e para brilhar com autenticidade. Sua identidade central é a generosidade criativa — você lidera com o coração, não com imposição. O desafio é a necessidade de aprovação: seu valor não depende de quem está aplaudindo.",
    "Vir": "Você existe através do cuidado com o detalhe. Sua identidade central é a melhoria contínua — você sente que sempre dá pra fazer um pouco melhor, e isso te move. O desafio é a autocrítica: a busca por perfeição pode te impedir de reconhecer o que já está bom.",
    "Lib": "Você existe através da busca por equilíbrio e beleza. Sua identidade central é a conexão — você sente sua própria existência mais clara quando está em relação com outra pessoa. O desafio é a indecisão: agradar todos os lados pode te afastar do que você mesma quer.",
    "Sco": "Você existe com intensidade que não se dilui na superfície. Sua identidade central é a profundidade — você não se contenta com versões mornas de nada. O desafio é a desconfiança: nem todo vínculo precisa ser testado até o limite pra ser real.",
    "Sag": "Você existe em expansão constante. Sua identidade central é a busca por sentido — você precisa entender o \"porquê maior\" das coisas, não só o \"como\". O desafio é a inquietação: nem todo compromisso é uma prisão, alguns são escolha.",
    "Cap": "Você existe através da construção de algo duradouro. Sua identidade central é a responsabilidade — você sente, desde jovem, que precisa erguer algo sólido com as próprias mãos. O desafio é a rigidez: descanso não é fracasso, é parte do processo.",
    "Aqu": "Você existe fora do padrão esperado. Sua identidade central é a originalidade — você vê o mundo de um jeito que poucos veem, e isso é seu maior ativo, não um defeito a corrigir. O desafio é o distanciamento emocional: conectar de verdade exige se permitir vulnerável.",
    "Pis": "Você existe através da sensibilidade que absorve tudo ao redor. Sua identidade central é a compaixão — você sente o mundo, literalmente, antes de entendê-lo com a razão. O desafio é a diluição de limites: nem toda dor que você sente é sua para resolver.",
}

LUA = {
    "Ari": "Por dentro, suas emoções chegam rápido e exigem ação imediata. Você processa sentimento fazendo, não ficando parada pensando. Precisa aprender que nem toda emoção forte exige resposta instantânea.",
    "Tau": "Por dentro, você busca estabilidade emocional acima de tudo. Sentir-se segura é tão importante quanto qualquer conquista externa. Precisa de tempo para se acalmar — pressioná-la a decidir rápido só aumenta a resistência interna.",
    "Gem": "Por dentro, você processa emoção conversando, escrevendo, verbalizando. Sentimentos guardados em silêncio pesam mais do que deveriam. Precisa de espaço para \"pensar em voz alta\" sem ser julgada por isso.",
    "Can": "Por dentro, você sente tudo em camadas profundas, e memórias antigas ainda têm peso emocional real hoje. Lar, família e raízes são pilares da sua segurança interior. Precisa aprender a se nutrir emocionalmente sem depender só dos outros pra isso.",
    "Leo": "Por dentro, você precisa se sentir vista e valorizada para se sentir emocionalmente segura. Não é vaidade, é necessidade real de reconhecimento afetivo. Precisa aprender a se validar internamente, sem depender só do olhar externo.",
    "Vir": "Por dentro, você processa emoção analisando, organizando, encontrando uma solução prática. Sentir sem \"resolver\" é desconfortável para você. Precisa permitir que algumas emoções simplesmente existam, sem precisar de solução imediata.",
    "Lib": "Por dentro, você busca harmonia emocional e evita conflito a qualquer custo. Desequilíbrio nas relações te desestabiliza mais do que você admite. Precisa aprender que discordância não é o mesmo que rompimento.",
    "Sco": "Por dentro, suas emoções são intensas, profundas e raramente superficiais. Você sente tudo em grande escala, mesmo quando não demonstra por fora. Precisa de confiança real para se abrir — mas também precisa permitir que isso aconteça, em vez de testar demais.",
    "Sag": "Por dentro, você precisa de liberdade emocional — sentir-se presa a uma rotina ou expectativa rígida sufoca seu interior. Otimismo é seu mecanismo natural de proteção. Precisa aprender que sentir tristeza também é seguro, não é fraqueza.",
    "Cap": "Por dentro, você controla suas emoções com disciplina, às vezes reprimindo o que sente para \"se manter firme\". Vulnerabilidade parece, para você, um risco. Precisa aprender que mostrar fragilidade não diminui sua força.",
    "Aqu": "Por dentro, você observa suas próprias emoções com certa distância racional, como se as analisasse de fora. Conexão emocional verdadeira exige esforço consciente de sua parte. Precisa permitir que o coração participe, não só a mente.",
    "Pis": "Por dentro, você absorve as emoções de quem está ao redor, às vezes sem conseguir diferenciar o que é seu do que é do outro. Sua sensibilidade é um dom, mas também uma vulnerabilidade. Precisa de limites claros para não se perder no sentimento alheio.",
}

ASCENDENTE = {
    "Ari": "Você chega com energia direta e decidida — as pessoas sentem sua presença antes mesmo de você falar. Isso transmite confiança, mas pode parecer abrupto para quem prefere ritmo mais suave.",
    "Tau": "Você chega com presença calma e firme — as pessoas sentem que podem confiar em você rapidamente. Isso transmite segurança, mas pode parecer parada ou reservada para quem espera mais expressividade inicial.",
    "Gem": "Você chega com leveza e curiosidade — as pessoas se sentem convidadas a conversar com você facilmente. Isso transmite acessibilidade, mas pode parecer dispersão para quem busca profundidade imediata.",
    "Can": "Você chega com sensibilidade acolhedora — as pessoas sentem que podem se abrir com você desde o início. Isso transmite empatia, mas pode parecer reservada até que a confiança se estabeleça.",
    "Leo": "Você chega com brilho natural — as pessoas notam sua presença mesmo sem você tentar chamar atenção. Isso transmite carisma, mas pode parecer intensa para quem prefere discrição.",
    "Vir": "Você chega com discrição observadora — as pessoas sentem que você presta atenção em detalhes que outros ignoram. Isso transmite competência, mas pode parecer crítica antes de mostrarem sua gentileza.",
    "Lib": "Você chega com charme e diplomacia — as pessoas se sentem à vontade perto de você quase instantaneamente. Isso transmite simpatia, mas pode parecer indecisão para quem busca posicionamento direto.",
    "Sco": "Você chega com intensidade magnética — as pessoas sentem que há mais profundidade em você do que aparenta. Isso transmite poder pessoal, mas pode parecer intimidante até que mostrem sua vulnerabilidade.",
    "Sag": "Você chega com entusiasmo expansivo — as pessoas sentem energia de possibilidade ao seu redor. Isso transmite otimismo, mas pode parecer inconstante para quem busca previsibilidade.",
    "Cap": "Você chega com seriedade e domínio — as pessoas sentem, de cara, que você tem controle da situação. Isso transmite autoridade, mas pode parecer fria até que mostrem o lado mais acessível.",
    "Aqu": "Você chega de um jeito que não segue padrão — as pessoas sentem que você é diferente, original. Isso transmite autenticidade, mas pode parecer distante para quem busca conexão emocional imediata.",
    "Pis": "Você chega com suavidade quase etérea — as pessoas sentem uma sensibilidade especial vindo de você. Isso transmite empatia, mas pode parecer dispersa ou difícil de \"definir\" para quem busca clareza objetiva.",
}

CASA_2 = {
    "Ari": "Seu dinheiro flui melhor quando você assume a liderança ou inicia algo novo. Talentos para gerar renda: coragem para arriscar, capacidade de agir rápido onde outros hesitam. Cuidado com decisões financeiras por impulso — velocidade não é sempre a mesma coisa que direção certa.",
    "Tau": "Seu dinheiro flui melhor através da constância e de algo que você possa construir com o tempo. Talentos para gerar renda: persistência, bom gosto, capacidade de transformar recursos em conforto e qualidade. Cuidado com apego excessivo à segurança — ele pode te impedir de aceitar oportunidades novas.",
    "Gem": "Seu dinheiro flui melhor através da comunicação, de vender ideias ou conectar pessoas. Talentos para gerar renda: versatilidade, facilidade de aprender rápido novas áreas, networking natural. Cuidado com dispersão financeira — múltiplas fontes de renda exigem organização, não só entusiasmo.",
    "Can": "Seu dinheiro flui melhor através do cuidado com pessoas ou de negócios ligados a lar, família, alimentação ou bem-estar emocional. Talentos para gerar renda: intuição para o que as pessoas precisam, capacidade de criar conexão genuína. Cuidado com misturar dinheiro e emoção — decisões financeiras tomadas no calor do sentimento raramente são as melhores.",
    "Leo": "Seu dinheiro flui melhor quando você está em destaque, liderando ou criando algo com sua marca pessoal. Talentos para gerar renda: carisma, capacidade de inspirar confiança, presença que atrai oportunidades. Cuidado com gastos ligados à necessidade de status — nem todo investimento em imagem traz retorno real.",
    "Vir": "Seu dinheiro flui melhor através de trabalho detalhado, organizado, ou que ajude outros a melhorar algo. Talentos para gerar renda: precisão, capacidade analítica, talento para otimizar processos. Cuidado com perfeccionismo que trava o lançamento — \"bom o suficiente\" às vezes já é hora de cobrar.",
    "Lib": "Seu dinheiro flui melhor através de parcerias, estética ou negócios que envolvam beleza e relacionamento. Talentos para gerar renda: senso estético refinado, diplomacia em negociações, facilidade de criar parcerias vantajosas. Cuidado com dificuldade de cobrar o valor justo — agradar não pode custar sua margem.",
    "Sco": "Seu dinheiro flui melhor através de transformação, temas profundos ou de confiança íntima com o cliente. Talentos para gerar renda: capacidade de lidar com crise e reinvenção, intensidade que gera resultados onde outros desistem. Cuidado com fases de altos e baixos financeiros — construir reserva é proteção, não desconfiança do futuro.",
    "Sag": "Seu dinheiro flui melhor através de ensino, viagens, ou negócios que expandam horizontes. Talentos para gerar renda: visão de oportunidades amplas, capacidade de inspirar com entusiasmo genuíno. Cuidado com otimismo financeiro exagerado — nem todo projeto grande precisa de investimento grande imediato.",
    "Cap": "Seu dinheiro flui melhor através de estrutura, longo prazo e construção de autoridade em uma área. Talentos para gerar renda: disciplina, visão estratégica, capacidade de sustentar esforço até o resultado aparecer. Cuidado com rigidez excessiva — diversificar pode ser tão seguro quanto manter um único caminho.",
    "Aqu": "Seu dinheiro flui melhor através de inovação, tecnologia ou propostas fora do padrão comum. Talentos para gerar renda: originalidade, capacidade de ver oportunidades onde outros veem só o convencional. Cuidado com desapego excessivo ao dinheiro — ele também é ferramenta pra sustentar suas ideias.",
    "Pis": "Seu dinheiro flui melhor através de criatividade, espiritualidade ou cuidado emocional com outras pessoas. Talentos para gerar renda: sensibilidade artística, intuição para o que vai tocar emocionalmente o público. Cuidado com dificuldade de precificar o próprio trabalho — sensibilidade tem valor financeiro real, não é \"só dom\".",
}

CASA_9 = {
    "Ari": "Sua busca de sentido se expressa através da ação direta — você entende o mundo testando, vivendo, se arriscando, não só lendo sobre ele. Seu propósito ganha força quando você pioneira algo, mesmo que isso assuste no início.",
    "Tau": "Sua busca de sentido se expressa através da experiência concreta e sensorial — você entende profundamente o que vive de verdade, não só o que é teoria. Seu propósito ganha força quando se conecta a algo que você possa construir com consistência ao longo da vida.",
    "Gem": "Sua busca de sentido se expressa através do aprendizado constante e da troca de ideias. Você entende o mundo conversando, lendo, conectando diferentes perspectivas. Seu propósito ganha força quando você compartilha o que aprende, não guarda só pra si.",
    "Can": "Sua busca de sentido se expressa através da conexão com raízes, ancestralidade e cuidado emocional. Você entende o mundo sentindo, não só racionalizando. Seu propósito ganha força quando cura algo do próprio passado e usa isso para guiar outras pessoas.",
    "Leo": "Sua busca de sentido se expressa através da expressão criativa e da inspiração que gera nos outros. Você entende o mundo vivendo com intensidade e autenticidade. Seu propósito ganha força quando ensina pelo exemplo, não apenas pelo discurso.",
    "Vir": "Sua busca de sentido se expressa através do serviço prático e da melhoria contínua. Você entende o mundo analisando o que funciona e o que pode ser refinado. Seu propósito ganha força quando ajuda outros a organizarem o próprio caos interno ou externo.",
    "Lib": "Sua busca de sentido se expressa através da harmonia, da justiça e da beleza nas relações. Você entende o mundo observando o que conecta as pessoas. Seu propósito ganha força quando media, ensina ou cria pontes entre visões diferentes.",
    "Sco": "Sua busca de sentido se expressa através da investigação do que está oculto — você não se contenta com respostas superficiais sobre a vida. Seu propósito ganha força quando atravessa as próprias sombras e usa essa travessia para guiar outras pessoas em transformação.",
    "Sag": "Sua busca de sentido se expressa através da filosofia, da fé e da expansão de horizontes — esse é, literalmente, o seu signo natural nessa casa, então esse tema é central na sua vida. Seu propósito ganha força quando ensina, viaja ou compartilha uma visão de mundo mais ampla.",
    "Cap": "Sua busca de sentido se expressa através da construção de autoridade reconhecida em algo que você acredita profundamente. Você entende o mundo estruturando conhecimento em algo sólido e aplicável. Seu propósito ganha força quando se torna referência confiável em sua área de atuação.",
    "Aqu": "Sua busca de sentido se expressa através de ideias que rompem padrões e beneficiam o coletivo. Você entende o mundo questionando o que está estabelecido. Seu propósito ganha força quando cria algo inovador que ajuda mais gente do que só seu círculo próximo.",
    "Pis": "Sua busca de sentido se expressa através da espiritualidade intuitiva e da compaixão universal. Você entende o mundo sentindo conexões que vão além do racional. Seu propósito ganha força quando transforma sua sensibilidade em uma ponte de cura para os outros.",
}


def gerar_bloco_astrologia(nome: str, ano: int, mes: int, dia: int,
                             hora: int, minuto: int, cidade: str, nacao: str = "BR") -> dict:
    """
    Função principal: recebe os dados de nascimento da cliente e devolve
    o bloco completo de astrologia (Sol, Lua, Ascendente, Casa 2, Casa 9)
    já com os textos certos da biblioteca.

    IMPORTANTE SOBRE O PARÂMETRO 'cidade':
    - Use o nome em formato simples, SEM acento e SEM "do/de/dos" no meio
      (ex: use "Sao Goncalo", não "São Gonçalo" e não "São Gonçalo do Amarante")
    - Se a cidade tiver nome comum a várias no Brasil, o resultado pode ficar
      ambíguo. Nesse caso, é mais seguro usar latitude/longitude diretas
      (ver função alternativa 'gerar_bloco_astrologia_com_coordenadas' abaixo).
    """
    pessoa = AstrologicalSubject(
        name=nome,
        year=ano, month=mes, day=dia,
        hour=hora, minute=minuto,
        city=cidade, nation=nacao
    )

    sol_signo = pessoa.sun["sign"]
    lua_signo = pessoa.moon["sign"]
    asc_signo = pessoa.first_house["sign"]
    casa2_signo = pessoa.second_house["sign"]
    casa9_signo = pessoa.ninth_house["sign"]

    return {
        "sol_signo": sol_signo,
        "sol_texto": SOL.get(sol_signo, "Texto não encontrado para este signo."),
        "lua_signo": lua_signo,
        "lua_texto": LUA.get(lua_signo, "Texto não encontrado para este signo."),
        "ascendente_signo": asc_signo,
        "ascendente_texto": ASCENDENTE.get(asc_signo, "Texto não encontrado para este signo."),
        "casa2_signo": casa2_signo,
        "casa2_texto": CASA_2.get(casa2_signo, "Texto não encontrado para este signo."),
        "casa9_signo": casa9_signo,
        "casa9_texto": CASA_9.get(casa9_signo, "Texto não encontrado para este signo."),
    }


def gerar_bloco_astrologia_com_coordenadas(nome: str, ano: int, mes: int, dia: int,
                                              hora: int, minuto: int,
                                              latitude: float, longitude: float,
                                              fuso_horario: str = "America/Sao_Paulo") -> dict:
    """
    VERSÃO ALTERNATIVA, MAIS PRECISA: usa latitude/longitude diretas
    em vez do nome da cidade. Use esta função se a busca por nome de
    cidade não estiver dando resultado confiável.

    Como achar sua latitude/longitude: pesquise no Google
    "latitude longitude [nome da sua cidade]" e copie os números.

    Exemplo de uso para São Gonçalo, RJ:
        gerar_bloco_astrologia_com_coordenadas(
            nome="Lohane", ano=1985, mes=8, dia=17,
            hora=SUA_HORA, minuto=SEU_MINUTO,
            latitude=-22.8268, longitude=-43.0634,
            fuso_horario="America/Sao_Paulo"
        )
    """
    pessoa = AstrologicalSubject(
        name=nome,
        year=ano, month=mes, day=dia,
        hour=hora, minute=minuto,
        lat=latitude, lng=longitude,
        tz_str=fuso_horario,
        city="Custom"
    )

    sol_signo = pessoa.sun["sign"]
    lua_signo = pessoa.moon["sign"]
    asc_signo = pessoa.first_house["sign"]
    casa2_signo = pessoa.second_house["sign"]
    casa9_signo = pessoa.ninth_house["sign"]

    return {
        "sol_signo": sol_signo,
        "sol_texto": SOL.get(sol_signo, "Texto não encontrado para este signo."),
        "lua_signo": lua_signo,
        "lua_texto": LUA.get(lua_signo, "Texto não encontrado para este signo."),
        "ascendente_signo": asc_signo,
        "ascendente_texto": ASCENDENTE.get(asc_signo, "Texto não encontrado para este signo."),
        "casa2_signo": casa2_signo,
        "casa2_texto": CASA_2.get(casa2_signo, "Texto não encontrado para este signo."),
        "casa9_signo": casa9_signo,
        "casa9_texto": CASA_9.get(casa9_signo, "Texto não encontrado para este signo."),
    }


# ---------------------------------------------------------
# TESTE COM OS DADOS DA PRÓPRIA LOH
# Rode esta parte no Google Colab para validar o resultado
# ---------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("TESTE DO MOTOR DE ASTROLOGIA — dados da Loh")
    print("=" * 60)
    print("\n⚠️ Preencha abaixo a HORA e CIDADE exatas de nascimento da Loh")
    print("   antes de rodar (estão como exemplo/placeholder):\n")

    print("\n⚠️ Usando coordenadas exatas de São Gonçalo, RJ (mais confiável")
    print("   do que buscar pelo nome da cidade)\n")

    resultado = gerar_bloco_astrologia_com_coordenadas(
        nome="Lohane",
        ano=1985, mes=8, dia=17,
        hora=12, minuto=0,                  # <-- SUBSTITUA pela hora real de nascimento
        latitude=-22.8269, longitude=-43.0539,  # São Gonçalo, RJ
        fuso_horario="America/Sao_Paulo"
    )

    print(f"☀️  Sol em {resultado['sol_signo']}")
    print(f"   {resultado['sol_texto']}\n")
    print(f"🌙 Lua em {resultado['lua_signo']}")
    print(f"   {resultado['lua_texto']}\n")
    print(f"⬆️  Ascendente em {resultado['ascendente_signo']}")
    print(f"   {resultado['ascendente_texto']}\n")
    print(f"💰 Casa 2 em {resultado['casa2_signo']}")
    print(f"   {resultado['casa2_texto']}\n")
    print(f"🧭 Casa 9 em {resultado['casa9_signo']}")
    print(f"   {resultado['casa9_texto']}\n")

    print("=" * 60)
    print("Esperado (do e-book original): Sol Leão, Lua Câncer, Ascendente Libra")
    print("Casa 2 em Escorpião, Casa 9 em Gêmeos")
    print("=" * 60)
