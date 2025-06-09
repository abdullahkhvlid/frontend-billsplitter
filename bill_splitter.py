import streamlit as st

st.title("💸 Bill Splitter App")

# Input: Total bill
bill = st.number_input("Enter total bill amount", min_value=0, step=1)

# Input: Number of people
num_people = st.number_input("How many people are paying?", min_value=1, step=1)

userdict = {}

# Input: Names and how much each paid
for i in range(int(num_people)):
    name = st.text_input(f"Name of person #{i+1}", key=f"name{i}")
    amount = st.number_input(
        f"Amount paid by {name if name else 'person'}",
        min_value=0,
        step=1,
        key=f"amount{i}"
    )
    if name:
        userdict[name] = amount

# Button to calculate
if st.button("Split the Bill"):
    try:
        if len(userdict) == 0:
            st.error("Please enter at least one name.")
        else:
            share = bill / len(userdict)
            st.success(f"Each person's share is: {share:.2f} PKR")

            for name, paid in userdict.items():
                if paid > share:
                    st.info(f"{name} should take back {paid - share:.2f} PKR")
                elif paid < share:
                    st.warning(f"{name} should pay {share - paid:.2f} PKR more")
                else:
                    st.success(f"{name} paid exactly their share.")
    except:
        st.error("Something went wrong. Please check the inputs.")
