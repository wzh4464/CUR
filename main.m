% matlab script

% A = rand(10,5);
A = [[1/2,1/2,0];[1/3,0,2/3];[0,1/4,3/4];[1/5,0,4/5];[0,1/6,5/6]];
[C, U, R] = svd_deim(A);

% print C: C \\ U: U \\ R: R

disp('C:'); disp(C);
disp('U:'); disp(U);
disp('R:'); disp(R);
