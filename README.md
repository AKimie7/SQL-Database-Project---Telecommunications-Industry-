# SQL-Database-Project---Telecommunications-Industry-

The telecommunications industry plays a crucial role in the lives of people and businesses worldwide. It is growing rapidly, and innovation in specific sectors or regions is tied to the development of local telecommunication networks. With the rise of digital transformation, network reliability and speed have become more critical than ever (Statista,2023). Therefore, analyzing performance data is essential for businesses in this industry to stay ahead of their fast-paced competitors and future-proof their operations.  
The business case I am examining classifies within this industry, operating as a flexible, no-contract mobile plan provider, named "Sprint" (made-up). Due to rapid technological advancements, intense competition, and changing customer demands, it is essential for businesses to continuously improve their network coverage, data speeds, and service offerings. The telecommunications industry deals with a lot of data, which poses challenges in managing network traffic, ensuring high-quality service, analyzing customer usage patterns, maintaining competitive pricing strategies, and forming partnerships with international roaming services. In addition, companies must comply with industry regulations and adapt to the constantly evolving technological landscape.  

1.	Users Table:
•	This table doesn't have any direct dependencies on other tables but will serve as a central reference point for other tables.
2.	Plans Table:
•	referenced by the "Users" table as users are associated with specific plans.
3.	Top-Up Transactions Table:
•	It has a foreign key reference to the "Users" table, associating transactions with specific users.
4.	Call Records Table:
•	References the "Users" table to associate calls with specific users.
5.	Message Records Table:
•	References the "Users" table.
6.	Network Towers Table:
•	Doesn't have direct dependencies on other tables
7.	Cancellation Reasons Table:
•	References the "Users" table to associate cancellation reasons with specific users.
8.	My Data Table:
•	It has a foreign key reference to the "Users" table to associate this data with individual users.
9.	Customer Reviews Table:
•	References the "Users" table to associate reviews with specific users.
10.	Roaming Locations Table:
•	It has a foreign key reference to the "Users" table to associate roaming locations with specific users.

I have created 50 sample data entries for each table based on the entity attributes and their respective data types. To expedite the process, I used Github-Copilot to generate additional rows. I also utilized Chat GPT by submitting the following command: "Given the SQL Tables from MVO Dataset <insert SQL code>, analyze the table structure and its columns, generate realistic data entries based on the proposed business case from <description of case study>, and generate a minimum of 50 entries." However, I had to make some changes to the generated data such as deleting the message content to protect user privacy, changing the cellphone numbers to UK numbers, and modifying the location to UK cities and postcodes.

The "plans" table is a crucial entity in any telecom company's operations. It facilitates efficient management and oversight of the services provided by the company. This table helps businesses maintain an organized record of various service plans offered, including plan names, data allowances, talk time, text message quotas, and associated prices. By linking the pricing table with users' information, the business can analyze trends based on geographic location, age, and profession, and adjust pricing strategies and plan offers to retain customers. For example, they can offer promotional student codes and partnerships with universities and student accommodations. Lastly, by comparing their service plans with those offered by competitors, companies can identify gaps and opportunities in the industry.

Call and message records provide important data on call duration and usage, which can be used to calculate call expenses and analyze customer behavior. These records can also be reviewed for quality validation goals, helping to monitor the network and identify issues such as call drops, weak connections, and other network-related issues. By leveraging this data, Sprint can identify areas with frequent call drops or weak signals and take the required steps to improve them. Moreover, call records allow tracking of roaming usage and charges for users who are outside the network's range area. This way, Sprint can analyze geographic locations and create partnerships with international companies.

The information collected from this table can be utilized to create a customer churn analysis, which will help identify the common issues or pain points that need to be addressed to reduce churn. For instance, if network coverage issues are a common reason behind customer loss, Stint knows to invest in expanding its network coverage. Similarly, if financial constraints are a frequent reason for customer churn, the business may need to offer more affordable plans or discounts to its customers. Additionally, this data can also be used for marketing ((KPI) - to track the success of customer retention efforts over time). Furthermore, it is also important for regulatory and compliance purposes. For example, the table can store reasons related to compliance issues, if any, for documentation.

Relationship, Cardinality & Participation
Users - MyData
•	Relationship: Users can have multiple data usage records.
•	Cardinality: One-to-Many (One User entity can relate to multiple MyData entities).
•	Participation: Mandatory (A user must have at least one data usage record).
Users - TopUpTransactions
•	Relationship: Users can initiate multiple top-up transactions.
•	Cardinality: One-to-Many (One User entity can relate to multiple TopUpTransaction entities).
•	Participation: Optional (A user may or may not have top-up transactions).
Users - CancellationReasons
•	Relationship: Users can have multiple cancellation reasons.
•	Cardinality: One-to-Many (One User entity can relate to multiple CancellationReason entities).
•	Participation: Optional (A user may or may not have cancellation reasons).
Users - CustomerReviews
•	Relationship: Users can write multiple customer reviews.
•	Cardinality: One-to-Many (One User entity can relate to multiple CustomerReview entities).
•	Participation: Optional (A user may or may not write customer reviews).
Plans - Users
•	Relationship: Each user is associated with a specific plan.
•	Cardinality: One-to-Many (One Plan entity can relate to multiple User entities).
•	Participation: Mandatory (Every user must have a plan).
Users - MyData
•	Relationship: Users can have multiple data usage records.
•	Cardinality: One-to-Many (One User entity can relate to multiple MyData entities).
•	Participation: Mandatory (A user must have at least one data usage record).
MyData - CallRecords
•	Relationship: Data usage records can have multiple call records.
•	Cardinality: One-to-Many (One MyData entity can relate to multiple CallRecord entities).
•	Participation: Optional (A data usage record may or may not have call records).
Users - RoamingLocations
•	Relationship: Users can have multiple roaming locations.
•	Cardinality: One-to-Many (One User entity can relate to multiple RoamingLocation entities).
•	Participation: Optional (A user may or may not have roaming locations).
Users - CallRecords
•	Relationship: Users can have multiple call records.
•	Cardinality: One-to-Many (One User entity can relate to multiple CallRecord entities).
•	Participation: Optional (A user may or may not have call records). 
Users - MessageRecords
•	Relationship: Users can have multiple message records.
•	Cardinality: One-to-Many (One User entity can relate to multiple MessageRecord entities).
•	Participation: Optional (A user may or may not have message records).
NetworkTowers - CallRecords
•	Relationship: Call records are associated with specific network towers.
•	Cardinality: Many-to-One (Multiple CallRecord entities can relate to one NetworkTower entity).
•	Participation: Mandatory (Every call record must be associated with a network tower). 
My Data - MessageRecords
•	Relationship: Data usage records (MyData) can have multiple message records.
•	Cardinality: One-to-Many (One data usage record in the MyData table can be associated with multiple message records in the MessageRecords table).
•	Participation: Optional (A data usage record may or may not have associated message records).
 
 ![image](https://github.com/AKimie7/SQL-Database-Project---Telecommunications-Industry-/assets/145045818/f04b8e55-ad3f-4fd2-aec9-695ffe910fef)


