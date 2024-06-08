import streamlit


def emi(p, n, r):
    rr = r / 12
    nn = n * 12
    emianswer = p * rr / 100 * (1 + rr / 100) ** nn / ((1 + rr / 100) ** nn - 1)
    return emianswer


def emiadvance(p, n, r, m):
    rr = r / 12
    nn = n * 12
    repeat = (emi(p, n, r)*nn)-(emi(p, n, r)*m)
    return repeat

streamlit.sidebar.title('Loan Calculator')
magic = streamlit.sidebar.selectbox("", ("Monthly Payment", "Outstanding Balance",))
if magic == 'Monthly Payment':
    streamlit.title('Loan Monthly Payment Calculator')
    prince = streamlit.slider('Principal Amount($)', 1000, 1000000)
    tenure = streamlit.slider('Tenure(years)', 1, 30)
    roi = streamlit.slider('rate of interest%', 1.00, 15.00)
    button = streamlit.button('Calculate')

    if button:
        streamlit.write('This much per month ',emi(prince, tenure, roi))
elif magic == 'Outstanding Balance':
    streamlit.title('Loan Outstanding Balance Calculator')
    prince = streamlit.slider('Principal Amount($)', 1000, 1000000)
    tenure = streamlit.slider('Tenure(years)', 1, 30)
    roi = streamlit.slider('rate of interest%', 1.00, 15.00)
    month = streamlit.slider('Months', 1, (tenure * 12))
    button = streamlit.button('Calculate')

    if button:
        streamlit.write('This much is left ',emiadvance(prince, tenure, roi, month))
