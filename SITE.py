import streamlit as st
import os
from PIL import Image
from datetime import datetime

# Título do aplicativo 
st.title("F1F4 12 Min | GT LEAGUE") 
st.markdown(""" <h4>Análises dos próximos Jogos na casa de apostas <span style='color:green'>Bet365.com</span></h4>
             """, unsafe_allow_html=True)

# Link clicável usando markdown 
st.markdown("[Link para os Jogos](https://www.bet365.com/?#/AC/B1/C1/D1002/E71755867/G40/)") 

# Caminho para a pasta com as imagens 
pasta_imagens = 'C:/Users/tofau/OneDrive/Documentos/sitef1f4/' 
# Listar os arquivos na pasta 
arquivos_imagens = os.listdir(pasta_imagens) 
# Iterar sobre os arquivos e exibir as imagens 

for imagem in arquivos_imagens: 
    if imagem.endswith('.jpg') or imagem.endswith('.png'): 
        # Carregar e exibir as fotos 
        caminho_imagem = os.path.join(pasta_imagens, imagem) 
        foto = Image.open(caminho_imagem) 
        st.image(foto, use_container_width=True)

# Adicionar rodapé 
current_year = datetime.now().year 
st.markdown(f"""
<hr style="border-top: 1px solid #ccc;" />
            
<div style="text-align: left;">
     <p>&copy; {current_year} <strong>Criative Flow</strong>. Todos os direitos reservados.</p> 
</div> """, unsafe_allow_html=True)