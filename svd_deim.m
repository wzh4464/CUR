function [C, U, R] = svd_deim(A)
    [V, S, W] = svd(A, 'econ');
    p = deim(V);
    q = deim(W);
    C = A(:,q);
    R = A(p,:);
    U = C \ A / R;
end