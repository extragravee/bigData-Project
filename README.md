Course contents
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
