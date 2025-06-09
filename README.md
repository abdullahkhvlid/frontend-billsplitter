Bill Splitter App
The Bill Splitter App is a simple Streamlit-based web application designed to help users easily divide a shared bill among multiple people. Users input the total bill amount and the amount each person contributed. The app calculates and displays how much each person owes or should receive based on an even split.

Features
Enter the total bill amount

Add the number of people contributing

Input each person's name and the amount they paid

Automatically calculate how much each person owes or should receive

Clean, responsive UI using Streamlit

Demo
To run the app locally:

bash
Copy
Edit
git clone https://github.com/your-username/bill-splitter-app.git
cd bill-splitter-app
pip install streamlit
streamlit run app.py
Code Overview
python
Copy
Edit
import streamlit as st

st.title("Bill Splitter App")

# Input total bill and number of people
bill = st.number_input("Enter total bill amount", min_value=0, step=1)
num_people = st.number_input("How many people are paying?", min_value=1, step=1)

userdict = {}

# Collect individual contributions
for i in range(int(num_people)):
    name = st.text_input(f"Name of person #{i+1}", key=f"name{i}")
    amount = st.number_input(f"Amount paid by {name if name else 'person'}", min_value=0, step=1, key=f"amount{i}")
    if name:
        userdict[name] = amount

# Calculate and display the result
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
Requirements
Python 3.7+

Streamlit

Install dependencies:

bash
Copy
Edit
pip install streamlit
Use Cases
Splitting dinner bills among friends

Roommate utilities cost-sharing

Any group expense where equal division is required

Project Structure
bash
Copy
Edit
bill-splitter-app/
├── app.py             # Main application script
├── README.md          # Project documentation
License
This project is licensed under the MIT License.

Contributing
Contributions are welcome. Feel free to open issues or submit pull requests.

