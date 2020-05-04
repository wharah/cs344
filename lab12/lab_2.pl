% Questions

% Exercise 2.1 - 1, 2, 8, 9, 14

    % 1.  bread = bread -> yes
    % 2.  'Bread' = bread -> no
    % 8.  food(X) = food(bread) -> X = bread
    % 9.  food(bread, X) = food(Y, sausage) -> X = sausage, Y = bread
    % 14. meal(food(bread), X) = meal(X, drink(beer)) -> no
        % if X = food(bread), then meal(food(bread), food(bread)) != meal(food(bread), drink(beer))
        % if X = drink(beer), then meal(drink(beer), drink(beer)) != meal(food(bread), drink(beer))

% Exercise 2.2

    house_elf(dobby).
    witch(hermione).
    witch('McGonagall').
    witch(rita_skeeter).
    magic(X):-  house_elf(X).
    magic(X):-  wizard(X).
    magic(X):-  witch(X).

    % magic(house_elf). -> no, house_elf isn't an atom. it's a complex term
    % wizard(harry). -> no, wizard isn't defined in the knowledge base
    % magic(wizard). -> no, wizard isn't defined in the knowledge base
    % magic('McGonagall'). -> yes, 'McGonagall' is in the knowledge base as a witch
    % magic(Hermione). -> yes, since Hermione is capitalized it's a variable

    % when unifying, prolog compares the types of objects represented by the terms in question. if they are complex,
    % they should have the same functors. it could also check if they are both atoms.

% b) Inferences does use unification in propositional logic because things can be identified together as true and then
   % be used to arrive at a larger conclusion.

% c) Prolog inferencing does not use resolution. It only makes inferences based on statements in the knowledge base.

