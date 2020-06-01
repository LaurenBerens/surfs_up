import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
engine = create_engine("demographics.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
session = Session(engine)
app = Flask(__name__)

* **Instructions**:
​
  * Create engine using the `demographics.sqlite` database file
​
  * Declare a Base using `automap_base()` and use this new Base class to reflect the database's tables
​
  * Assign the demographics table/class to a variable called `Demographics`
​
  * Create a session and use this session to query the `Demographics` table and display the first five locations
​
* **Bonus**:
​
  * Query and print the number of unique locations in the table.
​
* **Hint**:
​
  * For the bonus, look into counting and grouping operations in SQLAlchemy