import mysql.connector
from mysql.connector import Error


connection = mysql.connector.connect(host='localhost',database='banks',user='root',password='')
if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to mysql")
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)


    
def login(u, p):

    #Querying user credentials and matching them from database.
    try:
        squery = f"""SELECT username, password FROM users WHERE username = '{u}' AND password = '{p}'"""
        cursor = connection.cursor()
        result = cursor.execute(squery)
    except Error as e:
        print("something went wrong")
    finally:
        try:
            #this checks for results from the query
            res = cursor.fetchall()
            
            # PRINTING ORIGINAL QUERY RESULTS
            print("############################################################################")
            print("###############                                              ###############")
            print("###############         ORIGINAL QUERY RESULTS               ###############")
            print("###############                                              ###############")
            print("############################################################################")


            print(res)

            print("############################################################################")
            print("###############                                              ###############")
            print("###############     RESULTS DUE TO PROGRAM INTERCEPT         ###############")
            print("###############                                              ###############")
            print("############################################################################")
            # matching the expected query results with the inteded input match
            if u == res[0][0] and p == res[0][1]:
                print("Succesfully logged in")  
            else: 
                print("wrong credentials")
        except Error as f:
            print("No results")
        finally:
            print("Results present \n")
        print("Query succesful")

print("####Loggin in####")
# Get rid of characters that could result into the injection
u = input("Enter username: ")
p = input("Enter passowrd: ")


login(u,p)



#HOW THE PROGRAMM CAN BE FIXED FROM SQL INJECTIONS
"""


1. Insecure Packages
When you import a module into a Python application, the interpreter runs the code. 
This means you should be careful when importing modules. 

The PyPi package index is a great resource, but there is no verification that all
the code in libraries listed there is secure. Many malicious packages exist on PyPi, 
some of them attempt to 
trick users by adopting the names of well known libraries with small misspellings. 
If you are unsure of the authenticity and contents of the outer packaging, investigate 
further, and if you are still unsure about its origin or security status, don’t use it.

2. Identifying Vulnerabilities
The first step in preventing vulnerabilities is to create a checklist of security best
practices and review it before releasing your code or promoting it to a test environment. 
You should adhere to these best practices at the development stage, and automatically verify 
them at the testing stage. Ideally, you should adopt automated tools that scan your code at 
all stages of the software development lifecycle (SDLC).

3. Use Linters and Static Analysis Tools
Linters are tools that provide automated recommendations about good coding practices. 
They are a simple form of static application security testing (SAST) tools, which analyze 
source code during the development phase of a project. Linters can be used manually in the 
editor, as part of a local development process, or as part of an automated testing process. 

There are several linters in Python, including:

Pylint—Python’s de facto linter, which emphasizes bad code practices, some of which can lead
to vulnerabilities. However, it does not provide extensive security recommendations.
Bandit—you can use this tool to discover common security issues in Python code. Bandit processes 
each file, creates an AST node, and runs the appropriate plugin to test it.
Python IDEs like PyCharm and Wingware have these tools and others will be built in, as well as 
plugins for text editors that can provide security guidance.
Related content: Read our guide to SAST

4. Use Dynamic Application Security Testing
Dynamic Analysis Security Testing Tool, or DAST Testing, is an application security solution that 
helps web developers discover specific vulnerabilities while running in staging or production 
environments.

DAST testing can find a wide range of vulnerabilities, including I/O validation issues that can 
make applications vulnerable to SQL injection attacks. The major benefit of DAST testing is that 
it can validate that a vulnerability is really exploitable—meaning that attackers can actually 
perform a successful SQL injection attack. DAST testing can also help identify misconfigurations 
and errors that could lead to a SQL injection attack.

"""