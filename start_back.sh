
#!/bin/bash

cd b_backend
(cd data && ./create-db.sh) # run in a subshell, so does not change "b_backend"
uvicorn main:app --reload
