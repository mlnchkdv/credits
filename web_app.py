# import objects, variables and functions from .ipynb file
import import_ipynb
from krl import *

# connect to db
conn = create_connection(db_file)

# web app
import streamlit as st



# get data frames from DB
clients = pd.read_sql(sql_select_clients_table, conn)
services = pd.read_sql(sql_select_services_table, conn)
deals = pd.read_sql(sql_select_deals_table, conn)

deals_info = pd.merge(deals, clients[['id', 'name','surname','patronumic','gender','visit_countener','regular_client']], how='left', left_on='client_id', right_on = 'id')
deals_info = deals_info.drop(columns=['id_y'])


deals_info = pd.merge(deals_info, services[['id', 'name','cost','gender']], how='left', left_on='service_id', right_on = 'id')
deals_info = deals_info.drop(columns=['id'])
deals_info = deals_info.rename(columns={"id_x": "id", "name_x": "name_client", "name_y": "name_service"})


#st.write("### Editable:")
# .set_index('id')
#edited_users = st.experimental_data_editor(users, num_rows="dynamic")

tab1, tab2, tab3 = st.tabs(["Clients", "Services", "Deals"])

with tab1:
   st.header("Clients")
   st.write("### Editable:")
   edited_clients = st.experimental_data_editor(clients, num_rows="dynamic")
   
   if st.button('Update clients', on_click=None):
       st.success('Data updated!', icon="✅")
       st.dataframe(edited_clients)
       
       edited_clients.to_sql('clients', conn, if_exists='replace', index=False)
       
       
       #index_list = users.index.tolist()
       #deleted_index_list = [x for x in edited_users.index.tolist() if x not in index_list]
       #added_index_list = [x for x in index_list if x not in edited_users.index.tolist()]
       
       # добавить нехватающие и убрать лишние строки, после чего сравнить
       # edited_users_for_compare = edited_users
       # if len(deleted_index_list) > 0:
       #     edited_users_for_compare
       # if len(added_index_list) > 0:
           
           
       # edited_index_list = users.compare(edited_users).index.tolist()
       
       
       #print(index_list, deleted_index_list, added_index_list)

with tab2:
   st.header("Services")
   st.write("### Editable:")
   edited_services = st.experimental_data_editor(services, num_rows="dynamic")
   
   if st.button('Update services', on_click=None):
       st.success('Data updated!', icon="✅")
       st.dataframe(edited_services)
       
       edited_services.to_sql('services', conn, if_exists='replace', index=False)
       

with tab3:
    st.header("Deals")
    st.write("### Editable:")
    edited_deals = st.experimental_data_editor(deals, num_rows="dynamic")
   
    if st.button('Update deals', on_click=None):
           st.success('Data updated!', icon="✅")
           st.dataframe(edited_deals)
           
           edited_deals.to_sql('deals', conn, if_exists='replace', index=False)
           
           

    # =============================================================================
    # clients_index_list = clients.index.tolist()
    # added_index_list = [x for x in edited_clients.index.tolist() if x not in clients_index_list]
    # deleted_index_list = [x for x in clients_index_list if x not in edited_clients.index.tolist()]
    # =============================================================================

    # # добавить нехватающие и убрать лишние строки, после чего сравнить
    # edited_users_for_compare_list = edited_users.index.values.tolist()

    # if len(deleted_index_list) > 0:
    #     for i in deleted_index_list:
    #         edited_users_for_compare_list.append(i)
    # if len(added_index_list) > 0:
    #     for i in deleted_index_list:
    #         del edited_users_for_compare_list[i]

    # print(edited_users_for_compare_list)

    # edited_users_for_compare = users.loc[edited_users_for_compare_list]
    # edited_index_list = users.compare(edited_users_for_compare).index.tolist()

    # print(edited_index_list)

# =============================================================================
# merged = clients.merge(edited_clients, how='left', indicator=True)
# 
# def has_changes(row):
#         return row['_merge'] == 'right_only' or row['_merge'] == 'left_only' or not all(row['_merge'])
# 
#         merged['has_changes'] = merged.apply(has_changes, axis=1)
# 
#         edited_index_list = merged[merged['has_changes'] == True].index.tolist()
#         edited_index_list = [
#         x for x in edited_index_list if x not in deleted_index_list]
# 
#     # print(edited_index_list, deleted_index_list, added_index_list)
#     
# 
#     # get id from index
#         added_id_list = edited_clients.loc[added_index_list]['id'].tolist()
#         deleted_id_list = users.loc[deleted_index_list]['id'].tolist()
#         edited_id_list = edited_clients.loc[edited_index_list]['id'].tolist()
#     
#     # to int list
#         added_id_list = list(map(int, added_id_list))
#         deleted_id_list = list(map(int, deleted_id_list))
#         edited_id_list = list(map(int, edited_id_list))
#     
# 
#         print(edited_id_list, deleted_id_list, added_id_list)
# 
#         for i in deleted_id_list:
#             Client(get_by_id=i).delete()
# 
#         for i in added_id_list:
#             new_client = edited_clients[edited_clients['id'] == i]
#             Client(name=new_client.name,
#              surname=new_client.surname,
#              patronumic=new_client.patronumic,
#              gender=new_client.gender,
#              visit_countener=new_client.visit_countener,
#              regular_client=new_client.regular_client)
# =============================================================================


    