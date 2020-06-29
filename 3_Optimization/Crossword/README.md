<h1 id="crossword">Crossword</h1>
<div class="highlighter-rouge"><div class="highlight"><pre class="highlight"><code>$ python generate.py data/structure1.txt data/words1.txt output.png
██████████████
███████M████R█
█INTELLIGENCE█
█N█████N████S█
█F██LOGIC███O█
█E█████M████L█
█R███SEARCH█V█
███████X████E█
██████████████
</code></pre></div></div>

<p>
<div>
<img src="https://github.com/divypandya/CS-50-AI-Projects/blob/master/3_Optimization/Crossword/output.png" width="500"/>
</div>
</p>

<h2 id="background">Background</h2>

<p>Given the structure of a crossword puzzle (i.e., which squares of the grid are meant to be filled in with a letter), and a list of words to use,
the problem becomes one of choosing which words should go in each vertical or horizontal sequence of squares. We can model this sort of problem 
as a constraint satisfaction problem. 
Each sequence of squares is one variable, for which we need to decide on its value (which word in the domain of possible words will fill in that sequence). 
</p>
