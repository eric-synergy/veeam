V12 Features 
=============

New capabilities introduced with V12 include:

- Backups going direct to object storage and cloud-based agents are also available as cloud-accelerated features
- With immutability everywhere, ransomware can be recovered, and threats against cyberattacks can be stopped even faster
- Improves efficiency at scale with additional enterprise application support and innovations
- A new Veeam Backup & Replication plug-in for Kasten by Veeam K10 V5.0 provides visibility and management for Kubernetes data protection.

Key Highlights
--------------

.. image:: ../images/v12/v12_01.png


Core Architecture Improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

More Option for VBR Database
""""""""""""""""""""""""""""

Veeam is introducing a new database platform – PostgreSQL v14. 
Some of the reasons for doing so is first and foremost, like MSSQL Express, it’s free. 
But, from a use and scalability perspective, it has no size limit or compute restrictions, 
and has improved performance over SQL Express. 
SQL Express will still be an usable option if it’s your preference. 
PostgreSQL is only going to be in VBR and Enterprise Manager (EM) initially.

SQL Express limitations

- 10 GB maximum database size
- 4 cores maximum
- 1 MB buffer cache

SQL Standard / Enterprise Edition

- Too high costs

Postgres

- Free
- No database size or compute restrictions
- Proven in other Veeam Products
- Performance
