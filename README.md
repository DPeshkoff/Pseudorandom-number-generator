<h1 class="code-line" data-line-start=0 data-line-end=1><a id="Pseudorandom_number_generator_0"></a>Pseudorandom number generator</h1>
<p class="has-line-data" data-line-start="2" data-line-end="3">Pseudorandom number generator for generating question number for each student.</p>
<p class="has-line-data" data-line-start="4" data-line-end="5">List of dependencies (all are currently part of The Python Standard Library):</p>
<ul>
<li class="has-line-data" data-line-start="6" data-line-end="7">choice, seed from random</li>
<li class="has-line-data" data-line-start="7" data-line-end="8">sha512 from hashlib</li>
<li class="has-line-data" data-line-start="8" data-line-end="9">sys</li>
<li class="has-line-data" data-line-start="9" data-line-end="11">argparse</li>
</ul>
<h1 class="code-line" data-line-start=11 data-line-end=12><a id="Build_11"></a>Build</h1>
<ul>
<li class="has-line-data" data-line-start="13" data-line-end="15">
<p class="has-line-data" data-line-start="13" data-line-end="14">Install <a href="https://www.python.org/downloads/">Python3</a></p>
</li>
<li class="has-line-data" data-line-start="15" data-line-end="17">
<p class="has-line-data" data-line-start="15" data-line-end="16">Navigate the terminal to the directory where the script is located using the <code>$ cd</code> command.</p>
</li>
<li class="has-line-data" data-line-start="17" data-line-end="19">
<p class="has-line-data" data-line-start="17" data-line-end="18">Type <code>python prng.py</code> or <code>python3 prng.py</code> in the terminal to execute the script.</p>
</li>
<li class="has-line-data" data-line-start="19" data-line-end="21">
<p class="has-line-data" data-line-start="19" data-line-end="20">Use <code>test_input.txt</code> as test run. Type <code>python prng.py --file test_input.txt --numbilets 21 --parameter 42</code> or <code>python3 prng.py --file test_input.txt --numbilets 21 --parameter 42</code> in the terminal to execute test run.</p>
</li>
</ul>
<h1 class="code-line" data-line-start=21 data-line-end=22><a id="Configuration_21"></a>Configuration</h1>
<p class="has-line-data" data-line-start="23" data-line-end="24"><mark>All arguments are neccessary.</mark></p>
<table class="table table-striped table-bordered">
<thead>
<tr>
<th>argument</th>
<th>README</th>
</tr>
</thead>
<tbody>
<tr>
<td>‎ --file</td>
<td>text file path (ex. ‘test_input.txt’)</td>
</tr>
<tr>
<td>‎ --numbilets</td>
<td>integer number of questions (ex. ‘5’ gives 1-5 questions)</td>
</tr>
<tr>
<td>‎ --parameter</td>
<td>integer seed, used by generator (ex. ‘42’)</td>
</tr>
</tbody>
</table>
</body></html>
