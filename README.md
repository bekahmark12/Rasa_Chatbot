# Rasa_Chatbot
Python Chatbot using RASA Core and NLU


Phase 1 - Install Anaconda

Go to https://www.anaconda.com/products/individual and install the windows 64 bit version of anaconda.

Follow the setup wizard and click BOTH checkboxes, it will suggest not clicking the first one but click it anyways. 

Open Anaconda Prompt (hit your windows key and type anaconda) then run the following commands:
  conda create -n rasa python=3.7 anaconda
  conda activate rasa
  cd <path where it created your anaconda environment>  
    **it usually defaults to the user folder, then from there go to the envs directory and then to rasa.**
  pip install rasa-x --ignore-installed ruamel.yaml --extra-index-url https://pypi.rasa.com/simple --user (if running as administrator, leave off --user)
    This step may need to be repeated several times depending on configuration and settings on local machine.
  rasa init (DO NOT RUN THIS COMMAND MORE THAN ONCE, will wipe any edits you’ve made to files)
  rasa x 
  
Follow the prompts to allow access through your firewall, and accept their user license agreement. 
A localhost gui should open up.

Phase 2 - Download and upload scripts

Option 1 - Download nlu.yml, rules.yml, stories.yml, domain.yml, and 20210303-185416.tar.gz directly into rasa directory within anaconda3 file.
Option 2 - Upload these same files straight into Rasa X GUI after running rasa x command.
