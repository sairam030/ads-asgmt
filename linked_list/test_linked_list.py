from linkedList import *

st = Single_linked_list()

def test_empty_list():
    assert st.is_empty() == True
    assert st.get_count() == 0

def test_add_head():
    st.add_at_head(6)
    st.add_at_head(9)
    assert(st.is_member(6))
    test_print(st)  # [9, 6]

def test_add_tail():
    st.add_at_tail(8)
    st.add_at_tail(6)
    test_print(st)  # [9, 6, 8, 6]

# def test_dlt_tail():
#     d = st.delete_at_tail()
#     print("Deleted:", d)
#     test_print(st)

def test_print(s):
    print("Linked List elements:", s.display())


test_add_head()
#test_add_tail()
# test_dlt_tail()
