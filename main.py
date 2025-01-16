# from dotenv import load_dotenv
# from dotenv import load_dotenv
# import pandas as pd
# import os
# import streamlit as st
# from langchain_core.messages import AIMessage, HumanMessage
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.runnables import RunnablePassthrough
# from langchain_core.output_parsers import StrOutputParser
# from langchain_openai import ChatOpenAI

# def load_csv(file):
#     return pd.read_csv(file)

# def get_csv_prompt_chain():
#     template = """
#     You are a data analyst tasked with answering questions using only the provided data. 
#     Avoid generic explanations and base your response strictly on the data in the CSV file. 
    
#     Data Structure: {schema}
#     Data Preview: {preview}
#     User Query: {question}
    
#     Provide a concise, data-backed response.
#     """
#     prompt = ChatPromptTemplate.from_template(template)
#     llm = ChatOpenAI(model="gpt-4-0125-preview", temperature=0)  # Deterministic
#     return prompt | llm | StrOutputParser()

# def generate_response(user_query: str, df: pd.DataFrame):
#     schema = f"Columns: {', '.join(df.columns)}; Row count: {len(df)}"
#     preview = df.head(5).to_string(index=False)  # Include the first 5 rows for context
#     chain = get_csv_prompt_chain()
#     response = chain.invoke({"schema": schema, "preview": df, "question": user_query})
#     return response


# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = [
#         AIMessage(content="Hello! I can answer questions about your uploaded CSV file.")
#     ]

# load_dotenv()

# st.set_page_config(page_title="Chat with CSV")


# st.image("Jiostudios.png", caption=None, width=300)
# st.title("Chat with CSV 📊")

# csv_file = st.file_uploader("Upload a CSV file", type="csv")
# if csv_file:
#     df = load_csv(csv_file)
#     st.write("CSV loaded successfully!")

#     for message in st.session_state.chat_history:
#         if isinstance(message, AIMessage):
#             with st.chat_message("AI"):
#                 st.markdown(message.content)
#         elif isinstance(message, HumanMessage):
#             with st.chat_message("Human"):
#                 st.markdown(message.content)

#     user_query = st.chat_input("Ask a question about the CSV...")
#     if user_query:
#         st.session_state.chat_history.append(HumanMessage(content=user_query))
#         with st.chat_message("Human"):
#             st.markdown(user_query)

#         with st.chat_message("AI"):
#             with st.spinner("Processing..."):
#                 response = generate_response(user_query, df)
#             st.markdown(response)

#         st.session_state.chat_history.append(AIMessage(content=response))
# import os
# import pandas as pd
# import streamlit as st
# from dotenv import load_dotenv

# from langchain_core.messages import AIMessage, HumanMessage
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_openai import ChatOpenAI

# class CSVChatApp:
#     def __init__(self):
#         """Initialize the Streamlit application."""
#         # Load environment variables
#         load_dotenv()
        
#         # Configure Streamlit page
#         st.set_page_config(
#             page_title="CSV Chat Analyzer", 
#             page_icon="📊"
#         )
        
#         # Initialize session state for chat history
#         if "chat_history" not in st.session_state:
#             st.session_state.chat_history = [
#                 AIMessage(content="Hello! I can help you analyze your CSV file.")
#             ]
        
#         # Initialize dataframe as None
#         self.df = None
    
#     def _load_csv(self, file):
#         """
#         Load CSV file with error handling.
        
#         Args:
#             file: Uploaded Streamlit file object
        
#         Returns:
#             pandas DataFrame or None
#         """
#         try:
#             return pd.read_csv(file)
#         except Exception as e:
#             st.error(f"Error loading CSV: {e}")
#             return None
    
#     def _create_prompt_chain(self):
#         """
#         Create a LangChain prompt processing pipeline.
        
#         Returns:
#             LangChain processing chain
#         """
#         template = """
#         You are a precise data analyst tasked with answering questions using only the provided data.
        
#         Data Structure: {schema}
#         Data Preview: {preview}
        
#         User Query: {question}
        
#         Guidelines:
#         - Base your response strictly on the data
#         - Provide concise, data-backed insights
#         - Use clear and specific language
#         """
        
#         prompt = ChatPromptTemplate.from_template(template)
#         llm = ChatOpenAI(model="gpt-4-0125-preview", temperature=0)
#         return prompt | llm | StrOutputParser()
    
