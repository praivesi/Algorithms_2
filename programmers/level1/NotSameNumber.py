def solution(arr):
    st = []
    
    for a in arr:
        if not st:
            st.append(a)
            continue
       
        if st[-1] == a: continue
        st.append(a)

    return st
        