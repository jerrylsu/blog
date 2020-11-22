Status: published
Date: 2019-05-23 06:42:23
Author: Jerry Su
Slug: Using-groupBy-on-multiple-columns
Title: Using groupBy on multiple columns
Category: 
Tags: Python


Group By X means put all those with the same value for X in the one group.

Group By X, Y means put all those with the same values for both X and Y in the one group.

To illustrate using an example, let's say we have the following table, to do with who is attending what subject at a university:

Table: Subject_Selection

```
Subject   Semester   Attendee
---------------------------------
ITB001    1          John
ITB001    1          Bob
ITB001    1          Mickey
ITB001    2          Jenny
ITB001    2          James
MKB114    1          John
MKB114    1          Erica
```
When you use a group by on the subject column only; say:

```
select Subject, Count(*)
from Subject_Selection
group by Subject
You will get something like:
```

```
Subject    Count
------------------------------
ITB001     5
MKB114     2
```

...because there are 5 entries for ITB001, and 2 for MKB114

If we were to group by two columns:

```
select Subject, Semester, Count(*)
from Subject_Selection
group by Subject, Semester
```

we would get this:

```
Subject    Semester   Count
------------------------------
ITB001     1          3
ITB001     2          2
MKB114     1          2
```

This is because, when we group by two columns, it is saying **"Group them so that all of those with the same Subject and Semester are in the same group, and then calculate all the aggregate functions (Count, Sum, Average, etc.) for each of those groups".** 