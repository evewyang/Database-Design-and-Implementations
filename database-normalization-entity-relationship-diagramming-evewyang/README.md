# Data Normalization and Entity-Relationship Diagramming

An assignment to normalize the structure of data and establish a set of Entity-Relationship Diagrams for the data.

|assignment_id|student_id|due_date|professor|assignment_topic               |classroom|grade|relevant_reading   |professor_email  |
|-------------|----------|--------|---------|-------------------------------|---------|-----|-------------------|-----------------|
|1            |1         |23.02.21|Melvin   |Data normalization             |WWH 101  |80   |Deumlich Chapter 3 |l.melvin@foo.edu |
|2            |7         |18.11.21|Logston  |Single table queries           |60FA 314 |25   |Dümmlers Chapter 11|e.logston@foo.edu|
|1            |4         |23.02.21|Melvin   |Data normalization             |WWH 101  |75   |Deumlich Chapter 3 |l.melvin@foo.edu |
|5            |2         |05.05.21|Logston  |Python and pandas              |60FA 314 |92   |Dümmlers Chapter 14|e.logston@foo.edu|
|4            |2         |04.07.21|Nevarez  |Spreadsheet aggregate functions|WWH 201  |65   |Zehnder Page 87    |i.nevarez@foo.edu|
|...          |...       |...     |...      |...                            |...      |...  |...                |...              |

### Prerequisites 
4th Normalization is concerned with multi-valued facts. To qualify for a 4th Normalization form, the table need to be:
- satisfy the requirements of 1st,2nd,3rd normal form
- all values should be singular
    - A non-key field must provide a fact about the entity uniquely identified by the primary key, neither part of it
    - A non-key field cannot contain facts about another non-key field
- not containing more than one independent multi-valued fact about an entity
- need to deal with redundancy and anomalies at the same time

### More Assumptions
Also, we need to assume that one specific assignment can be only assigned by one specific professor. For example, given `assignmnet_id` = 1, we know that it must be assigned by professor Melvin, and the assignment_topic is "Data Normalization" and relevant_reading is "Deumlich Chapter 3". The same professor can only assign the same homework to different sections of the same course with different `due_date`. In other words, given `assignment_id` and `due_date`, we can specifically determine a class, where class is defined by a unique combination of a course and a section.

### Problems
The given data doesn't qualify for a 4th normalization form. As the table represents students' grade, the primary key should be composite, composed by `assignment_id, student_id, due_date`. The due_date added on should help with unique identification of a course as the professor can assign the same assignment(i.e. same assignment_id) with difference due dates. Yet, in this case, many field can only contain facts about part of the primary key. Field `assignment_topic`, `relevant_reading` is only associated with `assignment_id`; `classroom` is associted with `assignment_id` and `due_date` but not with `student_id`, etc. Some field contains fact about another non-key field: `professor_email` is only about `professor` and `relevant_reading` can also describe `assignment_topic`. <br>
The data redundancy and anomalies are severe in this table. Eedundancy happens as there are repitation of facts in multiple places within the data, such as professor's email, location, assignment topic and so on. This will cause update anomalies, since that updating a professor's email requires updating multiple records, for instance. Deletion anomalies can also occur in current structure. For example, if student with 2 is the only student in Prof. Nevarez's class, and Prof. Nevarez has only one class to teach, and there has been only one assignment yet, or even say that classroom has only one class taking place. If he wants to drop the grade, the Prof's email address is deleted entirely from the table, and the location of classroom will also be missing.  

### Normalization to 4NF
By seperating the original table into several tables, each "specializing" in storing a small part of the information of records, 4NF can be achieved. Now each table has improvement in non-redundancy and non-anomalies; all values are singular; non-key fields are independent and provide a fact about the primary key; finally each of them does not contain more than one independent multi-valued fact about an entity. <br>
Tables are initially defined by composite primary keys(e.g. for grade table, PRIMARY KEY(assignment_of_a_class_id, student_id)), yet singular surrogate key fields containing an auto-incrementing arbitrary integer are used for tables in preference of composite keys for easier referencing.<br>
Shown below are the seperated tables in 4NF. Primary key(s) of a table is marked in Italic. 
#### i) Grade Table:
This table is the top-most table of all tables in logic. 
|*id* |assignment_of_a_class_id|student_id|grade|
|---|------------------------|----------|-----|
|1  |1                       |1         |80   |
|2  |2                       |2         |25   |
|3  |1                       |3         |75   |
|4  |3                       |4         |92   |
|5  |4                       |4         |65   |
|...|...                     |...       |...  |

