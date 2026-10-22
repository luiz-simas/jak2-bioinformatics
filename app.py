import streamlit as st
from modules.hematology_rules import HematologyAnalyzer
from modules.llama_engine import LlamaEngine
from modules.admet import LipinskiFilter

st.set_page_config(page_title="Plataforma Bioinformática JAK2", layout="wide")

st.title("🧬 Plataforma de Bioinformática & Triagem JAK2")
st.sidebar.header("Navegação")
opcao = st.sidebar.radio("Selecione o Módulo:", ["Análise Clínica (JAK2)", "Triagem Molecular (HTVS)", "Consulta Llama RAG"])

if opcao == "Análise Clínica (JAK2)":
    st.header("Triagem Clínica e Hematológica")
    col1, col2 = st.columns(2)
    with col1:
        status_jak2 = st.selectbox("Status da Mutação JAK2 V617F:", ["POSITIVO", "NEGATIVO"])
        hb = st.number_input("Hemoglobina (g/dL):", value=14.5)
        ht = st.number_input("Hematócrito (%):", value=43.0)
    with col2:
        plt = st.number_input("Plaquetas (/uL):", value=250000)
        leuco = st.number_input("Leucócitos (/uL):", value=7000)

    if st.button("Analizar Caso"):
        hemograma = {"hemoglobina": hb, "hematocrito": ht, "plaquetas": plt, "leucocitos": leuco}
        resultado = HematologyAnalyzer.evaluate_jak2(status_jak2, hemograma)
        if resultado["flag_risco"] == "ALTO":
            st.error(f"Alerta: {resultado['mutacao']}")
        else:
            st.success("Status Normal")
            
        st.subheader("Hipóteses Diagnósticas")
        for h in resultado["hipoteses"]:
            st.write(f"- {h}")
            
        st.subheader("Condutas Recomendadas")
        for c in resultado["condutas"]:
            st.write(f"- {c}")

elif opcao == "Triagem Molecular (HTVS)":
    st.header("Análise ADMET / Regra de Lipinski")
    mw = st.number_input("Massa Molecular (Da):", value=400.0)
    logp = st.number_input("LogP:", value=2.5)
    hbd = st.number_input("Doadores de Hidrogênio:", value=2)
    hba = st.number_input("Aceitadores de Hidrogênio:", value=4)
    
    if st.button("Calcular Lipinski"):
        res = LipinskiFilter.check_lipinski(mw, logp, hbd, hba)
        if res["pass_lipinski"]:
            st.success("Aprovado na Regra de Lipinski!")
        else:
            st.warning(f"Violações ({res['violations_count']}): {', '.join(res['details'])}")

elif opcao == "Consulta Llama RAG":
    st.header("Assistente Llama Local")
    prompt = st.text_area("Digite a sua pergunta sobre JAK2 ou protocolos:")
    if st.button("Consultar Llama"):
        engine = LlamaEngine()
        with st.spinner("A processar localmente..."):
            resposta = engine.generate_response(prompt, system_prompt="Você é um especialista em bioinformática e hematologia.")
            st.write(resposta)
