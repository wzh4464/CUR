% matlab script

A = rand(1000,500);
[V, S, W] = svd(A, 'econ');

disp(deim(V));
