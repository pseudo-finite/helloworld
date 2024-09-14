import streamlit as st

st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')


st.latex(r'''
\begin{equation}
\begin{array}{|clll}
& 0 \leq p_t \leq 1 &(\forall t \in T) \cr 
& \sum_{t\in T}p_{t} = 1 &\cr
& p_{\mathrm{min}(T)} = 0 &\cr 
& p_{\mathrm{max}(T)} = 0 &\cr 
& p_{t} \leq p_{t+1} & (\forall t \in T,~ t+1\leq t_0)\cr
& p_{t} \geq p_{t+1} & (\forall t \in T,~ t_0 \leq t,~ t< \mathrm{max}(T))\cr
\end{array}
\end{equation}
     ''')