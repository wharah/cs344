% Questions

% Exercise 1.4

    % Butch is a killer
    killer(butch).
    % Mia and Marsellus are married
    married(mia, marsellus).
    % Zed is dead
    dead(zed).
    % Marsellus kills everyone who gives Mia a foot massage
    kills(marsellus, X):- footmassage(X, mia).
    % Mia loves everyone who is a good dancer
    loves(mia, X):- gooddancer(X).
    % Jules eats anything that is nutritious or tasty
    eats(jules, X):- nutritious(X); tasty(X).

    % to say X is a Y, write Y(X). this is a fact.
    % to say a rule that someone does something to something else, write verb(person, other).
    % to say X and Z are Y, write Y(X, Z). this is also a fact.
    % to say two rules that are joined together write :- and use X to connect the two.
    % the prolog syntax for "or" is ";"

% Exercise 1.5

    wizard(ron).
    hasWand(harry).
    quidditchPlayer(harry).
    wizard(X):-  hasBroom(X),  hasWand(X).
    hasBroom(X):-  quidditchPlayer(X).

    % wizard(ron). -> yes because this is a fact that we are given
    % witch(ron). -> no because there is no information about witches in this knowledge base
    % wizard(hermione). -> no because we are not told that hermione is a wizard
    % witch(hermione). -> no because there is still no information about witches in this knowledge base
    % wizard(harry). -> yes, because we're told that that harry has a wand and a broom (from him being a quidditch
        % player). even though it's not expressly stated, prolog can come to the conclusion that harry is a wizard
        % based on the facts and rules it is given.
    % wizard(Y). -> Y = ron, because we are given the fact that ron is a wizard
    % witch(Y). -> no because there are no facts starting with the symbol witch

% b) Modus Ponens: P implies Q and P is asserted to be true, therefore Q mut be true. Prolog does implement this. We
   % see this in the example with wizard(harry) because it's not explicitely given to us that harry is a wizard but
   % with the rules given it is implied that harry is a wizard.

% c) A horn clause can represent complete ideas of predicates and their subjects. Propositional logic would require
   % multiple different labels with no explicit relations between them. Propositional logic is better for just saying
   % if things are true or false bceause it's more concise.

% d) Prolog distinguishes between TELL and ASK by representing TELL with facts and ASK with rules.
