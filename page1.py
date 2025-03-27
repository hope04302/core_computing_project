import streamlit as st
from pyvis.network import Network
import streamlit.components.v1 as components


st.title("Page 1")

# 네트워크 객체 생성
net = Network(notebook=True)

# 노드 추가
net.add_node(1, label='Node 1')
net.add_node(2, label='Node 2')

# 엣지 추가
net.add_edge(1, 2)

# 네트워크 시각화
net.show('mygraph.html')

HtmlFile = open("test.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
components.html(source_code, height=900, width=900)