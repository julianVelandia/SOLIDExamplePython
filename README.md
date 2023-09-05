# SOLID Examples Python

Examples of the 5 SOLID principles in Golang, for the course SOLID Principles and Hexagonal Architecture with Python and Golang

Link: https://ed.team/cursos/solid

* Brief explanation

1. The course explains the principle of single responsibility with the analogy of a car factory, which has assigned and separated roles, against an application where all the logic is performed by a single worker.

2. The course explains the principle of Open / Closed, with an analogy of a restaurant menu, which wants to expand, but with a single product (The hamburger), this extension is done by accompanying the hamburger with a combo (Which is defined as an interface that can be implemented in multiple ways)


![image](https://github.com/julianVelandia/SOLIDExamplesGo/assets/52173621/bde5925b-2093-413a-9ce4-0ef481a15db8)


3. In the course, the Liskov Substitution principle is explained through the problem of a bad abstraction, where a daughter class (Toy Duck) inherits an unexpected behavior (Nadar). Fixed, segregating this behavior to child classes

Bad abstraction


<img src="https://github.com/julianVelandia/SOLIDExamplesGo/assets/52173621/5921a398-df12-4d66-a705-614d008c13f2" alt="image" width="50%">


Improved abstraction


![image](https://github.com/julianVelandia/SOLIDExamplesGo/assets/52173621/bbd87d34-ba15-418d-84ec-cca4ca50ba9d)


4. The interface segregation principle is explained with the example of the previous principle, where intermediate interfaces are used, in order to reduce cohesion and improve code modularity.


![image](https://github.com/julianVelandia/SOLIDExamplesGo/assets/52173621/b3d4830d-bfd2-47f7-9d5f-343af5bad636)


5. The principle of Dependency Inversion is explained with the example of the previous principles, showing the injection of dependencies (Abstractions are expected and concretions are injected)


![image](https://github.com/julianVelandia/SOLIDExamplesGo/assets/52173621/b1d913eb-3eda-4f09-b217-b7a2da477d52)


