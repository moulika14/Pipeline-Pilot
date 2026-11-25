\# Pipeline-Pilot — Database Schema Documentation



\## 1. Overview



Pipeline-Pilot uses SQLite as its database to store project validation history. SQLAlchemy is used as the Object Relational Mapper (ORM) to manage database operations.



\- \*\*Database:\*\* SQLite

\- \*\*Database file:\*\* `backend/app/data/pipeline\_pilot.db`

\- \*\*ORM:\*\* SQLAlchemy

\- \*\*Table:\*\* `validation\_records`



\## 2. Database Schema



\### Table: `validation\_records`



| Column | Data Type | Constraints | Description |

|---|---|---|---|

| id | VARCHAR | Primary Key, NOT NULL | Unique validation record identifier |

| timestamp | VARCHAR | NOT NULL | Date and time of validation |

| report | JSON | NOT NULL | Stores the validation report data |



Each row represents one project validation record.



\## 3. Entity Relationship Diagram



```mermaid

erDiagram

&#x20;   VALIDATION\_RECORDS {

&#x20;       VARCHAR id PK

&#x20;       VARCHAR timestamp

&#x20;       JSON report

&#x20;   }

```



The current database contains one table, so no inter-table relationships are required.



\## 4. Database Connection



The database connection is configured in:



`backend/app/database/connection.py`



SQLAlchemy creates the SQLite engine and session factory. The database directory is created automatically when required.



\## 5. Database Model



The database model is defined in:



`backend/app/database/models.py`



The `ValidationRecord` model maps the Python application to the `validation\_records` table.



\## 6. CRUD Operations



Pipeline-Pilot implements the following database operations:



\- \*\*Create:\*\* Save a new validation report.

\- \*\*Read:\*\* Retrieve all validation records or a specific record.

\- \*\*Update:\*\* Modify an existing validation report.

\- \*\*Delete:\*\* Remove a selected validation record.



These operations are exposed through FastAPI endpoints.



\## 7. Data Migration



Existing validation records were migrated from `validation\_history.json` into SQLite. Eight existing records were successfully migrated, and the original JSON backup was preserved.



\## 8. Verification Results



\- Database connection: Successful

\- Table creation: Successful

\- Table name: `validation\_records`

\- Columns verified: 3

\- Records stored: 10

\- CRUD operations: Tested successfully



\## 9. Conclusion



The SQLite database is integrated with Pipeline-Pilot. Validation history is now persisted using SQLAlchemy, with support for Create, Read, Update, and Delete operations.

