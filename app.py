# ✅ app.py
import streamlit as st
import json
import base64
import os
from dotenv import load_dotenv
from backend.pdf_loader import extract_text_by_page
from backend.web_loader import extract_text_from_url
from backend.vector_store import create_vector_store
from backend.qa_chain import get_qa_chain  # ✅ Removed 'agent'

load_dotenv()
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"  # ✅ Prevent torch watcher crash

st.set_page_config(page_title="AI Knowledge Bot", page_icon="📚")
st.title("📚 AI Knowledge Bot")
st.write("Ask questions about a PDF or webpage using local LLM + embeddings.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

input_mode = st.radio("Choose input type:", ("PDF", "Web URL"))

text = ""
source_filename = ""
pages = []

def show_pdf(file):
    base64_pdf = base64.b64encode(file.read()).decode("utf-8")
    pdf_display = f"""<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500" type="application/pdf"></iframe>"""
    st.markdown(pdf_display, unsafe_allow_html=True)
    file.seek(0)

# Handle PDF
if input_mode == "PDF":
    uploaded_file = st.file_uploader("Upload your PDF", type="pdf")
    if uploaded_file:
        show_pdf(uploaded_file)
        pages = extract_text_by_page(uploaded_file)
        text = "\n".join([p["text"] for p in pages])
        source_filename = uploaded_file.name
        with st.spinner("Indexing document..."):
            vectorstore = create_vector_store(pages)
            qa_chain = get_qa_chain(vectorstore)

# Handle Web URL
elif input_mode == "Web URL":
    url = st.text_input("Enter a URL")
    if url:
        text = extract_text_from_url(url)
        source_filename = url
        with st.spinner("Indexing page..."):
            vectorstore = create_vector_store([{"text": text, "page": 1}])
            qa_chain = get_qa_chain(vectorstore)

# Q&A Section
if "vectorstore" in locals() and "qa_chain" in locals():
    question = st.text_input("Ask a question about the content:")
    if question:
        with st.spinner("Thinking..."):
            try:
                result = qa_chain.invoke({"query": question})  # ✅ Correct key: "query"
                answer = result["result"]
                docs = result.get("source_documents", [])
                source_pages = sorted({doc.metadata.get("page", "?") for doc in docs})
                citation_note = f"📄 **Pages:** {', '.join(map(str, source_pages))}"
                st.success(answer)
                st.markdown(citation_note)

                st.session_state.chat_history.append({
                    "source": source_filename,
                    "question": question,
                    "answer": answer,
                    "pages": list(source_pages)
                })
            except Exception as e:
                st.error(f"❌ Error while processing question: {str(e)}")

# Show chat history
if st.session_state.chat_history:
    st.subheader("🧾 Chat History")
    for idx, chat in enumerate(st.session_state.chat_history):
        st.markdown(f"**Source:** {chat['source']}")
        st.markdown(f"**Q{idx+1}:** {chat['question']}")
        st.markdown(f"**A{idx+1}:** {chat['answer']}")
        st.markdown(f"📄 Pages: {', '.join(map(str, chat['pages']))}")
        st.markdown("---")

    chat_json = json.dumps(st.session_state.chat_history, indent=2)
    st.download_button("⬇️ Download Chat Log", chat_json, file_name="chat_history.json", mime="application/json")
    
# Footer
st.markdown("""
<hr style="margin-top: 50px; margin-bottom: 10px;">
<div style='text-align: center; color: gray; font-size: small;'>
    Developed by <strong>EzioDEVio</strong>
</div>
""", unsafe_allow_html=True)
