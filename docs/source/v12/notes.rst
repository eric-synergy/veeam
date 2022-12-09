

Note Taking Veeam v12 Capabilities for Service Providers
 This blog post is note-taking for Veeam v12 Capabilities for Service Providers



1. Support for Postgres for VBR and Enterprise Manager

Open Source Database
Performance & Scalability
Microsoft SQL Server is still available to use
Upgrade path 
a) EM to v12-> VBR to v12 -> Migrate EM to Postgres -> Migrate VBR to Postgres
The backup server & Enterprise Manager must have the same database type
Reduce licensing cost
2. CDP proxy on Linux

3. Linux Gateway & Proxies

to proxy access object storage

3. Move Machines between backup job

4. Retry one machine instead of whole job

5. Trigger active full for one VM

6. Separate health check schedule

7. VeeaMover

move back up to a different repository
Migrate Refs to XFS, NTFS-> Refs
Rebalance SOBR
Copy backup to a different repository
8. Security

gMSA and Keberos support
Multi-Factor Authentication (MFA) for Veeam Console
Protect IaaS environment
Protect cloud connect environment
Protect MSP environments
Auto log off after X minutes
Classified data marking
9. Object storage & SOBR

Direct to Object Storage
End-to-End Storage for SOBR
New object storage format
reduce transactional overheads and streamlines IO
SOBR rebalance
10. Self Service Portal Enhancement

Instant VM Recovery capability on EM by tenant
Available on vSphere and Vmware Cloud Director
11. Automation & API

Powershell 
12. Continuous Data Protection for Cloud Cloud with Vmware Cloud Director

CDP for IaaS (vcloud director) or CDP via Cloud Connect (vcloud director)
Replication
Failover vApps between virtual datacenter
Different vcloud director server are supported
13. Restore from Cloud Connect as the Service Provider Restore

14. VSPC v7 Integration

a)Self Service FLR for VSPC managed agent

self service portal for users
delegated restore (by a service provider or reseller)
Support for Windows/Linux/Mac
b) VBR patching and updating

c) CDP Policies support

d) Veeam Backup Appliance (public cloud) -orchestrate VB appliance creation