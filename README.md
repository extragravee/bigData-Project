BigData Project
===============
The work I did during my UniMelb internship - data analytics. I analysed how each subject used the Learning management system over time, in particular what types of files were uploaded, and how deep their folders were. This was done to get an approximation of how much of a use the subject made of the online LMS tool.

This is the first time I coded in object oriented python (previously I made a game using object oriented java, and did a decent bit of data work and scripting in python, but never used python 3 in a proper object oriented way until now). Things I did are:

1. Query data from an oracle data script
1. Wrangle, regine, complete and store data efficiently in python
1. Created an object oriented system which stored details of each subject, subject instances, an activity log that recorded each thing analysed and it's details.
1. These classes also output the subject and subject instance dictionaries (written to a text file)
1. Finally I visualised all data, by individually plotting each data point on a graph. Each subject had it's graph, each point was a subject instance, and this helped us see a time series view of how subjects evolved over time.

<b> Things I learnt </b>
<hr>
<ul>
  <li>I learned how to efficiently query, store and work with big data (15M X 32). </li>
  <li>Used my knowledge of data structures to write iterative solutions to recursive problems, such as finding max depth of folders for each subject</li>
  <li>Wrote large data to files to create information reports and summaries which can be queried much easier later for other purposes</li>
  <li>Learnt more about visualising data, and how inefficient it can be to plot each indiviual data point</li>
 </ul>
 
<p>Visit <a href="https://github.com/extragravee/extraGravee/tree/master/subjectInstanceDepth/plots_SPUD">here</a> for the final resulting plots. Data points only exist while the subject existed at Uni. </p>
 
<p>All data files had to be clipped because of github file size limits. The data dictionaries and other files I created from data were approximately 800mb each.</p>



