import numpy as np

def svd_deim(A):
    # Compute the SVD of A
    U, S, Vt = np.linalg.svd(A, full_matrices=False)

    # Compute the DEIM indices
    p = deim(U)
    q = deim(Vt.T)

    # Compute the reduced matrices
    C = A[:, q]
    R = A[p, :]

    # Compute the reduced system
    # U = C \ A / R
    C_dag = np.linalg.pinv(C)
    R_dag = np.linalg.pinv(R)
    U = C_dag @ A @ R_dag
    return C, U, R

def deim(V):
    # Compute the DEIM indices for the matrix V
    m, n = V.shape
    p = np.zeros(n, dtype=int)
    p[0] = np.argmax(np.abs(V[:, 0]))
    for j in range(1, min(m, n)):
        # c = np.linalg.lstsq(V[p[:j], [0: (j-1)]], V[p[:j], j, np.newaxis], rcond=None)[0]
        c = np.linalg.lstsq(V[p[:j], :j], V[p[:j], j], rcond=None)[0]
        r = V[:, j] - V[:, :j] @ c
        p[j] = np.argmax(np.abs(r))
    return p

# if main
if __name__ == "__main__":
    # A = [[1/2,1/2,0];[1/3,0,2/3];[0,1/4,3/4];[1/5,0,4/5];[0,1/6,5/6]];
    A = np.array([[1/2,1/2,0],[1/3,0,2/3],[0,1/4,3/4],[1/5,0,4/5],[0,1/6,5/6]])
    C, U, R = svd_deim(A)
    # print C,U,R pretty
    print("C = \n", C)
    print("U = \n", U)
    print("R = \n", R)
    
    # print loss
    print("Loss = ", np.linalg.norm(A - C @ U @ R))