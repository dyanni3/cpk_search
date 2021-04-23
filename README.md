# cpk_search
search text chicago police killing text documents

![Screen Shot 2021-04-23 at 10 54 19 AM](https://user-images.githubusercontent.com/19617527/115890130-9c1e3200-a422-11eb-99ef-859fc2b054f1.png)

## How to use

1) Download the text data (email David for link)
2) Download and install python (3.X)
3) Clone this repo or copy the files into the same directory as the text data
4) Open up a terminal and navigate to the data directory
5) Install the requirements `pip install -r requirements.txt`
6) Index the documents (stores & organizes all the terms for future searching use, only do this the first time you set up the project) `python whoosh_index.py` on mac and `py whoosh_index.py` on Windows
7) Now run the search program! `python search.py` on mac and `py search.py` on windows. You should see an interactive command line interface like in the screenshot above :smile:
8) Using the program should be self explanatory, email David with questions and/or requests for additional functionality.


On subsequent runs you only need to open up a terminal window, navigate to the folder, and start the search program.