#     def _generate_response(self, user_query):
#         """
#         Generate AI response based on user query and CSV data.
        
#         Args:
#             user_query (str): User's question about the data
        
#         Returns:
#             str: AI-generated response
#         """
#         if self.df is None:
#             return "Please upload a CSV file first."
        
#         schema = f"Columns: {', '.join(self.df.columns)}; Rows: {len(self.df)}"
        
#         # Instead of just preview, convert entire DataFrame to string
#         full_data = self.df.to_string(index=False)
        
#         chain = self._create_prompt_chain()
        
#         try:
#             response = chain.invoke({
#                 "schema": schema, 
#                 "preview": full_data,  # Pass entire DataFrame 
#                 "question": user_query
#             })
#             return response
#         except Exception as e:
#             return f"Error generating response: {e}"
    
#     def _display_chat_history(self):
#         """Display previous chat messages."""
#         for message in st.session_state.chat_history:
#             if isinstance(message, AIMessage):
#                 with st.chat_message("AI"):
#                     st.markdown(message.content)
#             elif isinstance(message, HumanMessage):
#                 with st.chat_message("Human"):
#                     st.markdown(message.content)
    
#     def run(self):
#         """Main application runner."""
#         # Logo and Title
#         st.image("Jiostudios.png", caption=None, width=300)
#         st.title("CSV Chat Analyzer 📊")
        
#         # CSV File Upload
#         csv_file = st.file_uploader("Upload a CSV file", type="csv")
        
#         if csv_file:
#             # Load CSV
#             self.df = self._load_csv(csv_file)
            
#             if self.df is not None:
#                 st.success("CSV loaded successfully!")
#                 st.write(f"Rows: {len(self.df)}, Columns: {len(self.df.columns)}")
                
#                 # Display Chat History
#                 self._display_chat_history()
                
#                 # User Query Input
#                 user_query = st.chat_input("Ask a question about the CSV...")
                
#                 if user_query:
#                     # Update Chat History
#                     st.session_state.chat_history.append(
#                         HumanMessage(content=user_query)
#                     )
                    
#                     # Display User Query
#                     with st.chat_message("Human"):
#                         st.markdown(user_query)
                    
#                     # Process and Display Response
#                     with st.chat_message("AI"):
#                         with st.spinner("Analyzing data..."):
#                             response = self._generate_response(user_query)
#                             st.markdown(response)
                    
#                     # Save AI Response to Chat History
#                     st.session_state.chat_history.append(
#                         AIMessage(content=response)
#                     )

# def main():
#     """Application entry point."""
#     app = CSVChatApp()
#     app.run()

# if __name__ == "__main__":
#     main()

import os
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()

    # Validate OpenAI API Key
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        st.error("OpenAI API Key is not set. Please set it in your environment variables.")
        st.stop()

    # Streamlit UI Setup
    st.set_page_config(page_title="CSV Data Insights", page_icon="📊")
    st.image("Jiostudios.png", caption=None, width=300)
    st.header("CENTRE OF EXCELLENCE ")


    # File Uploader
    csv_file = st.file_uploader("Upload a CSV file", type="csv")

    if csv_file is not None:
        try:
            # Read the CSV file
            df = pd.read_csv(csv_file)

            # Initialize PandasAI with OpenAI
            llm = OpenAI()
            smart_df = SmartDataframe(df, config={"llm": llm})

            # User question input
            user_question = st.text_input("Ask a question about your data:")

            # Process query when user submits a question
            if user_question:
                with st.spinner("Analyzing your data..."):
                    try:
                        # Generate response using PandasAI
                        response = smart_df.chat(user_question)
                        
                        # Display the response
                        st.write(response)

                        # If the response involves a plot, display it
                        if os.path.exists("temp_chart.png"):
                            st.image("temp_chart.png")
                            os.remove("temp_chart.png")

                    except Exception as e:
                        st.error(f"An error occurred: {e}")

            # Optional: Display basic dataframe information
            st.subheader("Dataset Preview")
            st.dataframe(df.head())
            st.write(f"Total Rows: {len(df)}, Total Columns: {len(df.columns)}")

        except Exception as e:
            st.error(f"Error processing the CSV file: {e}")

if __name__ == "__main__":
    main()