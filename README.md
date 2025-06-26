# Short Eulers formula animation
## Description
The project consists of a continuos animation of a complex plane, a unit circle, a dot which coordinates are being calculated using the Eulers formula, and the formula itself with the according values. The animation ends with a famous Roger Bacon quote about mathematics.

## Running the code
To run the program in medium quality through terminal install manim via their [official guide](https://docs.manim.community/en/stable/installation.html), go to the program's directory and enter 
```bash
manim -qm eulers-formula.py
```
or 
```bash
manim -qm eulers-formula.py EulersFormula
```
into your terminal.

You can also [run the program with docker](https://docs.manim.community/en/stable/installation/docker.html), in this case use 
```bash
docker run --rm -it -v "/full/path/to/your/directory:/manim" manimcommunity/manim manim -qm eulers-formula.py
```
