from cli import run_cli

if __name__ == "__main__":
    run_cli()


"""
    Before running commands, please prepare your environment by following these instructions:

        1. Please cd task_3 
        

        2. To initialize db, Firstly you need to add connection to mysql (using workbench Will simplify the process)
           Please keep in mind, you need to use your Mysql user Password, otherwise it returns "Connection failed: Access Denied" 
           Connection name and Username can be default: localhost, root ( can be different, if you grant access to other users)
           

        3. there are two commands availabe to run: - initdb  
                                                   - execute 
            by running --> uv run py main.py initdb <-- we initialize whole process:  
                                                                            Connection to mysql server, 
                                                                            Creating database,
                                                                            Connection to database,
                                                                            Creating tables (students, rooms)
                                                                            Loading and inserting data,
                                                                            Creating Indexes.
        
         
            by running execute command you be able to retrieve data as requested:   
                                                                                - List of rooms and the number of students in each.
                                                                                - Top 5 rooms with the smallest average student age
                                                                                - Top 5 rooms with the largest age difference among students
                                                                                - List of rooms where students of different sexes live together
             To achieve that, we need to specify query:  
                                                      largest_age_difference,
                                                      count_students_in_room,
                                                      smallest_average_age,
                                                      different_sex_in_room, 

            Full command would look like this:  --> uv run py main.py execute smallest_average_age  <--



"""
