% Questions

% a)  i) Exercise 3.2

         directlyIn(katarina, olga).
         directlyIn(olga, natasha).
         directlyIn(natasha, irina).
         in(X, Y) :- directlyIn(X, Y).               % Y is in X
         in(X, Y) :- directlyIn(Z, Y), in(X, Z).     % if Y is in Z, Z is in X

%    ii) Exercise 4.5

         tran(eins,one).
         tran(zwei,two).
         tran(drei,three).
         tran(vier,four).
         tran(fuenf,five).
         tran(sechs,six).
         tran(sieben,seven).
         tran(acht,eight).
         tran(neun,nine).

         listtran([], []).
         listtran([G|TG], [E|TE]) :- tran(G, E), listtran(TG, TE).

% b) Prolog does implement a partial version of modus ponens. It uses universal instantiation but doesn't use
  %  existential instantiation. This s because Prolog doesn't handle uncertainty well and uncertainty is assigned to
  %  every variable with existential instantiation. It can do universal instantiation because universal instantiation
  %  doesn't deal with uncertainties.