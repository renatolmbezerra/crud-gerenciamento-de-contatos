import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout="wide")

st.image("logo.png", width=200)

st.title("Gerenciamento de Contatos")


# Função auxiliar para exibir mensagens de erro detalhadas
def show_response_message(response):
    if response.status_code == 200:
        st.success("Operação realizada com sucesso!")
    else:
        try:
            data = response.json()
            if "detail" in data:
                # Se o erro for uma lista, extraia as mensagens de cada erro
                if isinstance(data["detail"], list):
                    errors = "\n".join([error["msg"] for error in data["detail"]])
                    st.error(f"Erro: {errors}")
                else:
                    # Caso contrário, mostre a mensagem de erro diretamente
                    st.error(f"Erro: {data['detail']}")
        except ValueError:
            st.error("Erro desconhecido. Não foi possível decodificar a resposta.")


# Adicionar Contato
with st.expander("Adicionar um Novo Contato"):
    with st.form("new_contact"):
        operador = st.selectbox("Operador", ["Matheus", "Lucas", "João", "Pedro", "Maria", "Ana", "José", "Carlos"])
        dataContato = st.date_input("Data do Contato")
        nomeCliente = st.text_input("Nome do Cliente")
        pessoaContato = st.text_input("Pessoa de Contato")
        formaContato1 = st.selectbox("Forma de Contato 1", ["Whatsapp", "Ligação", "Visita", "E-mail"])
        formaContato2 = st.selectbox("Forma de Contato 2", ["Whatsapp", "Ligação", "Visita", "E-mail"])
        tipoContato = st.selectbox("Tipo de Contato", ["Ativo", "Receptivo"])
        pedidoGerado = st.selectbox("Pedido Gerado", ["Sim", "Não"])
        motivoDeclino = st.selectbox("Motivo de Declínio", ["Sem demanda", "Preço", "Sem estoque", "Crédito", "Logística", "Prospecção"])
        observacao = st.text_area("Observação")
        submit_button = st.form_submit_button("Adicionar Produto")

        if submit_button:
            response = requests.post(
                "https://meu-app-backend.onrender.com/contacts/",
                json={
                    "operador": operador,
                    "dataContato": dataContato,
                    "nomeCliente": nomeCliente,
                    "pessoaContato": pessoaContato,
                    "formaContato1": formaContato1,
                    "formaContato2": formaContato2,
                    "tipoContato": tipoContato,
                    "pedidoGerado": pedidoGerado,
                    "motivoDeclino": motivoDeclino,
                    "observacao": observacao,
                },
            )
            show_response_message(response)

# Visualizar Contatos
with st.expander("Visualizar Contatos"):
    if st.button("Exibir Todos os Contatos"):
        response = requests.get("https://meu-app-backend.onrender.com/contacts/")
        if response.status_code == 200:
            contact = response.json()
            df = pd.DataFrame(contact)

            df = df[
                [
                    "id",
                    "operador",
                    "dataContato",
                    "nomeCliente",
                    "pessoaContato",
                    "formaContato1",
                    "formaContato2",
                    "tipoContato",
                    "pedidoGerado",
                    "motivoDeclino",
                    "observacao",
                    "created_at",
                ]
            ]

            # Exibe o DataFrame sem o índice
            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)

# Obter Detalhes de um Contato
with st.expander("Obter Detalhes de um Contato"):
    get_id = st.number_input("ID do Contato", min_value=1, format="%d")
    if st.button("Buscar Contato"):
        response = requests.get(f"https://meu-app-backend.onrender.com/contacts/{get_id}")
        if response.status_code == 200:
            contact = response.json()
            df = pd.DataFrame([contact])

            df = df[
                [
                    "id",
                    "operador",
                    "dataContato",
                    "nomeCliente",
                    "pessoaContato",
                    "formaContato1",
                    "formaContato2",
                    "tipoContato",
                    "pedidoGerado",
                    "motivoDeclino",
                    "observacao",
                    "created_at",
                ]
            ]

            # Exibe o DataFrame sem o índice
            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)

# Deletar Contato
with st.expander("Deletar Contato"):
    delete_id = st.number_input("ID do Contato para Deletar", min_value=1, format="%d")
    if st.button("Deletar Contato"):
        response = requests.delete(f"https://meu-app-backend.onrender.com/contacts/{delete_id}")
        show_response_message(response)

# Atualizar Contato
with st.expander("Editar Contato"):
    with st.form("update_contact"):
        update_id = st.number_input("ID do Contato", min_value=1, format="%d")
        new_operador = st.selectbox("Novo Operador", ["Matheus", "Lucas", "João", "Pedro", "Maria", "Ana", "José", "Carlos"])
        new_dataContato = st.date_input("Nova Data do Contato")
        new_nomeCliente = st.text_input("Novo Nome do Cliente")
        new_pessoaContato = st.text_input("Nova Pessoa de Contato")
        new_formaContato1 = st.selectbox("Nova Forma de Contato 1", ["Whatsapp", "Ligação", "Visita", "E-mail"])
        new_formaContato2 = st.selectbox("Nova Forma de Contato 2", ["Whatsapp", "Ligação", "Visita", "E-mail"])
        new_tipoContato = st.selectbox("Novo Tipo de Contato", ["Ativo", "Receptivo"])
        new_pedidoGerado = st.selectbox("Novo Pedido Gerado", ["Sim", "Não"])
        new_motivoDeclino = st.selectbox("Novo Motivo de Declínio", ["Sem demanda", "Preço", "Sem estoque", "Crédito", "Logística", "Prospecção"])
        new_observacao = st.text_area("Nova Observação")

        update_button = st.form_submit_button("Atualizar Contato")

        if update_button:
            update_data = {}
            if new_operador:
                update_data["operador"] = new_operador
            if new_dataContato:
                update_data["dataContato"] = new_dataContato
            if new_nomeCliente:
                update_data["nomeCliente"] = new_nomeCliente
            if new_pessoaContato:
                update_data["pessoaContato"] = new_pessoaContato
            if new_formaContato1:
                update_data["formaContato1"] = new_formaContato1
            if new_formaContato2:
                update_data["formaContato2"] = new_formaContato2
            if new_tipoContato:
                update_data["tipoContato"] = new_tipoContato
            if new_pedidoGerado:
                update_data["pedidoGerado"] = new_pedidoGerado
            if new_motivoDeclino:
                update_data["motivoDeclino"] = new_motivoDeclino
            if new_observacao:
                update_data["observacao"] = new_observacao

            if update_data:
                response = requests.put(
                    f"https://meu-app-backend.onrender.com/contacts/{update_id}", json=update_data
                )
                show_response_message(response)
            else:
                st.error("Nenhuma informação fornecida para atualização")