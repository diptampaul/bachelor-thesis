from gingerit.gingerit import GingerIt
import streamlit as st


# st.title('Grammer & Spell Checker in Python')
# text = st.text_area("Enter Text:",value = '', height = None, max_chars = None, key = None)
# parser = GingerIt()

# if st.button('Correct Sentence'):
#     if text == '':
#         st.write('Please Enter text for checking')
#     else:
#         result_dict = parser.parse(text)
#         print(result_dict)
#         st.markdown('**Corrected Sentence - **' + str(result_dict["result"]))
# else:
#     pass

text = 'My name are Diptam. and I were from Kolkta'
parser = GingerIt()
result_dict = parser.parse(text)
print(result_dict)
print(len(result_dict["corrections"]))
print('**Corrected Sentence - **' + str(result_dict["result"]))
