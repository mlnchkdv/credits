# import objects, variables and functions from .ipynb file
import import_ipynb
from nstk import *

# connect to db
conn = create_connection(database)

# web app
import streamlit as st



# get data frames from DB
users = pd.read_sql(sql_select_users_table, conn)
credits = pd.read_sql(sql_select_credits_table, conn)
contracts = pd.read_sql(sql_select_contracts_table, conn)




st.write("### Editable:")
# .set_index('id')
edited_users = st.experimental_data_editor(users, num_rows="dynamic")

if st.button('Update', on_click=None):
    st.success('Data updated!', icon="✅")
    st.dataframe(edited_users)
    
    
    index_list = users.index.tolist()
    deleted_index_list = [x for x in edited_users.index.tolist() if x not in index_list]
    added_index_list = [x for x in index_list if x not in edited_users.index.tolist()]
    
    # добавить нехватающие и убрать лишние строки, после чего сравнить
    # edited_users_for_compare = edited_users
    # if len(deleted_index_list) > 0:
    #     edited_users_for_compare
    # if len(added_index_list) > 0:
        
        
    # edited_index_list = users.compare(edited_users).index.tolist()
    
    
    print(index_list, deleted_index_list, added_index_list)
    