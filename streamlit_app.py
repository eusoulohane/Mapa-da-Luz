# -*- coding: utf-8 -*-
"""
MAPA DA LUZ - APP WEB (Streamlit)
Loh do @LuzdeLoh

Este é o arquivo principal do site. O Streamlit Community Cloud
vai rodar este arquivo e transformá-lo automaticamente em uma
página web com formulário e botão.

NOME OBRIGATÓRIO: este arquivo precisa se chamar "streamlit_app.py"
no GitHub para o deploy funcionar sem configuração extra.
"""

import streamlit as st
from cidades_brasil import CIDADES_BRASIL
from motor_numerologia import gerar_bloco_numerologia
from motor_astrologia import gerar_bloco_astrologia_com_coordenadas
from motor_design_humano import gerar_bloco_design_humano
from motor_arquetipo import gerar_arquetipo_sintese


# ---------------------------------------------------------
# CONFIGURAÇÃO VISUAL DA PÁGINA
# ---------------------------------------------------------
st.set_page_config(
    page_title="Mapa da Luz | Loh do @LuzdeLoh",
    page_icon="✨",
    layout="centered"
)

st.title("✨ Mapa da Luz")
st.caption("de Loh — Um guia personalizado para iluminar o seu mundo interior")

st.markdown("---")

# ---------------------------------------------------------
# FORMULÁRIO
# ---------------------------------------------------------
st.subheader("Preencha seus dados de nascimento")

nome_completo = st.text_input(
    "Nome completo de nascimento (como na certidão)",
    placeholder="Ex: Maria da Silva Santos"
)

col1, col2 = st.columns(2)
with col1:
    data_nascimento = st.date_input(
        "Data de nascimento",
        min_value=None,
        format="DD/MM/YYYY"
    )
with col2:
    hora_nascimento = st.time_input("Hora de nascimento (exata)")

cidade_selecionada = st.selectbox(
    "Cidade de nascimento",
    options=list(CIDADES_BRASIL.keys()),
    index=None,
    placeholder="Selecione a cidade mais próxima do seu nascimento"
)

st.caption("💡 Se sua cidade não está na lista, escolha a capital do seu estado.")

gerar = st.button("✨ Gerar meu Mapa da Luz", type="primary", use_container_width=True)

# ---------------------------------------------------------
# PROCESSAMENTO E RESULTADO
# ---------------------------------------------------------
if gerar:
    if not nome_completo or not cidade_selecionada:
        st.error("Por favor, preencha seu nome completo e selecione a cidade de nascimento.")
    else:
        with st.spinner("Consultando os astros e calculando sua energia... ✨"):
            try:
                latitude, longitude = CIDADES_BRASIL[cidade_selecionada]

                numerologia = gerar_bloco_numerologia(
                    nome_completo=nome_completo,
                    dia=data_nascimento.day,
                    mes=data_nascimento.month,
                    ano=data_nascimento.year
                )

                astrologia = gerar_bloco_astrologia_com_coordenadas(
                    nome=nome_completo,
                    ano=data_nascimento.year, mes=data_nascimento.month, dia=data_nascimento.day,
                    hora=hora_nascimento.hour, minuto=hora_nascimento.minute,
                    latitude=latitude, longitude=longitude,
                    fuso_horario="America/Sao_Paulo"
                )

                design_humano = gerar_bloco_design_humano(
                    ano=data_nascimento.year, mes=data_nascimento.month, dia=data_nascimento.day,
                    hora=hora_nascimento.hour, minuto=hora_nascimento.minute,
                    utc_offset=-3
                )

                arquetipo = gerar_arquetipo_sintese(
                    sol_signo=astrologia["sol_signo"],
                    tipo_design_humano=design_humano["tipo_original"]
                )

                # -----------------------------------------------------
                # EXIBIÇÃO DO RESULTADO
                # -----------------------------------------------------
                st.success("Seu Mapa da Luz está pronto! ✨")
                st.markdown("---")

                st.header(f"✨ Mapa da Luz de {nome_completo}")

                st.subheader(f"🌟 Seu Arquétipo: A {arquetipo['nome_arquetipo'].upper()}")
                st.write(arquetipo["texto_base"])
                st.write(arquetipo["texto_complemento"])
                st.info(f"💫 **Sua missão:** \"{arquetipo['missao_em_uma_linha']}\"")

                st.markdown("---")
                st.subheader("🔮 Análise Astrológica")

                st.markdown(f"**☀️ Sol em {astrologia['sol_signo']}**")
                st.write(astrologia["sol_texto"])

                st.markdown(f"**🌙 Lua em {astrologia['lua_signo']}**")
                st.write(astrologia["lua_texto"])

                st.markdown(f"**⬆️ Ascendente em {astrologia['ascendente_signo']}**")
                st.write(astrologia["ascendente_texto"])

                st.markdown(f"**💰 Casa 2 em {astrologia['casa2_signo']}**")
                st.write(astrologia["casa2_texto"])

                st.markdown(f"**🧭 Casa 9 em {astrologia['casa9_signo']}**")
                st.write(astrologia["casa9_texto"])

                st.markdown("---")
                st.subheader("🔢 Mapa Numerológico")

                st.markdown(f"**Número do Destino: {numerologia['numero_destino']} — {numerologia['destino']['nome']}**")
                st.write(numerologia["destino"]["texto"])

                st.markdown(f"**Número da Alma: {numerologia['numero_alma']}**")
                st.write(numerologia["alma"]["texto"])

                st.markdown(f"**Número da Personalidade: {numerologia['numero_personalidade']}**")
                st.write(numerologia["personalidade"]["texto"])

                st.markdown("---")
                st.subheader("🌀 Design Humano")

                st.markdown(f"**Tipo: {design_humano['tipo_nome']}**")
                st.write(f"Estratégia: {design_humano['estrategia']}")
                st.write(design_humano["tipo_texto"])
                st.write(f"👉 {design_humano['tipo_pratica']}")

                st.markdown(f"**Autoridade: {design_humano['autoridade_original']}**")
                st.write(design_humano["autoridade_texto"])

                st.markdown(f"**Perfil: {design_humano['perfil']}**")
                st.write(f"Linha 1: {design_humano['perfil_linha1_texto']}")
                st.write(f"Linha 2: {design_humano['perfil_linha2_texto']}")

                st.markdown("---")
                st.caption("✨ Mapa da Luz de Loh — Com carinho e presença 🌟")

            except Exception as e:
                st.error(f"Algo não saiu como esperado. Detalhe técnico: {e}")
                st.info("Se o erro persistir, confira se a data e hora foram preenchidas corretamente.")
