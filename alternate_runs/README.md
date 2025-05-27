# Guide to use alternate_runs script

This folder contains code to run PTRIG and TLOGIC tests back to back for a specified number of runs.

## Usage

- Changing run_num will tell the code how many PTRIG/TLOGIC tests you would like to run. For example, two runs would result in a PTRIG test, then TLOGIC, then PTRIG, and then TLOGIC again.

- Both runtime variables dictate how long the PTRIG and TLOGIC tests run

## The Code Itself

If you're interested in changing the code itself, here is a quick walkthrough of the less obvious sections.

- You may notice I copy config_PTRIG.txt into the Janus_Config.txt file, and do the same with config_TLOGIC.txt. This is because the Janus software only reads Janus_Config when collecting data. The PTRIG and TLOGIC config files have each specify different settings, and we get Janus to read these setting by loading each file into Janus_Config

- The usage of tmux here is to navigate the Janus console automatically, since the console only takes single letter commands instead of bash commands. Tmux opens the Janus console (JanusC) in a detached tmux session, which allows the process to keep running even if the terminal is closed or you log out. It also allows us to send key inputs to the console, which I use to "s" to start the run and "S" to stop it after a specified runtime.
