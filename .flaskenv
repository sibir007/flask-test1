# The flask command is implemented using Click https://click.palletsprojects.com/
# flask
# If python-dotenv is installed, 
# running the flask command will set environment 
# variables defined in the files .env and .flaskenv.

FLASK_APP=5test # where to find your application in order to use it
# FLASK_APP=src/hello
#     Sets the current working directory to src then imports hello.
# FLASK_APP=hello.web
#     Imports the path hello.web.
# FLASK_APP=hello:app2
#     Uses the app2 Flask instance in hello.
# FLASK_APP="hello:create_app('dev')"
#     The create_app factory in hello is called with the string 'dev' as the argument.


# environment in which the Flask app runs
# development: enable the interactive debugger and reloader. 
# reloader will trigger whenever your Python code or imported modules change 
FLASK_ENV=development 

# #  reloader can watch additional files
# FLASK_RUN_EXTRA_FILES=file1:dirA/file2:dirB/
FLASK_RUN_EXTRA_FILES=.flaskenv

# # reloader can also ignore files using fnmatch patterns  
# # Multiple patterns are separated with :, or ; on Windows.
# FLASK_RUN_EXCLUDE_PATTERNS=

# # Debug mode will be enabled when FLASK_ENV is development, as described above. 
# # If you want to control debug mode separately, use FLASK_DEBUG. 
# # The value 1 enables it, 0 disables it.
FLASK_DEBUG=1


# FLASK_RUN_PORT=8000 - flask run --port 8000
#  variables use the pattern FLASK_COMMAND_OPTION
# --debug / --no-debug            Set debug mode.

#   -h, --host TEXT                 The interface to bind to.
#   -p, --port INTEGER              The port to bind to.
#   --cert PATH                     Specify a certificate file to use HTTPS.
#   --key FILE                      The key file to use when specifying a
#                                   certificate.
#   --reload / --no-reload          Enable or disable the reloader. By default
#                                   the reloader is active if debug is enabled.
#   --debugger / --no-debugger      Enable or disable the debugger. By default
#                                   the debugger is active if debug is enabled.
#   --with-threads / --without-threads
#                                   Enable or disable multithreading.
#   --extra-files PATH              Extra files that trigger a reload on change.
#                                   Multiple paths are separated by ';'.
#   --exclude-patterns PATH         Files matching these fnmatch patterns will
#                                   not trigger a reload on change. Multiple
#                                   patterns are separated by ';'.

# # Flask not to load dotenv files
# FLASK_SKIP_DOTENV=1