Here, `id` is the primary key of the grade table as increasing natural numbers, `assignment_of_a_class_id` is the foreign key linking to assignment_of_a_class table, and `student_id` is the foreign key linking to student table. So, each grade should be defined by the specific assignment of that class and id of a student, owner of this grade.  

#### ii) Assignment Table: 
This table records all types of assignments existing in the univeristy, and the relevant information including which professor assigns it, topic and relevant readings. I made this seperation because one teacher can assign one specific assignment to many different sections of a course, and this seperation avoids redundancy. 
|*id* |professor_id|assignment_topic|relevant_reading   |
|---|------------|----------------|-------------------|
|1  |1           |Data normalization|Deumlich Chapter 3 |
|2  |2           |Single table queries|Dümmlers Chapter 11|
|...|...         |...             |...                |
|4  |3           |Spreadsheet aggregate functions|Zehnder Page 87    |
|5  |2           |Python and pandas|Dümmlers Chapter 14|
|...|...         |...             |...                |

#### iii) Assignment_of_a_class Table:
This table adds on the due_date to a specific type of assignment. Assignment_id and due_date uniquely defines an assignment of that class. I do this because grade is relevant to assignment of that specific class, not a type of assignment. 

|*id* |assignment_id|due_date |
|---|-------------|---------|
|1  |1            |23.02.21 |
|2  |2            |18.11.21 |
|3  |5            |05.05.21 |
|4  |4            |04.07.21 |
|...|...          |...      |

And note that `assignment_id` and `due_date` are independet fields, and here their combinations makes up for unique records.

#### iv) Student Table:
|*id* |student_id|
|---|----------|
|1  | 1        |
|2  | 7        |
|3  | 4        |
|4  | 2        |
|...|...       |

It seems unnecessary to have another column of `id` as primary key besides `student_id`, since `student_id` are all integers. However, it is unclear in the original table about whether the `student_id` are all in integer form, or it can be something else like our school's NetId. Let's assume there can be other form of student id's. Then adding a column of naturally increasing primary keys allows the flexibility of possible changing in `student_id`, easiness of searching, and integrity of record keeping.  

#### v) Professor Table:
This table record information of all professors. 

|*id* |professor_name|professor_email   |
|---|--------------|------------------|
|1  | Melvin       | l.melvin@foo.edu |
|2  | Logston      | e.logston@foo.edu|
|3  | Nevarez      | i.nevarez@foo.edu|
|...|...           |...               |

#### vi) Class Table:
|*id* |professor_id|classroom_id|
|---|------------|------------|
|1  | 1          |1           |
|2  | 2          |2           |
|3  | 3          |3           |
|...|...         |...         |

I make this an entity because of assumption 1&2, and the class(a unique combination of course and its section) is meaningful for itself. Possibly, there can be one line like:

|*id* |professor_id|classroom_id|
|-----|------------|------------|
|100  | 1          |3           |

Same professor may teach same/different class in different room, or:

|*id* |professor_id|classroom_id|
|-----|------------|------------|
|200  | 3          |1           |

Different professors may teach same/different class in the same room.<br>
Usually, as in Albert, finding a course need the procedure "search course-->search section", so to make this entity more robust, more information of `course_number` and `section_number` should be provided for uniqueness of each record. Here, I just assume that class can be identified by its `id` so that it satisfies 4NF. 

#### vii) Classroom Table:
|*id* |location|
|---|--------|
|1  | WWH 101|
|2  | 60FA 314|
|3  | WWH 201|
|...|...     |

This entity is constructed to save all classroom's location, and by assigning each of them an unique id it avoids deletion anomalies. There is only one attribute, and its all about the primary key, so this is 4NF. 

### ER Diagram
Here is the ER Diagram for the normalized tables:
<img src="images/er_diagram.drawio.svg" alt="ER Diagram">
The yellow colored attributes are actually not provided in the original table. I added it as a "pending" state to indicate the definition of a class, which is determined uniquely by `course_number` and its `section_number`, a similar logic as in Albert. 