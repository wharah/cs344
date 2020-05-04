% Burn the Witch

    % bonk
    % witches burn
    % wood burns
    % woman is made of wood
    % bridges are made of wood
    % bridges are made of stone
    % wood floats in water
    % bread, apples, small rocks, cider, gravy, cherries, mud, churches, lead, and ducks float on water
    % if she weighs the same as a duck, she is a witch

duckweight(woman).
floats(X) :- duckweight(X).
wood(X) :- floats(X).
burn(X) :- wood(X).
witch(X) :- burn(X).

witch(woman).

% the woman is indeed a witch
