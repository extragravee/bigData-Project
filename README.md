BigData Project
===============
The work I did during my UniMelb internship - data analytics. I analysed how each subject used the Learning management system over time, in particular what types of files were uploaded, and how deep their folders were. This was done to get an approximation of how much of a use the subject made of the online LMS tool.

I learned object oriented python, and used my skills to:

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



Instructions
===============

Data being analysed is from a Blackboard LMS
Table being queried is course_contents

1. Create a default directory where you want the output to be saved (e.g., data).
1. Edit the config.sample.yaml file and save it as config.yaml
1. Please ensure that you are connected to VPN if required.
1. Run queryOracle_RawData.py to collect the data.
1. Run create_Dataframe.py to structure the data. This can be run multiple times once the data has been downloaded.
1. Paste the df_output.csv file into the 'subjectInstanceDepth' folder
1. Ensure you have the valid primary keys and not the duplicates, and save that as shorter_toc.txt in the 'subjectInstanceDepth' folder.
1. Create an empty folder called plots_SPUD/
1. Run ActivityLog.py and wait for the graphs to be constructed
