function p = deim(V)
    % Assume V is a matrix of size m x n

    % Initialize p as an empty vector
    p = zeros(1, size(V, 2));
    
    % Step 1: Get the first column of V
    v1 = V(:, 1);

    % Step 2: Find the index of the maximum absolute value of v1
    [~, p(1)] = max(abs(v1));

    % Step 4: Iterate over the rest of the columns in V
    for j = 2:size(V, 2)
        % Step 5: Get the j-th column of V
        vj = V(:, j);

        % Step 6: Compute c
        c = V(p(1:j-1), 1:j-1) \ vj(p(1:j-1));

        % Step 7: Compute r
        r = vj - V(:, 1:j-1)*c;

        % Step 8: Select the next interpolation point
        [~, idx] = max(abs(r));
        p(j) = idx;
    end
end
