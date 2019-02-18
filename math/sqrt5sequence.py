'''
Define a sequence $\{a_n\}_{n=1}^\infty$ by setting $a_1=1$, and defining $a_{n+1}=\sqrt{5a_n}$ for each $n$.  
\begin{enumerate}
\item (2 points) Show that $0\leq a_n\leq 5$ for all $n$.
\item (2 points) Show that $\{a_n\}$ is increasing.
\item (3 points) It follows from (a) and (b) and Theorem 1.16 that $\{a_n\}$ is convergent.  Find the limit, and prove that $\{a_n\}$ converges to it.
\end{enumerate}
'''
import math

x = math.sqrt(5)
for i in range(1,20):
    print(x)
    x = math.sqrt(5*x)
